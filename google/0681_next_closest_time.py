"""
681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closet time by reusing the current digits. There is no
limit on how may times a digit can be reused.

You any assume the given input string is always valid. For example, "01:34", "12:09" are valid. "1:34", "12:0" are all
invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later. it is not
19:33, because this occurs 23 hours and 59 minutes later.

Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assuming that the returned time
is next day's time since it is smaller than the input time numerically.

Approach 1: Simulation

Simulate the clock going forward by one minute. Each time it mores forward, if all the digits are allowed, then return
the current time.

The natural way to represent time is an integer t in the range 0 <= t < 24 * 60. Then the hours are t / 60, the minutes
are t % 60, and each digit of the hours and minutes can be found by hours // 10, hours % 10. etc.
"""
import itertools



class Solution(object):
    def next_closest_time(self, time):
        """
        Time complexity: O(1). We will try up to 24 * 60 possible times until w find the correct time.
        Space complexity: O(1).
        :param time:
        :return:
        """
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                   for block in divmod(cur, 60)
                   for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))


"""
Approach 2: Build From Allowed Digits

Intuition and Algorithm

We have up to 4 different allowed digits, which naively gives us 4 * 4 * 4 * 4 possible times. For each possible time. 
Let's check that it can be displayed on a clock: ie., hours < 24 and mins < 60. The best possible time != start is the 
one with the smallest cand_elapsed = (time - start) % (24 * 60), as this represents the time that has elapsed since 
start, and where the modulo operation is taken to be always non-negative.

For example, if we have start = 720 (ie, noon), then times like 12:05 = 725 means that (725 - 720) % (24 * 60) = 5 
seconds have elapsed; while time like 00:10 = 10 means that (10 - 720) % (24 * 60) = -710 % (24 * 60) = 730 seconds 
have elapsed.

Also we should make sure to handle cand_elapsed carefully. When our current candidate time cur is equal to the given 
starting time, then cand_elapsed will be 0 and we should handle this case appropriately.
"""


class Solution1(object):

    def next_colsest_time1(self, time):
        """
        time complexity: O(1)
        space comlexity: O(1)
        :param time:
        :return:
        """

        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ":"}
        for h1, h2, m1, m2 in itertools.product(allowed, repeat=4):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cand_elapased = (cur - start) % (24 * 60)
                if 0 < cand_elapased < elapsed:
                    ans = cur
                    elapsed = cand_elapased
        return "{:02d}:{:02d}".format(*divmod(ans, 60))


"""
5. Data structures

This chapter describes something you already learned in more detail, and add some new things as well.

5.1. More on Lists

The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
    Ad an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
    Extend the list by appending all the elements from the iterable. Equivalent to a[len(a):] = iterable.
    
list.insert(i, x)
    Insert an item at a given position. The first argument is the index of the element before which to insert, so 
    a.insert(0, x) insert at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
    
list.remove(x)
    Remove the first item fom the list whose value is x. It is an error if there is no such item.
    
list.pop([i])
    Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and 
    returns the last item in the list. ( The square brackets around the i in the method signature denote that the 
    parameter is optional, not that you should type square brackets at the position. You will see this notation
    frequently in the Python Library Reference.)
    
list.clear()
    Remove all items from the list. Equivalent to del a[:].
    
list.index(x[, start[, end]])
    Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.
    
    The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to 
    a particular sub-sequence of the list. The returned index is computed relative to the beginning of the full 
    sequence rather the start argument.
    
list.count(x)
    Return the number of times x in the list.
    
list.sort(key=None, reverse=False)
    Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their 
    explanation).
    
list.reverse()
    Reverse the element of the list in place.
    
list.copy()
    Return a shallow copy of the list. Equivalent to a[:]

You might have noticed that methods like insert, remove, or sort that only modify the list have no return value printed
- they return the default None. This is  design principle for all mutable data structure in Python.

5.1.1. using List as Stacks

The list methods make it very easy to use a list as stack, where the last element added is the first element retrieved
("last-in, first-out"). To add an item to the top of the stack, use append(). To retrieve an item from the top of the 
stack, use pop() without an explicit index. For example:

5.1.2. Using lists as queues

It is also possible to use a list as a queue, where the first element added is the first element retrieved ("first-in, 
first-out"); however, lists are not efficient for this purpose. While appends and pops from teh end of listed are fast,
doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by 
one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For 
example:

5.1.3. List comprehensions

List comprehensions provide a concise wy to create lists. Common applications are to make new lists where each element
is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of 
those elements that satisfy certain condition.

For example, assume we want to create a list of squares, like:

Note that this creates (or overwrites) a variable named x that still exists after the loop completes. We can calculate 
list of squares without any side effects using:

squares = list(map(lambda x: x ** 2, range(10)))

or equivalently:

squares = [x**2 for x in range(10)]

which is more concise and readable.

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if
clauses. The result will be a new list resulting from evaluating the expressions in the context of the for and if 
clauses which follow it. for example, this listcomp combines the elements of two list from they are not equal:

>>> [(x, y) for x in [1, 2, 3] for y in [3, 1, 4]

and it's equivalent to: 
"""

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

