# -*- coding: utf-8 -*-
# countdown.py


def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)


countdown(15)
