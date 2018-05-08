# with_threading.py


import threading


def function(i):
    print("function called by thread {}\n".format(i))
    return


threads = []

for i in range(50):
    t = threading.Thread(target=function, args=(i, ))
    threads.append(t)
    t.start()
    t.join()