"""
Note how the order of the for and if statements is the same in both this snippets.

If the expression is a tuple (e,g. the (x, y) in the previous example), it must be parenthesized.

List comprehensions can contain complex expressions and nested functions.

5.1.4. Nested list comprehensions

The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

Consider the following example of 3 x 4 matrix implemented as a slit of 3 lists of length 4:

>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12]
... ]

The following list comprehension will transpose rows and columns:

>>> [[row[i] for row in matrix] for i in range(4)]

As we saw in the previous section, the nested listcomp is evaluated in teh context of the for that follows it, so this 
example is equivalent to:
"""
matrix = []

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])


"""
which, in turn, is the same as:
"""

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


"""
If the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great
job for this use case:
"""


list(zip(matrix))


"""
See Unpacking Argument Lists for details on the asterisk in this line.

5.2. The del statement

There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from
the pop() method which returns a value. The del statement can also used to remove slices from a list or clear the entire
list (which we did earlier by assignment of an empty list to the slice). For example:

del can also be used to delete entire variables:

Referencing the name a hereafter is an error (at least until another values is assigned to it). We'll find other uses 
for del later.

5.3. Tuples and Sequences

We saw that lists and strings have amny common properties, such as indexing and slicing operations. they are two 
examples of sequence data types (see Sequence Types - list, tuple, range). Since Python is an evolving language, other
sequence data types may be added. there is aldo another standard sequence data type: the tuple.

A tuple consists of a number of values separated by commas, of instance:

As you see, on output tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly; they 
may be input with or without surrounding parentheses, although often parentheses are necessary anyway (if the tuple is 
part of larger expression). It is not possible to assign the individual items of a tuple, however it is possible to 
create tuples which contains mutable objects, such as lists.

Though tuples may seem similar to lists, they are often used in different situations and for different purpose. Tuples
are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in 
this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements
are usually homogeneous and are accessed by iterating over the list.

A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate
these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following 
a value with a, comma (it is not sufficient to enclose a single value in parentheses). ugly, but effective. For example:

The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321, and 'hello!' are 
packed together in a tuple. The reverse operation is also possible:

>>> x, y, z = t

This is called, appropriately enough, sequence unpacking and works for any sequence on the right-hand side. Sequence 
unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the 
sequence. Note that multiple assignment is really just a combination of tuple packing and sequence unpakcing.

5.4. Sets

Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses 
include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like
union, intersection, difference and symmetric difference.

Curly braces or the set() function can be used to created sets. Note: to create an empty set you have to use set(), not 
{}; the later creates empty dictionary, a data structure that we discuss in the next sectioin.

Here is a brief demonstration:

Similarly to list comprehensions, set comprehensions are also supported:

5.5. Dictionaries

Another useful data type built into Python is the dictionary (using Mapping Types - dict). Dictionaries are found in 
other languages as "associative memories" or "associative arrays". Unlike sequences, which ar indexed by a range of 
numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. 
Tuples can be used as keys if they contains only strings, numbers, or tuples; if a tuple contains any mutable object
either directly or indirectly, it cannot be sued as a key. You can't use lists as keys, since lists can be modified in
place using index assignments, slice assignments, or methods like append() and extend().

It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are 
unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of 
key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionary are 
written on output.

The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also
possible to delete a key:value pair with del. If you store suing a key that is already in use, the old value associated
with that key is forgotten. It is an error to extract a value using a non-existing key.

Performing list(d.keys()) on a dictionary returns a list of all the keys used in the dictionary, in arbitrary order (if 
you want it sorted, just use sorted(d.keys() instead). To check whether a single key is in the dictionary, use the in
keyword.

Here is a small example using a dictionary;

The dict() constructor builds dictionaries directly from sequences of key-value pairs:

In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

When the keys are simple strings, it is sometimes easier to specify pairs suing keyword arguments.

5.6. Looping Techniques

When loop through dictionaries, the key and corresponding value can be retrieved at the same time using the items() 
method.

When looping through a sequence, the position index and corresponding value can be retrieved at teh same time using the 
enumerate() function.

To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

To loop over a sequence in reverse, first specify hte sequence in a forward direction and then call the reversed() 
function.

To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the 
source unaltered

it is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to 
create a new list instead.

5.7. More on conditions

The conditions used in while and if statement can contain any operators, not just comparisons.

The comparison operators in and not in check whether a value occurs (does not occur) in a sequence. The operators is 
and is not  compare whether the object are really the same object; this only matters for mutable objects like lists.
All comparisons have the same priority, which is lower then that all numerical operators.

Comparisons can be chained. For example, a < b == C tests whether a is less than b and moreover b equals c.

Comparisons may be combined using the Boolean operators and and or, and the outcome of a comparison (or of any other
Boolean expression) may be negated with not. These have lower priorities than comparison operators; between them, not
has the highest priority and or the lowest, so that A and not B or C is equivalent (A and (not B)) or C. As always, 
parentheses can be sued to express teh desired composition.

The Boolean operators and or or are so-called short-circuit operators: their arguments re evaluated from left to right,
and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false, A and B and
C doesn't not evaluate the expression C. When used as general value and not as Boolean, the return value of a 
short-circuit operator is the last evaluated argument.

It is possible to assign the result of comparison or other Boolean expression to a variable. For example,

Note that in Python, unlike C, assignment cannot occur inside expressions, C programmers may grumble about this, but it
avoids a common class of leetcode encountered in C programs: typing = in an expression when == was intended.

5.8. Comparing Sequences and other types

Sequence objects may be compared to other objects with the same sequence type. The comparison uses lexicographical 
ordering: first two items re compared, an differ this determines the outcome of the comparison; if they are equal, the
next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves
of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare 
equal, the sequence are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence 
is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual
characters. Some examples of comparisons between sequences of hte same type:

Note that comparing object of different types with < or > is legal provide that the object have appropriate comparison
methods. for example, mixed numeric types are compared according to their numeric value, so 0 equals 0,0, etc, 
Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a TypeError exception.

6. Modules

If you quit from teh Python interpreter and enter it again, the definitions you have made (function and variables) are
lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the
input for the interpreter and running it with that file as input instead. This is known as creating a script. As your
program gets longer, you may want to split it into several files for easier maintenance. You may also wan to use a handy
function that you've written in several programs without copying its definition into each program.

To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of
the interpreter. Such a file is called module; definitions from a module can  be imported into other modules or into 
the main module (the collection of variables that you have access to in a script executed at the top level and in 
calculator mode).

A module is a file containing Python definitions an statements. The file name with the suffix .py appended. Within a 
module, the module's name (as a string) is available as value of the global variable __name__. For instance, use your 
favorite text editor to create a file called fibo.py in current directory with the following contents:

Now enter teh Python interpreter and imported this module with the following command:

This does not enter the names of functions defined in fibo directly in the current symbol table; it only enters the 
module name fibo there. Using the module name you can access the functions:

If you intend to use a function often you can assign it to local name:

6.1. More on modules

A module can contain executable statements as well as function definitions. These statements are intended to initialized
the module. They are executed only the first time the module name is encountered in an import statement. (They are also 
run if the file is executed as a script.)

Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the 
module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes 
with a user's global variables. On the other hand, if you know what you are doing you can touch a modules's global 
variables with the same notation used to refer to its functions, modname.itemname.

Modules can import other modules. It is customary but not required to replace all import statements at the beginning
of a module (or script,for that matter). The imported module names are placed in the importing module's global symbol 
table.

There is variant of the import statement that imports names from a module directly into the importing module's symbol
table. For example:

This does not introduce the module name from which the imports are taken in the local symbol table (so in the example,
fibo is not defined.

This imports all names except those beginning with an underscore (_). In most case Python programmers do not use this 
facility since it introduces an unknown set of names into hte interpreter, possibly hiding some things you have already
defined. 

Note that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly
readable code. However, it is okay to use it to save typing interpreter sessions.

Note: For efficiency reason, each module is only imported once per interpreter session. Therefore, if you change your 
modules, you must restart the interpreter - or, if it's just one module you want to test interactively, use 
imprtlib.reload(), e.g. import iimportlib; importlib.reload(modulename).

6.1.1. Executing modules as scripts

When you run a Python module with

Python fibo.py <arguments>

The code in the module will be executed, just as if you imported it, but with the __name__ set to '__main__'. That means
that by adding this code at the end of your module:
"""


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))


