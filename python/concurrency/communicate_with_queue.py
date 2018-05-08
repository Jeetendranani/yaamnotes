# -*- coding: utf-8 -*-
# communicate_with_queue.py


import multiprocessing
import random
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print("Process Producer : item {} appended to queue by {}".format(item, self.name))
            time.sleep(1)
            print("The size of queue is {}".format(self.queue))


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("the queue is empty")
                break

            else:
                time.sleep(2)
                item = self.queue.get()
                print("Process Consumer : item {} popped from queue by {}".format(item, self.name))
                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()