"""Wspólne funkcje dla producera i consumera: kolejka oparta o plik CSV.

Dostęp do pliku jest chroniony blokadą (lock file), dzięki czemu
wielu konsumerów i producerów może pracować równocześnie bez
nadpisywania sobie zmian i bez pobierania tej samej pracy dwa razy.
"""
import csv
import os
import time
from contextlib import contextmanager

QUEUE_FILE = "queue.csv"
LOCK_FILE = QUEUE_FILE + ".lock"
FIELDS = ["id", "status", "created_at", "started_at", "finished_at", "consumer"]

PENDING = "pending"
IN_PROGRESS = "in_progress"
DONE = "done"

STALE_LOCK_SECONDS = 10  # blokada starsza niż to jest uznawana za porzuconą


@contextmanager
def file_lock():
    """Prosta blokada międzyprocesowa (działa na Windows, Linux i macOS).

    os.open z O_CREAT | O_EXCL jest atomowe - tylko jeden proces
    może utworzyć plik blokady w danym momencie.
    """
    while True:
        try:
            fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError:
            try:
                if time.time() - os.path.getmtime(LOCK_FILE) > STALE_LOCK_SECONDS:
                    os.remove(LOCK_FILE)  # proces z blokadą prawdopodobnie padł
                    continue
            except FileNotFoundError:
                continue
            time.sleep(0.05)
    try:
        yield
    finally:
        os.close(fd)
        try:
            os.remove(LOCK_FILE)
        except FileNotFoundError:
            pass


def read_jobs():
    """Zwraca listę prac (słowników). Wywoływać wewnątrz file_lock()."""
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_jobs(jobs):
    """Zapisuje całą listę prac atomowo. Wywoływać wewnątrz file_lock()."""
    tmp = QUEUE_FILE + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(jobs)
    os.replace(tmp, QUEUE_FILE)


def now():
    return time.strftime("%Y-%m-%d %H:%M:%S")