"""
You can make the file usable as a script as well as an importable module, because the code that parse the command line
only runs if the module is executed as the "main" file:

If the module is imported, the code is not run.

This is often used either to provide a convenient user interface to a module, or for testing purpose (running the module
as a script executes a test suite).

6.1.2. The module search path

When a module named spam is imported, the interpreter first searches for a built-in module with that name. If not found, 
it then searches for a file named spam.py in a list of directories given by the variable sys.path. sys.path is 
initialized from these locations:

    - The directory containing input script (or the current directory when no file is specified).
    - PYTHONPATH (a list of directory names, with the name syntax as the shell variable PATH).
    - The installation-dependent default.
    
Note: On file systems which support symlinks, the directory containing the input script is calculated after teh symlink
is followed. In other words the directory containing the symlink is not added to the module search path.

After initialization, Python programs can modify sys.path. The directory containing the script being run is placed at 
the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be 
loaded instead of modules of the same name in the library directory. This is an error unless the replacement is instead.
See section Standard Modules for more information.

6.1.3. "Compile" Python files

To speed up loading modules, python caches the compiled version of each module in the __pychache__ directory under
the name module.version.pyc, where the versioin encodes the format of the compiled file; it generally contains the 
python version number. For example, in CPython release 3.3 the compiled version of spam.py would be cached as 
__pycache__/spam.cpython-33.pyc. This naming convention allows compiled modules from different release and different 
versions of Python to coexist.

Python checks the modification date of the source against the compiled version to see if it's out of date and need to be
recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the name
library can be shared among systems with different architecture.

Python does not check the cache in two circumstances, First it always re-compiles and does not store the result for the 
module that'si loaded directly from the command line, Second, it does not check teh cache if there is no source module. 
To support a non-source (compiled only) distribution. the compiled module must be in the source directory, and there must
not be a source module.

Some tips for experts:
    - you can use the -O or -OO switches on the Python command to reduce the size of compiled module. The -O switch 
    removes assert statements, the -OO switch removes both asert statements and __doc__ strings. Since some programs may
    relay on having these available, you should only use this option if you know what you're doing. "Optimized" modules 
    have an oopt- tag and are usually smaller. Future releases may change the effects of optimization.
    
    - A program doesn't turn any faster when it is read from a .pyc file than when it is read from a .py file; the only 
    thing that's faster about .pyc files is the spead with which they are loaded.
    
    - The module compileall can create .pyc files for all modules in a directory.
    
    - There is more detail on this process, including a flow chart of the decisions, in PEP 3147.
"""