# -*- coding: utf-8 -*-
# concurrent_futures.py


import concurrent.futures
import time


number_list = [x for x in range(1, 11)]


def evalute_item(x):
    result_item = count(x)
    return result_item


def count(number):
    for i in range(10000000):
        i += 1
    return i * number


if __name__ == '__main__':
    start_time = time.time()
    for item in number_list:
        print(evalute_item(item))
    print("Sequential execution in {} seconds".format(time.time() - start_time))

    start_time_1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evalute_item(item)) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

    print("Thread pool execution in {} seconds".format(time.time()-start_time_1))

    start_time_2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evalute_item(item)) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

    print("Process pool execution in {} seconds".format(time.time() - start_time_2))