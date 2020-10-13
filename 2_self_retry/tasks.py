# tasks.py

from celery import Celery

app = Celery('tasks_retry', broker='redis://guest@localhost//')

@app.task(bind=True, max_retries=3)
def add_retry(self,x, y):
    z = x + y
    print(' times, ' +  str(z))

    if (z < 100):
        self.retry(countdown=2)

    return x + y
