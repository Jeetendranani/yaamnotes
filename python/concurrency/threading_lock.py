# -*- coding: utf-8 -*-
# threading_lock.py


import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Staring {}".format(self.name))
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("{}: {}".format(threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

t1 = myThread(1, "Thread-1", 1)
t2 = myThread(2, "Thread-2", 2)
threads.append(t1)
threads.append(t2)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Exiting Main Thread")