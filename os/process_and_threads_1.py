"""
2.2.2 The classical thread model

Now that we have seen why threads might be useful and how they can be used, lets investigate the idea a bit more
closely. The process model is based on two independent concepts: resource grouping and execution. Sometimes it is
useful to separate them; this is where threads come in. First we will look at teh classical thread model; after that
will examine the Linux thread model, which blurs the lien between processes and threads.

One way of looking at a processes is that it is a way to group related resources together. A process has an address
space containing program test and data, as well as other resources. These resources may include open files, child
processes, pending alarms, signal handlers, accounting information, and more. By putting them together in the form of
process, they can be managed more easily.

The other concept a process has is a thread of execution, usually shortened to just thread. The thread has a program
counter that keeps track of which instruction to execute next. It has registers, which hold its current working
variables. it has a stack, which contains the execution history, with one frame for each procedure called but not yet
returned from. Although a thread must execute in some process, The thread and its process are different concepts and
can be treated separately. Processes are used to group resources together; threads are the entities scheduled for
execution on the cpu.

What threads add to the process model is to allow multiple execution to take place in the same process environment, to
a large degree independent of one another. Having multiple threads running in parallel in one process is analogous to
having multiple processes running in parallel in one computer. In the former case, the threads share an address space
and other resources. In the later case, processes share physical memory, disk printers, and other resources. Because
threads have some of the properties of processes, they are sometimes called lightweight processes. The term
multithreading is also used to describe the situation of following multiple threads in the same process. As we saw in
chapter 1, some cpus have direct hardware support for multithreading and allow thread switches to happen on a
nanosecond time scale.

In Fig 2-11(a) we see three traditional processes. Each process has its own address space and a single thread of
control. In contrast, in Fig 2-11(b) we see a single process with three threads of control. Although in both cases we
have three threads, in Fig 2-11(a) each of them operates in a different address space, whereas in Fig 2-11(b) all three
of them share the same address sapce.

When a multithreaded process is run on a single cpu system, the threads take turns running. In Fig 2-1, we saw how
multiprogramming of processes works. By switching back and forth among multiple processes, the system gives the
illusion of separate sequential processes running in parallel. Multithreading works the same way, the cpu switches
rapidly back and forth amount the threads, providing the illusion that the threads are running in parallel, albeit on
a slower cpu than the real one. With three compute bound threads in a process, the threads would appear to be running
in parallel, each one on a cpu with one-third the speed of the real cpu.

Different threads in a process are not as independent as different processes. All threads have exactly the same address
space, which means that they also share the same global variables. Since every thread can access every memory address
within the process address space, one thread can read, write, or even wipe out another thread's stack. There is no
protection between threads because (1) it is impossible, and (2) it should not be necessary. Unlike different processes,
which may be from different users and which may be hostile to one another, a process is always owned by a single user,
who has presumably created multiple threads so that they can cooperate, not fight. In addition to sharing an address
space, all the threads can share the same set of open files, child processes, alarms, and signals, an so on. as show in
Fig 2-12. Thus, teh organization of Fig 2-12(a) would be used when the three process are essentially unrelated, whereas
Fig 2-12(b) would be appropriate when the three threads are actually part of the same job and are actively and closely
cooperating with each other.

Per-processes items
    address space
    global variables
    open files
    child processes
    pending alarms
    signals and signal handlers
    accounting information

per-thread  items
    program counter
    register
    stack
    state

The items in the first column are processes properties, not thread properties. For example, if one thread opens a file,
that file is visible to the other threads in the process and they can read and write it. This is logical, since the
process is the unit of resource management, not the thread. If each thread had its own address space, open files,
pending alarms, and so on, it would be a separate process. What we are tying to achieve with the thread concept is the
ability for multiple threads of execution to share a set of resource so that they can work together closely to perform
some task.

Like a traditional process (i.e., a process with only one thread), a thread can be in any one of several states:
running, blocked, ready, or terminated. A running thread currently has the cpu and is active. In contrast, a blocked
thread is waiting for some event to unblock it. For example, when a thread performs a system call to read from the
keyboard, it is blocked until input is typed. A thread can block waiting for some external event to happen or for some
other thread to unblock it. A ready thread is scheduled to run and will as soon as its turn comes up. The transitions
between thread states are the same as those between process states and are illustrated in Fig 2-2.

it is important to realize that each thread has its own stack, as illustrated in Fig 2-13. Each thread's stack contains
one frame from each procedure called but not yet returned from. This frame contains the procedure's local variables and
the return address to use when the procedure call has finished. For example, if procedure x calls procedure y and y
calls procedure z, then while z is executing, the frames for x, y, and z will all be on the stack. Each thread will
generally call different procedures and thus have a different execution history. This is why each thread needs its own
stack.

When multithreading is present, processes usually start with a single thread present. This thread has teh ability to
create new threads by calling a library procedure such as thread_create. A parameter to thread_create specifies the
name of a procedure for the new thread to run. it is not necessary (or even possible) to specify anything about the new
thread's address space, since it automatically runs in the address space of the creating thread. Sometimes threads are
hierarchical, with a parent child relationship, but often no such relationship exists, with all threads being equal.
With or without a hierarchical relationship, the creating thread is usually returned a thread identifier that names
the new thread.

When a thread has finished its work, it can exit by calling a library procedure, say, thread_exit. It then vanishes and
it no longer schedulable. In come thread thread systems, one thread can wait for a (specific) thread to exit by calling
a procedure, for example thread_join. The procedure blocks the calling thread until a (specific) thread has exited. In
this regard, thread creation and termination is very much like process creation and termination, with approximately the
same options as well.

Another common thread call is thread_yield, which allows a thread to voluntarily give up the cpu to the another thread
run. such a call is important because there is no clock interrupt to actually enforce multiprogramming as there is
with processes. Thus it is important for threads to be polite and voluntarily surrender the cpu from time to time to
give other threads a chance to run. Other calls allow one thread to wait for another thread to finish some work, for a
thread to announce that it has finished some work, and so on.

While threads are often useful, they also introduce a number
"""