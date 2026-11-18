FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY producer.py consumer.py ./

# Domyślnie uruchamiany jest consumer; producer nadpisuje entrypoint w docker-compose
CMD ["python", "-u", "consumer.py"]
