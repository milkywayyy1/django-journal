from django_journal.celery import app


@app.task
def send_notification(user_email):
    return user_email
