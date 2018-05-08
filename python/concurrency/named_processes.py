# -*- coding: utf-8 -*-
# named_processes.py


import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting {}".format(name))
    time.sleep(3)
    print("Exiting {}".format(name))


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name="foo_process", target=foo)
    process_without_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_without_name.start()
    process_with_name.join()
    process_without_name.join()