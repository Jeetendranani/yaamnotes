# -*- coding: utf-8 -*-
# run_task.py

from celery_framework import add_task


if __name__ == '__main__':
    result = add_task.add.delay(5, 5)
    print("something")
