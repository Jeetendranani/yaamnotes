"""
Why use parallel programming?

distribute programming aims at teh possibility of sharing the processing by exchanging data through messages between
machines (nodes) of computing, which are physically separated.

Distributed programming is becoming more and more popular for many reasons; they are explored as follows:

- Fault-tolerance: As the system is decentralized, we can distribute the processing to different machines in a network,
and thus perform individual maintenance of specific machines without affecting the functioning of the system as a whole

- horizontal scalability: We can increase the capacity of processing in distributed systems in general. We can link new
equipment with no need to abort application being executed. We can say that it is cheaper and simpler compared to
vertical scalability.

- Could computing: with the reduction in hardware costs, we need the growth of this type of business where we can
obtaining huge machine parks acting in a cooperative way and running programs in a transparent way for their users.

Communicating in parallel programming

There are two forms of communication that are ore widely know when it comes to parallel programming:
1. Shared state
2. Message passing

Understanding the shared state

Illustrating this, we will make use of a real-world case, suppose you are a customer of specific bank, and this bank
has only one cashier. when you go to the bank, you must head to a queue and wait for your change. Once in the queue, you
notice that only one customer can make use of the cashier at a time, and it would be impossible for the cashier to
attend two customer simultaneously without potentially making errors. computing provides means to access data in a
controlled way, and there are several techniques, such as mutex.

Mutex can be understood as a special process variable that indicates the level of availability to access data. That is,
in our real-life example, the customer has number and at a specific moment, this number will be activated and the
cashier will be available for this customer exclusively. At the end of the process, this customer will free the cashier
for the next customer and so on.

Understanding message passing

Message passing is used when we aim to avoid data access control and synchronizing problems originating from shared
state. Message passing consists of a mechanism for message exchange in running processes. It is very commonly used
whenever we are developing programs with distributed architecture, where teh message exchanges within the network they
are placed are necessary. languages such as Erlang, for instance, use this model to implement communication in tis
parallel architecture. Once data is copied at each message exchange, it is impossible that problems occur in terms of
concurrence of access. Although memory use seems to be higher than in shared memory state, there are advantages to the
use of this model. They are as follows:
- Absence of data access concurrence
- Messages can be exchange locally (various processes) or in distributed environments
- This makes it less likely that scalability issues occur and enables interoperability of different systems.
- In general, it is easy to maintain according to programmers.

Identify parallel programming problems

Deadlock

Deadlock is a situation in which two or more workers keep indefinitely waiting for the freeing of a resource, which is
blocked by a worker of the same group for some reason. For a better understanding we will use another rea-life case.
Imagine the back those entrance as a rotating door. Customer A heads to the side, which with allow him to enter the
bank, while customer B tries to exit the bank by using the entrance side of this rotating door so that both customers
would be stuck forcing the door but heading nowhere. This situation would be hilarious in real life but tragic in
programming.

Deadlock is a phenomenon in which processes wait for a condition to free their tasks, but this condition will never
occur.

Starvation

This is the issue whose side effects are caused by unfair raking of one or more processes that take much more time to
run a task. Imagine a group of processes, A, which runs heavy tasks and has data processor priority. Now, imagine that a
process A with high priority constantly consumes the cpu, while a lower priority process B never gets the chance. Hence,
one can sya the process B is starving for CPU cycles.

Starvation is caused by badly adjusted policies of process ranking.

Race conditions

Non-determinism, if combined with lack of synchronization mechanisms, may lead to race condition issues.

Discovering Python's parallel programming tools

The python language, created by Guido Van Rossum, is a multi-paradigm, multipurpose language. It has been widely
accepted worldwide due to its powerful simplicity and easy maintenance. it is also known as the language that has
batteries included. There is a wide range of modules to make its use smoother. Within parallel programming, Python has
built-in and external modules that simplify implementation. This work is based on Python 3.x.

Threading module

multiprocessing module

parallel python module

Among some of the features, we may highlight the following:
- Automatic detection of the optimal configuration
- The fact that a number of worker processes can be changed during runtime
- Dynamic load balance
- Fault tolerance
- Auto-discovery of computational resources

Celery - A distributed task queue todo

Taking care of Python GIL

GIL is mechanism that is used in implementing standard Python, known as CPython, to avoid bytecode that are executed
simultaneously by different threads. The existence of GIL in Python is a reason for fiery discussion among users of
this language. GIL was chosen to protect the internal memory used by the CPython interpreter, which does not implement
mechanisms of synchronization for the concurrent access by threads. In any case, GIL results in a problem when we
decide to use threads, and these tends to be CPU-bound. I/O threads, for example, are out of GIL's scope. maybe the
mechanism brings more more benefits to the evolution of Python than harm to it. Evidently, we could not consider only
speed as a single argument to determine whether something is good or not.
"""