# -*- coding: utf-8 -*-
# add_task.py


from celery import Celery

app = Celery('add_task', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y