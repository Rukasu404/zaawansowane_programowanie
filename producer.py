"""Producer - publikuje pracę do kolejki RabbitMQ (status: pending).

Każde uruchomienie = 1 praca (1 rozmowa telefoniczna).
Opcjonalnie: `--count 100` publikuje 100 prac.
"""
import argparse
import json
import os
import time
import uuid

import pika

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
QUEUE = "jobs"


def now():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def main():
    parser = argparse.ArgumentParser(description="Dodaje prace do kolejki")
    parser.add_argument("--count", type=int, default=1,
                        help="ile prac dodać (domyślnie 1)")
    args = parser.parse_args()

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS),
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE, durable=True)  # kolejka przeżyje restart brokera
    channel.confirm_delivery()  # broker potwierdza, że przyjął wiadomość

    for _ in range(args.count):
        job = {
            "id": uuid.uuid4().hex[:8],
            "status": "pending",
            "created_at": now(),
        }
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE,
            body=json.dumps(job),
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
        print(f"[producer] dodano pracę {job['id']} ({job['status']})", flush=True)

    connection.close()


if __name__ == "__main__":
    main()
