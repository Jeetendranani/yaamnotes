"""
621. Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters
represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For
each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n
intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals teh CPU will take to finish all the given tasks.

Example 1:

Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
    1. The number of task is the range [1, 10000].
    2. The integer n is the range [0, 100].

Thought Process:
1. Array is not sorted, could i t be sorted?
2. Task is a finite set, 26 maximum
3. It is about extreme value (min value in this case), can Dynamic Programming (DP) be applied?
4. DP seems cannot be applied here, it is very hard to come up with a mathematical induction function, even though
there is a solution by coming up with a math formula, but it is very hard to come up with this in a real interview
session.
5. Can we do any binary search hear, nope.
6. Hmm... it seems maybe we can be greedy here, doing it in a round robin way. Schedule the largest job first, then
2nd largest job, then 3rd largest job until the interval is met. Note, we have to always apply the largest job as soon
as possible, for example, if we have a test case [ A, A, A, A, B, C, D, E] and interval is 2. if we are doing round
robin, it would be A, B, C, D, E, idle, idle, A, idle, idle, A, idle, idle, A -> 15 cycle, where we should really apply
A as soon as possible, so it becomes A, B, C, A, D, E, A, idle, idle, A, idle, idle, A -> 13 cycle.

Solutions 1:
Sort after every iteration
Given the greedy sort, we want to always apply the largest job first, so we should sort the jobs first (job name does
not matter), after meeting the interval requirement, sort the array again and repeat by applying the largest job fist,
then the 2nd largest etc.
"""
import threading
import queue
from queue import PriorityQueue


class Solution:
    def __ini__(self):
        self.ans = None

    @staticmethod
    def least_interval(self, tasks, n):

        """
        Time Complexity O(T), T is the number of iterations, given sort on fixed array (26)
        Space Complexity O(1), constant array size

        :param self:
        :param tasks: List[str], The number of tasks is in the range [1, 10000]
        :param n: int The nuber of tasks is in the range [0, 100]
        :return:
        """

        task_count_list = [0] * 26
        # task name does not matter, just cast it to integer
        for task in tasks:
            task_count_list[ord(task) - ord('A')] += 1

        task_count_list.sort()

        total_cpu_cycle = 0

        while task_count_list[-1] > 0:
            i = 0
            while i < n:
                if not task_count_list[-1]:
                    break
                # always come from the largest element, and
                if i < 26 and task_count_list[25 - i]:
                    task_count_list[25 - i] -= 1
                i += 1
                total_cpu_cycle += 1
            task_count_list.sort()
        return total_cpu_cycle

    """
    Solution 2:
    Use priority queue (max help)
    Instead of sorting after every iteration we can use the max heap to always pop out the largest element, and 
    instead of sort O(nlgn) on every iteration, it will just be O(lgn) to heaptify, even though N is fixed 26 on size.
    """

    @staticmethod
    def least_interval2(self, tasks, n):
        """
        Time Complexity: O(T) how many iterations we do
        Space Complexity: O(1) fixed heap size (26)
        :param self:
        :param task:
        :param n:
        :return:
        """

        task_count_list = [0] * 26
        for task in tasks:
            task_count_list[ord(task) - ord('A')] += 1

        pq = PriorityQueue() # use it as max heap by inverting the number

        for item_count in task_count_list:
            if item_count:
                # gosh, only python can have those hacks, a min heap (default) inverted to use as max heap
                pq.put(-item_count)

        total_cpu_cycle = 0
        while not pq.empty():
            i = 0
            temp = []
            while i <= n:
                if not pq.empty():
                    if -pq.queue[0] > 1:
                        temp.append(-pq.get() - 1) # save it to later insert back to teh priority queue
                    else:
                        # this pops the element out
                        pq.get()

                total_cpu_cycle += 1
                if pq.empty() and not temp:
                    break

                i += 1

            for item_count in temp:
                pq.put(-item_count)

        return total_cpu_cycle

    """
    Solution 3:
    It is a math calculation. This problem has 2 different case in general:
    1. No idle cycle. The result should be len(tasks)
    2. With idles. This means we have some tasks too many, so it lasts to the end. So we need (M - 1) * (n + 1) + Mct.
    So the solution is return the max(len(tasks), (M - 1) * (n + 1) + Mct).
    """

    @staticmethod
    def least_interval3(self, tasks, n):
        import collections
        """
        Time Complexity: O(1), need to count the tasks
        Space complexity: O(1)
        :param self:
        :param tasks:
        :param n:
        :return:
        """
        task_counts = collections.Counter(tasks).values()
        max_repeat_times = max(task_counts)
        max_repeat_times_counter = task_counts.count(max_repeat_times)
        return max(len(tasks), (max_repeat_times-1) * (n + 1) + max_repeat_times_counter)


