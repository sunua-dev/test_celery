# tasks.py

from celery import Celery

app = Celery('tasks', broker='redis://guest@localhost//')

@app.task
def add(x, y, MAX_COUNT):
    z = x + y
    print(str(MAX_COUNT) + ' times, ' +  str(z))

    if (z < 100) and (MAX_COUNT <= 10):
        add(x + 10, y + 10, MAX_COUNT + 1)

    return x + y
