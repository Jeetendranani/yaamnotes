# -*- coding: utf-8 -*-
# daemon_process.py


import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Staring {}".format(name))
    time.sleep(3)
    print("Exiting {}".format(name))


if __name__ == '__main__':
    background_process = multiprocessing.Process(name="background_process", target=foo)
    background_process.daemon = True

    frontend_process = multiprocessing.Process(name="frontend_process", target=foo)
    frontend_process.daemon = False

    background_process.start()
    frontend_process.start()

    background_process.join()
    frontend_process.join()