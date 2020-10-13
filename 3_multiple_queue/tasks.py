from celery import Celery

app = Celery('tasks', broker='redis://guest@localhost//')

@app.task()
def task_1(a,b):
    print ("task_1 called")
    if (a+b < 100):
        task_1.apply_async(queue='queueB', args=(a*10, b*10))
    #task_2.apply_async(queue='queueB')


@app.task()
def task_2():
    print ("task_2 called")