"""
Knowledge Summary:
1. Greedy algorithm:
A greedy algorithm is an algorithmic paradigm that follows teh problem solving heuristic of making the locally optimal 
choice at each stage with the hope of finding a global optimum. In many leetcode, a greedy strategy does not in general
produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a
global optimal solution in a reasonable time.
For example, a greedy strategy for the traveling salesman problem (which is of a high computational complexity) is the 
following heuristic: "At each stage visit an unvisited city nearest to the current city" This heuristic need not find a
best solution, but terminates in a reasonable number of steps; finding an optimal solution typically requires 
unreasonably many steps. In mathematical optimization. greedy algorithms solve combinatorial leetcode having the 
properties of matroids.

Specifics:
In general, greedy algorithms have five components:
1. A candidate set, from which a solution is created
2. A selection function, which choose the best candidate to be added to teh solution
3. A feasibility function, that is used to determine if a candidate can be used to contribute to solution
4. An objective function, which assigns a value to a solution, or a partial solution, and 
5. A solution function, which will indicate when we have discovered a complete solution.
Greedy algorithms produce good solutions on some mathematical leetcode, but not on others. Most leetcode for which they
work will have two properties.

Greedy choice property:
We can make whatever choice seems best at the moment and them solve the sub-leetcode that arise later. The choice made 
by a greedy algorithm may depend on choices made so far, but not on future choices or all the solutions to the 
sub-problem. it iteratively makes one greedy choice after another, reducing each given problem into a smaller one. In 
other words, a greedy algorithm never reconsiders its choices. This the main difference from dynamic programming, which
is exhaustive and is guaranteed to find the solution.
After every stage, dynamic programming makes decisions based on all the decisions made in the previous stage, and may 
reconsider the previous stage's algorithmic path to solution.

Optimal substructure:
"A problem exhibits optimal substructure if an optimal solution to the problem contains optimal solutions to the 
sub-leetcode.

Cases of failure:
For many other leetcode, greedy algorithems fail to produce the optimal solution, and may even produce unique worst
possible solution. One example is the traveling salesman problem mentioned above: for each number of cities, there is 
an assignment of distances between the cities for which the nearest neighbor heuristic produces the unique worst 
possible tour.

Types:
Greedy algorithms can be characterized as being 'short sighted', and also as 'non-recoverable'. They are ideal only for 
leetcode which have 'optimal substructure'. Despite this, for many simple problem (e.g. giving change), the best suited 
algorithms are greedy algorithms. It is important , however, to note that the greedy algorithm can be used as selection 
algorithm to prioritize options within a search, or branch-and-bound algorithm. There are a few variations to the greedy
algorithm:
- Pure greedy algorithms
- Orthogonal greedy algorithms
- Relaxed greedy algorithms

Applications:
Greedy algorithms mostly (but not always) fail to find the globally optimal solution, because they usually do not 
operate exhaustively on all the data. They can make commitments to certain choices too early which prevent them from 
finding the best overall solution later. For example, all known greedy coloring algorithms for the graph coloring 
problem and all other NP-complete leetcode do not consistently find optimum solutions. Nevertheless, they are useful 
because they ar quick to think up and often give good approximations to the optimum.
If a greedy algorithm can be proven to yield the global optimum for a given problem class, it typically becomes the 
method of choice because it is faster than other optimization methods like dynamic programming. Examples of such greedy
algorithms are Kruskal's algorithm and Prim's algorithm for finding the minimum spanning trees, and the algorithm for 
finding optimum Huffman trees.
The theory of matroids, and the more general theory of geedoids, provide whole classes of such algorithms.
Greedy algorithms appear in network routing as well, using greedy routing, a message is forwarded to the neighboring
node which is 'closest' to the destination. The notion of node's location ( and hence 'closeness') may be determined
by its physical location, as in geographic routing used by ad hoc networks. location may also be an entirely artificial
construct as in small world routing and distributed hash table.

Examples:
- The activity selection problem is characteristic to this class of leetcode, where the goal is to pick the maximum 
number of activities that to do not clash with each other.
- In the Macintosh computer game Crystal Quest the objective is to collect crystals, in a fashion similar to the 
travelling salesman problem. The game has a demo mode, where the game uses a greedy algorithm to go to every crystal. 
The artificial intelligence does not account for obstacles, so the demo more often ends quickly.
- A greedy algorithm finds the optimal solution to Malfatti's problem of finding three disjoint circles within a given 
triangle that maximize the total area of the circles; it is conjectured that the same greedy algorithm is optimal for 
any number of circles.
- A greedy algorithm is used to construct a Huffman tree during Huffman coding where it finds an option solution.
- In decision tree learning, greedy algorithms are commonly used, however they are not guaranteed to find the optimal 
solution.

2. PriorityQueue:
queue - A synchronized queue class
The queue module implements multi-producer, multi-consumer queues. it is especially useful in threaded programming when
information must be exchanged safely between multiple threads. The Queue class in this module implements all required 
locking semantics. It depends on teh availability of thread support in Python; see threading module.
The module implemented three types of queue, which differ only in the order in which the entries are retrieved. In a 
FIFO queue, the first tasks added are the first retrieved. In a LIFO queue, the most recently added entry is the first 
retrieved (operating like a stack). With a priority queue, the entries are kept sorted (using the heapq module) and the 
the lowest valued entry is retrieved first.
Internally, the module uses locks to temporarily block competing threads; however, it is not designed to handle 
re-entrancy within a thread.
The queue module defines the following classes and exceptions:

class queue.Queue(maxsize = 0)
constructor for a FIFO queue. maxsize is an integer that sets the upper-bound limit on the number of items that can be 
placed in the queue. Insertion will blocked once this size has been reached, until queue items are consumed. If maxsize 
is less thtan or equal to zero, the queue size is infinite.

class queue.LifoQueue(maxsize = 0)
constructor for LIFO queue, maxsize is an integer that sets the upper-bound limit on the number of itms that can be 
placed in teh queue. Insertion will blocked once this size has been reached, until queue items are consumed. If maxsize
is less than or equal to zero, the queue size is infinite.

class queue.PriorityQueue(maxsize = 0)
constructor for a priority queue. maxsize is an integer that sets the upper-bound limit on the number of items that can 
be placed in the queue. Insertion will be blocked once this size has been reached, until queue items are consumed. if 
maxsize is less than or equal to zero, the queue size i infinite.
The lowest value entries are retrieved first (the lowest valued entry is the one returned by sorted(list9entries))[0]). 
A typical pttern for entries is a tuple in the form: (priority_number, data).

Exception queue.Empty
Exception raised when non-blocking get() (or get_nowait()) is called on a Queue object which is empty.

Exception queue.Full
Exception raised when non-locking put() (or put_nowait()) is called on a Queue object which is full.

Queue Objects
Queue objects(Queue, lifoQueue, or PriorityQueue) provide the public methods described below.

Queue.qsize()
Return the approximate size of the queue. Note, qsize() > 0 doesn't guarantee that a subsequent get() will not block, 
nor will qsize() < maxsize guarantee that put() will not block.

Queue.empty()
Return True if the queue is empty, False otherwise. If empty() returns True it doesn't guarantee that subsequent call 
to put() will not block. Similarly, if empty() returns False it doesn't guarantee that a subsequent call to get() will 
not block.

Queue.full()
Return True if the queue is full, False otherwise. if full() returns True it doesn't guarantee that a subsequent call 
to get() will not block. Similarly, if full() return False it doesn't guarantee that a subsequent call to put() will not
block.

Queue.put(item, lock=True, timeout=None)
Put item into the queue. If optional args block is true and timeout is None (the default), block if necessary until a 
free slot is available. If timeout is positive number, it blocks at most timeout seconds and raises the Full exception 
if no free slot was available within that time. Otherwise (block is false), put an item on the queue if a free slot is
immediately available, else raise the Full exception (timeout is ignored in that case).

Queue.put_nowait(item)
Equivalent to put(item, False).

Queue.get(block=True, timeout=None)
Remove and return an item fro the queue. If optional args block is true and timeout is None (the default), block if 
necessary until an item is available. If timeout is a positive number, it blocks at most timeout seconds and raises the 
Empty exception if no item was available within that time. Otherwise (block is false), return an item if one is 
immediately available, else raise the Empty exception (timeout is igmored in that case).

Queue.get_nowait()
Equivalent to get(False).

Queue.task_done()
indicate that a formerly enqueued task is complete. Used by queue consumer threads. For each get() used to fetch a task, 
a subsequent call to task_done() tells the queue that the processing on the task is complete.

Queue.join()
Blocks until all items in the queue have been gotten and processed.
The count of unfinished tasks goes up whenever an item is added to the queue. the count goes down whenever a consumer 
thread calls task_done() to indicate that item was retrieved and all work on it is complete. When the count of 
unfinished tasks drops to zero, join() unblocks.
"""

