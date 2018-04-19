from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print("Run task {} ({})...".format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task {} runs {:0.2f}".format(name, (end-start)))


if __name__ == '__main__':
    print("Parent process {}.".format(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))

    print("Waiting for all sub-processes done...")
    p.close()
    p.join()
    print("All sub processes done.")

