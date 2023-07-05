# Python HM template

## Pre-Reqs

- Python3
- Docker + docker-compose

## What's included?

- Basic FastAPI server
- Docker compose with redis
- Basic Celery task worker

## How to setup?

Just run:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to run?

### Redis

```sh
docker-compose up
```

### Server

Just run:

```sh
uvicorn main:app --reload
```

### Celery Worker

Just run:

```sh
celery -A tasks.celery_app worker
```

## How to test Celery?

Insert the test job by running the following cUrl:

```sh
curl --location --request POST 'localhost:8000/task?message=hi'
```
