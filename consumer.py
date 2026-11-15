"""Consumer - w pętli sprawdza plik i wykonuje prace (pending -> in_progress -> done).

Można uruchomić wielu konsumerów równolegle - każda praca trafi
tylko do jednego z nich dzięki blokadzie pliku.
"""
import os
import time

from queue_file import (DONE, IN_PROGRESS, PENDING, file_lock, now,
                        read_jobs, write_jobs)

POLL_INTERVAL = 5   # co ile sekund sprawdzamy plik
WORK_DURATION = 30  # tyle trwa wykonanie jednej pracy

NAME = f"consumer-{os.getpid()}"


def log(msg):
    print(f"[{now()}] [{NAME}] {msg}", flush=True)


def claim_job():
    """Znajduje pierwszą pracę 'pending' i zmienia jej status na 'in_progress'.

    Odczyt i zapis odbywają się pod jedną blokadą, więc dwóch konsumerów
    nie weźmie tej samej pracy.
    """
    with file_lock():
        jobs = read_jobs()
        for job in jobs:
            if job["status"] == PENDING:
                job["status"] = IN_PROGRESS
                job["started_at"] = now()
                job["consumer"] = NAME
                write_jobs(jobs)
                return job
    return None


def finish_job(job_id):
    """Zmienia status pracy na 'done'."""
    with file_lock():
        jobs = read_jobs()
        for job in jobs:
            if job["id"] == job_id:
                job["status"] = DONE
                job["finished_at"] = now()
                break
        write_jobs(jobs)


def main():
    log("start, czekam na prace...")
    while True:
        job = claim_job()
        if job is None:
            time.sleep(POLL_INTERVAL)
            continue

        log(f"pobrano pracę {job['id']} -> in_progress")
        time.sleep(WORK_DURATION)  # symulacja rozmowy telefonicznej
        finish_job(job["id"])
        log(f"praca {job['id']} -> done")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("zatrzymany")