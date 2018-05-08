# -*- coding utf-8 -*-
# thread_performance.py


from threading import Thread


class ThreadsObject(Thread):
    def run(self):
        function_to_run()


class NoThreadsObject(object):
    def run(self):
        function_to_run()


def non_threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(NoThreadsObject())
    for i in funcs:
        i.run()


def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(ThreadsObject())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


def function_to_run():
    pass


def show_result(func_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))


if __name__ == '__main__':
    import sys
    from timeit import Timer
    repeat = 100
    number = 1
    num_threads = [1, 2, 4, 8]
    print("Starting tests")
    for i in num_threads:
        t = Timer("non_threaded(%s)" % i, "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_result("non_threaded (%s iters" % i, best_result)
        t = Timer("threaded (%s)" % i, "from __main__ import threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_result("threaded (%s threads)" % i, best_result)
        print("Iterations complete")