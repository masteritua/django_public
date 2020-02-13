from celery import shared_task
from celery import Celery
from celery.schedules import crontab
from datetime import datetime, timedelta
from Student.models import Logger


@shared_task
def clear_log():
    d = datetime.today() - timedelta(days=1)
    Logger.objects.filter(created__lt=d).delete()


app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(hour=0, minute=0, day_of_week=7),
        clear_log()
    )