# Example of how to wait for enqueued tasks to be completed:

num_worker_threads = 10


def do_work():
    pass


def source():
    pass


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()


q = queue.Queue()

threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for item in source():
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()


"""
Built-in Functions:
The python interpreter hs a number of functions and types built into it that are always available. they are listed here 
in alphabetical order.
abs()
all()
any()
ascii()
bin()
bool()
byterarray()
bytes()
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
exec()
filter()
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
print()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()
__import__()

abs(x)

all(iterable)
Return True if all elments of iterable are true (of if the iterable is empty). Equivalent to:
"""


def all1(iterable):
    for element in iterable:
        if not element:
            return False
    return True


"""
any(iterable)
Return True if any element of the iterable is true. If the iterable is empty return False. Equivalent to:
"""


def any1(iterable):
    for element in iterable:
        if element:
            return True
    return False


"""
ascii(object)
As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters in 
the string returned by repr() using \x, \u or \U escapes. This generates a string similar to that returned by repr()
in Python 2.

bin(x)
Convert an integer number to a binary string prefixed with "0b". The result is a valid Python expression. if x is not 
a Python int object, it has to define an __index__() method that returns an integer. Some examples: 
If prefix '0b' is desired or not, you can use either of the following ways.
>>> format(14, '#b'), format(14, 'b')
or 
>>> f'{14:#b}', f'{14:b}'

class bool([x])
Return a Boolean value, i.e. one of True or False. X is converted using the standard truth testing procedure. if x is 
false or omitted, this return False; otherwise it returns True. The bool class is a subclass of int (see Numeric Types 
- int, float, complex). It can't be subclassed further. Its only instance are False and True (see Boolean Values).

class bytearray()
Return a new array of bytes. the bytearray class is a nutable equence of integers in the range 0 <= x < 256. It has 
most of the usual methods of mutable sequences, described in Mutable Sequences Types. as well as most methods that the 
bytes type has, see Bytes and Bytearray Operations.

The optional source parameter can be used to initialize the array in a few different ways:
- if it is string, you must also give the encoding (and optionally, errors) parameters; bytearray() then converts the 
string to bytes using str.encode().
- If it is an integer, the array will have that size and will be initialized with null bytes.
- If it is an object conforming to the buffer interface, a read-only buffer of the object will be userd to initialize 
the bytes array.
- If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial 
content of the array.
Without an argument, an array of size 0 is created.
"""