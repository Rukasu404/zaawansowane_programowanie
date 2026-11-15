"""Producer - zapisuje do pliku pracę do wykonania (status: pending).

Każde uruchomienie = 1 rekord (1 rozmowa telefoniczna).
Opcjonalnie: `python producer.py --count 100` dodaje 100 prac.
"""
import argparse
import uuid

from queue_file import PENDING, file_lock, now, read_jobs, write_jobs


def main():
    parser = argparse.ArgumentParser(description="Dodaje prace do kolejki")
    parser.add_argument("--count", type=int, default=1,
                        help="ile prac dodać (domyślnie 1)")
    args = parser.parse_args()

    for _ in range(args.count):
        job = {
            "id": uuid.uuid4().hex[:8],
            "status": PENDING,
            "created_at": now(),
            "started_at": "",
            "finished_at": "",
            "consumer": "",
        }
        with file_lock():
            jobs = read_jobs()
            jobs.append(job)
            write_jobs(jobs)
        print(f"[producer] dodano pracę {job['id']} ({job['status']})")


if __name__ == "__main__":
    main()