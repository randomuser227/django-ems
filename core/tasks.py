# from event_management.celery import app
from celery import Celery
from time import sleep
from celery import shared_task


#broker rabbitmq or redis
# app = Celery('tasks', broker = '')
# app = Celery('event_management', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0', include=['tasks'])

# app.autodiscover_tasks()

# @app.task(bind=True)
# def send_email(self):
#     # sleep(2)
#     print("email sent to customer")

@shared_task()
def send_email():
    # sleep(2)
    print("email sent to customer")
    return "Completed"

# @app.task
def test():
    print("testing")


    
