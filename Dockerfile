# Docker image for Python image base
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY test_app.py test_app.py

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]