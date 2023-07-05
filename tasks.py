from time import sleep
from celery import Celery

celery_app = Celery(
    "celery_blog", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@celery_app.task
def create_task(message):
    print(f"Celery task received: {message}")
    sleep(5)
    print("Celery task done!")
