import os
from multiprocessing import Process


print('Process ({}) start...'.format(os.getpid()))

pid = os.fork()

if pid == 0:
    print('I am child process ({}) and my parent is {}'.format(os.getpid(), os.getppid()))
else:
    print("I ({}) just created a child process ({}).".format(os.getpid(), pid))


def fun_proc(name):
    print("Ran child process {} ({})...".format(name, os.getpid()))


if __name__ == '__main__':
    print("Parent process {}.".format(os.getpid()))
    p = Process(target=fun_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
