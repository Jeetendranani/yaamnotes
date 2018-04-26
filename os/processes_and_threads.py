"""
2.1.2 Process creation

Operating system need some way to create processes. In very simple systems, or in systems designed for running only a
single application (e.g. the controller in a microwave oven), it may be possible to have all the processes that will
ever be needed be present when teh system comes up. In general purpose systems, however, some whay is needed to create
and terminate processes as needed during operation. We will now look at some of the issues.

Four principle events cause processes to be created.
    1. System initialization
    2. Execution of a process-creation system call by a running process
    3. A user request to create a new process
    4. Initiation of batch job

In Unix, there is only one system call to create a new process: fork. This call creates an exact clone of teh calling
process. After the fork, the two processes, the parent and teh child, have the same memory image, the same environment
strings, and the same open files.

2.1.3 process termination

sooner or later the new process will terminate, usually due to one of the following conditions:
    1. normal exit
    2. error exit
    3. fatal error
    4. killed by another process

2.1.6 Implementation of processes

to implement the process model, the operating system maintains a table (an array of structures), called the process
table, with one entry per process. (some authors call these entries process control blocks). This entry contains
important information about the process state, including tis program counter, stack pointer, memory allocation, the
status of its open files, its accounting and scheduling information, and everything else about the process that must be
saved when the process is switched from running to ready or blocked state so that it can be restarted later as if it had
ever been stopped.

2.2 Threads todo

2.3 interpocesses communication todo

2.4 scheduling todo

2.5. classic ipc problems todo

2.6 research on processes and threads todo
"""