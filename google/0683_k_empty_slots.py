"""
683. K Empty Slots

There is a garden with N slots. In each slot, there is a flower. The N flowers will boom one by one in N days. In each
day, there will be exactly one flower blooming and it will be in the status of booming since them.

Given an array flowers consists of number from 1 to N. Each number in the array represents place where the flower will
open in that day.

For example, flower[i] = x means that the unique flower that booms at day i will be at position x, where i and x will
be in teh range from 1 to N.

Also given an integer k, you need to output in which day there exist two flowers in teh status of blooming, and also
the number of flowers between them is k and these flower are not booming.

if there isn't such day, output -1

Example 1:

input:
flowers: [1, 3, 2]
k: 1
Output: 2

Explanation: In the second day, the first and the third flower have become looming.

Example 2:

Input:
flowers: [1, 2, 3]
k: 1

Output: -1


Note:
    The given array will be in the range [1, 20000]


Approach #1: Insert into sorted structure

Intuition

Let's add flowers in the order they bloom. when each flower booms, we check it's neighbors to see if they can satisfy
the condition with the current flower.

Algorithm

We'll maintain active, a sorted data structure containing every flower that has currently bloomed. When we add a
flower to active, we should check it's lower and higher neighbors. If some neighbor satisfies the condition, we know the
condition occurred first on this day.
"""
from collections import deque
import bisect


def k_empty_slots(flowers, k):
    """
    Time Complexity: O(n**2), as above, except list.insert is O(n)
    Space Complexity: O(n), the size of active.
    :param flowers:
    :param k:
    :return:
    """

    active = []
    for day, flower in enumerate(flowers, 1):
        i = bisect.bisect(active, flower)
        for neighbor in active[i-(i > 0): i+1]:
            if abs(neighbor - flower) - 1 == k:
                return day
        active.insert(i, flower)
    return -1


"""
enumerate(iterable, start=0)
    Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.
    The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which
    defaults to 0) and the values obtained from iteration over iterable.
    
    >>> seasons = ['Sprint', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons), start=1)
    [(1, 'Sprint'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    
    Equivalent to:
"""


