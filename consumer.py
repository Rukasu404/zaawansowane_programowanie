"""Consumer - odbiera prace z RabbitMQ i wykonuje je (30 s każda).

Statusy w RabbitMQ:
  pending      -> wiadomość czeka w kolejce (Ready)
  in_progress  -> wiadomość dostarczona do consumera, jeszcze bez ack (Unacked)
  done         -> consumer wysłał ack, wiadomość znika z kolejki
"""
import json
import os
import socket
import time

import pika

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
QUEUE = "jobs"
WORK_DURATION = int(os.getenv("WORK_DURATION", "30"))  # sekundy na jedną pracę

NAME = f"consumer-{socket.gethostname()}"


def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{NAME}] {msg}", flush=True)


def connect():
    """Łączy się z RabbitMQ, ponawiając próby aż broker będzie gotowy."""
    while True:
        try:
            return pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=RABBITMQ_HOST,
                    credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS),
                    heartbeat=60,
                )
            )
        except pika.exceptions.AMQPConnectionError:
            log("RabbitMQ jeszcze niedostępny, próbuję za 5 s...")
            time.sleep(5)


def main():
    connection = connect()
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE, durable=True)
    # Brak nowej pracy dopóki poprzednia nie dostanie ack -
    # dzięki temu prace rozdzielają się równo między consumerów.
    channel.basic_qos(prefetch_count=1)

    def on_message(ch, method, properties, body):
        job = json.loads(body)
        log(f"pobrano pracę {job['id']} -> in_progress")

        # Symulacja rozmowy. connection.sleep (zamiast time.sleep) obsługuje
        # heartbeaty, więc połączenie nie zostanie zerwane podczas 30 s pracy.
        connection.sleep(WORK_DURATION)

        # ack = praca wykonana. Gdy consumer padnie przed ack, RabbitMQ
        # automatycznie odda pracę do kolejki innemu consumerowi.
        ch.basic_ack(delivery_tag=method.delivery_tag)
        log(f"praca {job['id']} -> done")

    channel.basic_consume(queue=QUEUE, on_message_callback=on_message)
    log("start, czekam na prace...")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("zatrzymany")