def enumerate1(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


"""
bisect - Array bisection algorithm

This module provides support for maintaining a list in sorted order without having to sort the list after each 
insertion. for long lists of items with expensive comparison operations, this can be an improvement over the more common
approach. The module is called bisect because it used a basic bisection algorithm to do its work. The source code may
be most useful as a working example of the algorithm (the boundary conditions are already right!).

The following functions are provide:

bisect.bisect_left(a, x, lo=0, hi=len(a))
    Locate the insertion point for x in a to maintain sorted order. The parameters lo and hi may be sued to specify a 
    subset of the list which should be considered; by default the entire list is used. If x is already present in a, 
    the insertion point will be before (to the left) any existing entries. The return value is suitable for use as the 
    first parameter to the list.insert() assuming that a is already sorted.
    
    The returned insertion point i partitions the array a into two halves so that all(val < x for val in a[lo:i]) for 
    the left side and all(val >= x for val in a[i:hi]) for the right side.
    
bisect.bisect_right(a, x, lo=0, hi=len(a))
bisect.bisect(a, x, lo=0, hi=len(a))
    Similar to bisect_left(), but returns an insertion point which comes after (to the right) any existing entries of x
    in a.
    
    The returned insertion point partitions the array a into two halves so that all(val <=x for val in a[lo:i] for the 
    left side and all(val > x for val in a[i: hi] for the right side.
    
bisect.insort_left(a, x, lo=0, hi=len(a))
    Inset x in a in sorted order. This is equivalent to a.insert(bisect.bisect_left(a, x, lo, hi), x) assuming that a
    is already sorted. Keep in mind that the O(log n) search is dominated by the slow O(n) insertion step.
    
bisect.insort_right(a, x, lo=0, hi=len(a))
bisect.insort(a, x, lo=0, hi=len(a))
    Similar to insort_left(), but inserting x in a after any existing entries of x.
    
See also: SortedCollection recipe that uses bisect to build a full-featured collection class with straight-forward 
search methods and support for a key-function. The keys are precomputed to save unnecessary calls to the key function
during searches.

8.5.1. Searching Sorted Lists

The above bisect() functions are useful for finding insertion points but can be tricky or awkward to use for common 
searching tasks. The following five functions show how to transform them into the standard lookups for sorted lists:
"""


def index(a, x):
    "Locate the leftmost value exactly equal to x"
    i = bisect.bisect_left(x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    'Find rightmost value less then x'
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError


def find_le(a, x):
    "Find rightmost vlaue less than or equal to x"
    i = bisect.bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError


def find_gt(a, x):
    "find leftmost value greater than x"
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    "Find leftmost item greater than or equal to x"
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


"""
8.5.2. Other Examples

The bisect() function can be useful for numeric table lookups. This example uses bisect() to look up a letter grade for
an exam score (say) based on a set of ordered numeric breakpoints: 90 and up is 'A', 80 to 89 is a 'B', and so on:
"""


def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


"""
Unlike the sorted() function, it does not make sense for the bisect() functions to have key or reversed arguments
because that would lead to an inefficient design (successive calls to bisect functions would not "remember" all of the
previous key lookups).

Instead, it is better to search a list of precomputed keys to find the index of the record in question.
"""


"""
Approach 2: Min Queue

for each contiguous block ("window") of k positions in the flower bed, we know it satisfies the condition in the problem
statement if the minimum blooming date of this window is larger than the blooming date of the left and right neighbors.

Because these windows overlap, we can calculate these minimum queries more efficiently using a sliding window structure.

Algorithm

Let days[x] = i be the time that the flower at position x blooms. For each window of k days, let's query the minimum of 
this window in (amortized) constant time using a MinQueue, a data structure built just for this task. If this minimum is
larger than it's tow neighbors, then we know this is a place where 'k empty slots' occurs, and we record this candidate 
answer.

To operate a MinQueue, the key invariant is that mins will be an increasing list of candidate answers to the query 
MinQueue.min.

For example, if our queue is [1, 2, 6, 2, 4, 8], then mins will be [1, 2, 4, 8]. As we MinQueue.popleft, mins will 
become [2, 4, 8], then after 3 more popleft's will become [4, 8], then after 1 more popleft will become [8].

As we MinQueue.append, we should maintain this invariant. We do it by popping any elements larger than the one we are 
inserting. For example, if we appended 5 to [1, 3, 6, 2, 4, 8], then mins which was [1, 2, 4, 8] becomes [1, 2, 4, 5]

Notes that we used simpler variant of MinQueue that requires every inserted element to be unique to ensure correctness.
Also, the operations are amortized constant time because every element will be inserted and removed exactly once from 
each queue.
"""


class MinQueue(deque):
    def __init__(self):
        deque.__init__(self)
        self.mins = deque()

    def append(self, x):
        deque.append(self, x)
        while self.mins and x < self.mins[-1]:
            self.mins.pop()
        self.mins.append(x)

    def popleft(self):
        x = deque.popleft(self)
        if self.mins[0] == x:
            self.mins.popleft()
        return x

    def min(self):
        return self.mins[0]


class Solution(object):
    @staticmethod
    def k_empty_slots1(self, flowers, k):
        """
        Tome Complexity: O(n), where n is the length of flowers. In enumerating through the O(n) outer loop, we do
        constant work as MinQueue.popleft and MinQueue.min operation are (amortized) constant time.
        Space Complexity: O(n), the size of our window.
        :param self:
        :param flowers:
        :param k:
        :return:
        """

        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position-1] = day

        window = MinQueue()
        ans = len(days)

        for i, day in enumerate(days):
            window.append(day)
            if k <= i < len(days) - 1:
                window.popleft()
                if k == 0 or days[i-k] < window.min() > days[i+1]:
                    ans = min(ans, max(days[i-k], days[i+1]))

        return ans if ans <= len(days) else -1


"""
Approach 3: Sliding Window

As in approach 2, we have days[x] = i for the time that the flower at position x blooms. We wanted to find candidate 
intervals [left, right] where days[left] days[right] are the two smallest values in days[left], days[left+1], ... 
days[right], and right - left = k + 1.

Notice that these candidate intervals connot intersect: for example, if the candidate intervals are [left1, right1] and 
[left2, right2] with left1 < left2 < right1 < right2, then for the first interval to be a candidate, days[left2] > 
days[right1]; and for the second interval to be a candidate, days[right1] > days[left2], a contradiction.

That means whenever whether some interval can be a candidate and it fails first at i, indices j < i can't be the start 
of a candidate interval. This motivates a sliding window approach.

Algorithm

As in approach 2, we construct days.

Then, for each interval [left, right] (starting with the first available one), we'll check whether it is a candidate: 
whether days[i] > days[left] and days[i] > days[right] for left < i < right.

If we fail, then we've found some new minimum days[i] and we should check the new interval [i, i+k+1]. If we succeed, 
then it's a candidate answer, and we'll check the new interval [right, right+k+1].
"""


def k_empty_slots3(flowers, k):

    """
    Time and Space Complexity: O(n)
    :param flowers:
    :param k:
    :return:
    """
    days = [0] * len(flowers)
    for day, position in enumerate(flowers, 1):
        days[position-1] = day

    ans = float('inf')
    left, right = 0, k+1
    while right < len(days):
        for i in range(left+1, right):
            if days[i] < days[left] or days[i] < days[right]:
                left, right = i, i+k+1
                break
        else:
            ans = min(ans, max(days[left], days[right]))
            left, right = right, right+k+1

    return ans if ans < float('inf') else -1


"""
In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match 
one of the arguments accepted by the function (e.g. actor is not a valid argument for the parrot function), and their
order is not important. This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too). No argument
may receive a value more than once. Here's an example that fails due to this restriction.

When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types - dict) 
containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a 
formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional 
arguments beyond the formal parameter list. (*name must occur before **name.) For example, if we define a function like
this:
"""


def cheeseshop(kind, *arguments, **kwwords):
    print("-- do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(kwwords.keys())
    for kw in keys:
        print(kw, ":", kwwords[kw])


"""
Note that the list of keyword argument names is creatd by sorting the result of hte keywords dictionary's keys() method
before printing its contents; if this is not done, the order in which the arguments are printed is undefined.

4.7.3. Arbitrary Argument Lists

Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of 
arguments. This arguments will be wrapped up in a tuple (see Tuples and Sequences). Before the variable number of 
arguments, zero or more normal arguments may occur.
"""


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


"""
Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining 
input arguments that are passed to the function. Any formal parameters which occur after the *args parameter are 
'keyword-only' arguments, meaning that they can only be used as keywords rather than positional arguments.

4.7.4. Unpacking Argument Lists

The reverse situation occurs when the arguments are already in a list or tuple but need to unpacked for a function call 
requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop 
arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out 
of a list or tuple:

>>> list(range(3, 6))
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))
[3, 4, 5]

In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

4.7.5. Lambda Expressions

Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments:
lambda a, b: a+b. Lambda function can be used wherever function objects are required. They are syntactically restricted 
to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested 
function definitions, lambda functions can reference variables from the containing scope:

The above example use a lambda expression to return a function. Another use is to pass a small function as an 
argument:

4.7.6. Documentation Strings

Here are some conventions about the content and formatting of documentation strings.

The first line should always be a short, concise summary of the object's purpose. for brevity, it should not explicitly
state the object's name or type, since these are available by other means (except if the name happens to be a verb 
describing a function's operation). This line should begin with a capital letter and end with a period.

If there are more lines in the documentation string, the second line should be blank, visually separating the summary 
for the rest of the rest of hte description. The following lines should be one or more paragraphs describing the 
object's calling conventions, it side effects, etc.

The Python parser does not strip indentation from multi-line string literals in Python, so tools that process 
documentation have to strip indentation if desired. This is doing using the following convention. The first non-blank 
line after the first line of the string determines the amount of indentation for the entire documentation string. (We
can't use the first line since it is generally adjacent to the string's opening quotes so its indentation is not 
apparent in the string literal.) Whitespace 'equivalent' to this indentation is then stripped from the start of all 
lines of the string. Liens that are indented less should not occur, but if they occur all their leading whitespace
should be stripped. Equivalence of whitespace should be tested after expansion of tabs (to 8 spaces, normally).

Here is an example of a multi-line docstring;

"""


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything
    """
    pass


"""
4.7.7. Function Annotations

Function annotations are completely optional metadata information about the types used by user-defined functions (see
PEP 484 for more information).

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other 
part of the function. Parameter annotations are defined by a colon after the parameter name, followed by an expression 
evaluating to the annotation. Return annotations are defined by a literal ->, follow by an expression, between the 
parameter list and the colon denoting the end of the def statement. The following example has a positional argument, a
keyword argument, and the return value annotated:

4.8. Intermezzo: Coding Style

Now that you are about to write longer, more complex pieces fo Python, it is a good time to talk about coding style.
Most languages can be written (or more concise, formatted) in different styles; some are more readable than others. 
Making it easy for others to read your code is always a good idea, and adopting a nice coding style helps tremendously
for that.

For Python, PEP 8 has emerged as the style guide that most projects adhere to; it promotes a very readable and 
eye-pleasing coding style. Every Python developer should read it at some point; here are the most important points
extracted for you:

    - Use 4-space indentation, and no tabs.
    4 space are good compromise between small indentation (allows greater nested depth) and large indentation (easier 
    to read). Tabs introduce confusion, and are best left out.
    
    - Wrap lines so that they don't exceed 79 characters.
    This helps users with small displays and makes it possible to have several code files side-by-side on large 
    displays.
    
    - Use blank lines to separate functions and classes, and larger blocks of code inside functions.
    
    - When possible, put comments on a line of their own.
    
    - Use docstrings.
    
    - Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
    
    - Name your classes and functions consistently; the convention is to use CamelCase for classes and 
    lower_case_with_underscores for functions and methods. Always use self as hte name for the first method argument 
    (see A First Look at Classes for more on classes and methods).
    
    - Don't use fancy encodings if your code is meant to be used in international environments. Python's default, UTF-8,
    or even plain ASCII work best in any case.
    
    - Likewise, don't use mon_ASCII characters in identifiers if there is only the slightest chance people seaking a 
    different language will read or maintain the code.
    
Footnotes
    Actually, call by object reference would be a better description, since if a mutable object is passed, the caller 
    will see any changes the callee makes to it (items inserted into a list).
"""