"""
54. Spiral Matrix

Given a matrix of m x n element (m rows, n columns), return all elements of the matrix in spiral order.

For example,

Given the following matrix:

[
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
]

You should return [1, 2, 3, 6, 9, 8, 7, 4, 5]

Approach 1: Simulation

Intuition

Draw the path that the spiral makes, we know that the path should turn clockwise whenever it would go out of bounds or
into a cell that previously visited.

Algorithm

Let the array have r rows and c columns. seen[r][c] denotes that the cell on the r-th row and c-th column was previously
visited. our current position is (r, c), facing direction di, and we want to visit r x c total cells.

As we move through the matrix, our candidate next position is (cr, cc), if the candidate is in the bounds of the matrix
and unseen, then it becomes our next position; otherwise, our next position is the one after performing a clockwise
turn.
"""


class Solution(object):
    def spiral_order(self, matrix):
        """
        Time complexity: O(n), where N is the total number of elements in the input matrix. We add every element in the
        matrix to our final answer.
        Space complexity: O(n), the information stored in seen and ans.
        :param matrix:
        :return:
        """

        if not matrix:
            return []

        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0

        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]

        return ans


"""
Approach 2: Layer-by-layer

Intuition

The answer will be all teh element in clockwise order for the first-outer layer, followed by the elements from the 
second-outer layer, and so on.

Algorithm

We define the k-th outer layer of a matrix as all elements that have minimum distance to some border equal to k. For 
example, the following matrix has all elements in the first-outer layer equal to 1, all elements in the second-outer 
layer equal to 2, and all elements in the third-outer layer equal to 3.

For each outer layer, we want to iterate through its elements in clockwise order starting from the top left corner.
suppose the current outer layer has top-left coordinates (r1, c1) and bottom-right coordinates (r2, c2).

Then, the top rwo is the set of elements (r1, c) for  for c = c1, ..., c2, in that order, the rest of the right side is 
the set of elements (r, c2, for r = r1 + 1, ..., r2, in that order. Then, if there are four sides to this layer (ie., 
r1 < r2 and c1 < c2), we iterate through the bottom side and left side as shown in the solution below.
"""


class Solution1(object):
    def spiral_order(self, matrix):
        """
        Time Complexity: O(n), where N is the total number of elements in the input matrix. We add every elements in
        the matrix to our final answer.
        Space Complexity: O(n), the information stored in ans.
        :param matrix:
        :return:
        """

        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 +1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix:
            return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1

        return ans


"""
9.4. Random Remarks

Data attributes override method attributes with the same name; to avoid accidental name conflicts, which may cause 
hard-to-find bugs in large problems, it is wise to use some kind of convention that minimizes the chance of conflicts.
Possible conventions including capitalizing methods names, prefixing data attribute names with a small unique string 
(perhaps just an underscore), or using verbs for methods and nouns for data attributes.

Data attributes may be referenced by methods as well as by ordinary users ("clients") of an object. In other words, 
classes are not usable to implement purse abstract data types. In fact, nothing in Python makes it possible to 
enforce data hiding - it is all based upon convention. (On the other hand, the Python implementation, written in C, can 
completely hide implementation details and control access to an object if necessary; this can be used by extensions
to Python written in C.)

Clients should use data attributes with care - clients may mess up invariants maintained by the methods by stamping on
their data attributes. Note that clients may add data attributes of their own to an instance object without affecting
the validity of the methods, as long as name conflicts are avoided - again, a naming convention can save a lot of 
headaches here.

There is no shorthand for referencing data attribute ( or other methods!) from within methods. I find that this actually
increases the readability of methods: there is no chance of confusing local variables and instance variables when
glancing through a method.

Often,  the first argument of a method is called self. This is nothing more than a convention: the name self has 
absolutely no special meaning to Python. Note, however, that by not following the convention you code mby be less 
readable to other Python programmers, and it is also conceivable that a class browser program might be written that 
relies upon such a convention.

Any function object that is a class attribute defines a method for instances of that class. It is not necessary that 
the function definition is textually enclosed in the class definition: assigning a function object to a local variable
in the class is also ok. for example:
"""


def f1(self, x, y):
    return min(x, y)

class C:
    f = f1

    def g(self):
        return "hello world"

    h = g


"""
Now f, g and h are all attributes of class C that refer to function objects, and consequently they ar all methods of 
instances of C - h being exactly equivalent to g. Note that this practice usually only serves to confuse the reader of
a program.

Methods may call other methods by using the method attributes of the self argument:
"""


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


"""
Methods may reference global names in the same way as ordinary functions. the global scope associated with a method is
the module containing its definitions. (A class is never used as a global scope.) While one rarely encounters a good 
reason for using global data in a method, there are many legitimate uses of the global scope: for one thing, functions 
and modules imported into the global scope can be used by methods, as well as functions and classes defined in it.
usually, the class containing the method is itself defined in this global scope, and in the next section we'll find 
some good reasons why a method would want to reference its own class.

Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.

9.5. Inheritance

Of course, a language feature would not be worthy of the name "class" without supporting inheritance. The syntax for 
a derived class definition looks like this:

The name BaseClassName must be defined in a scope containing the derived class definition In place of a base class name,
other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in 
another module:

Execution of a derived class definition proceeds the same as for a base class. When teh class object is constructed, the 
base class is remembered. This is used for resolving attribute references: if a requested attributes is not found in 
the class, teh search proceeds to look in the base class. This rule is applied recursively if the base class itself is
derived from some other class.

There's nothing special about instantiation of derived classes: DerivedClassName() creates a new instance of the class.
Method references are resolved as follows: the corresponding class attributes is searched, descending down the chain of 
base classes if necessary, and the method reference is valid if this yields a function object.

Derived classes may override methods of their base classes. Because methods have no special privileges when calling
other methods of the same object, a method of a base class that calls another method defined in the same base class may
end up calling a method of a derived class that overrides it. (For C++ programmers: all methods in Python are 
effectively virtual.)

An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of 
the same name. There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, 
arugments). This is occasionally useful to clients as well. (Note that this only works if the base class is accessible 
as BaseClassName in the global scope.)

Python has two built-in functions tht work with inheritance:
    - use isinstance() to check the instance's type: isinstance(obj, int) will be true only if obj.__class__ is int or
    class derived from int.
    - Use issubclass() to check the class inheritance: issubclass(bool, int) is True since bool is a subclass of int.
    However, issubclass(float, int) is False since float is not a subclass of int.
    
9.5.1. Multiple Inheritance

Python supports a from of multiple inheritance as well. A class definition with multiple base classes looks like this:

For most purpose, in the simplest cases, you can think of the search of attributes inherited from a parent class as 
depth-first, left-to-right, not searching twice in the same class where is an overlap in the hierarchy. Thus ,if an 
attributes is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of 
Base1, and if it was not found there, it was searched for in Base2, and so on.

In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative
calls to super(). This approach is known in some other multiple-inheritance languages as call-next-method and is more 
powerful than the super call found in single-inheritance language.

Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships (
where at least one of the parent classes cna be accessed through multiple paths fom the bottommost class). For example, 
all classes inherit from object. so any case of multiple inheritance provides more than one path to reach object. To
keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way
that preserves the left-to-right ordering specified in each class, that calls each parent only once, and tht is 
monotonic (meaning that a class can be subclassed without affecting the precedence order of its parents). Taken together
these properties make it possible to design reliable and extensible classes iwht multiple inheritance. 

9.6. Private Variables

"Private" instance variables that connot be accessed except from inside an object dont' exist in Python. However, there
is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated 
as a non-public part of the API (whether it is a function, a method or a dta member). It should be considered as 
implementation detail and subject to change without notice.

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by
subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at
least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where 
classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the 
syntactic position of the identifier. as long as it occurs with the definitioin of a class.

Name mangling is helpful for letting subclasses override methods without breaking intra-class method calls. For example:
"""


class Mapping:
    def __int__(self, iterable):
        self.item_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update


class MappingSubclass(Mapping):

    def update(self, keys, values):
        for item in zip(keys, values):
            self.item_list.append(item)


"""
Note that the mangling rules are designed mostly to avoid accidents; it still is possible to access of modify a 
variable that is considered private. This can even be useful in special circumstances, such as in the debugger.
Notice that code passed to exec() or eval() does not consider the classname of the invoking class to be the current 
class; this is similar to the effect of the global statement, the effect of which is likewise restricted to code that
is byte-compiled together. The same restriction applies to getattr(), setattr(), and delattr(), as well as when 
referencing __dict__ directly.

9.7. Odds and Ends

Sometimes it is useful to have a data type similar to the Pascal "record" or C "struct", bundling together a few named 
data items, An empty class definition will do nicely:

A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the 
methods of that data type instead. For instance, if you have a function that formats some data from a file object, you 
can define a class with methods read() and realine() that get the data from a string buffer instead, and pass it as
an argument. 

Instance method objects have attributes, too: m.__self__ is the instance object with the method m(), and m.__func__ is 
the function object corresponding to the method.

9.8. Iterators

By now you have probably noticed that most container objects can be looped over using a for statement:

This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind the 
scenes, the for statement calls iter() on the container object. The function returns an iterator object that defines 
the method __next__() which accesses elements in the container one at a time. When there no more elements, __next__()
raises a StopIteration exception which tells the for loop to terminate. You can call the __next__() method using the 
next() built-in function; this example shows how it all works:

Having seen the mechanics behind the iterator protocol, it is eash to add iterator behavior to your classes. Define an 
__next__() method which returns an object with a __next__() method. If the class defines __next__(), then __iter__() 
can just return self:
"""

class Reverse:
    """
    Iterator for looping over a sequence backwards.
    """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


"""
9.9. Generators

Generators are simple and powerful tool for creating iterators. They are written like functions but use the yield 
statement whenever they want to return data. Each time next() is called on it, hte generator resumes where it left off
(it remembers all the data values and which statement was last executed). An example shows that generators can be 
trivially easy to create:
"""


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


"""
Anything that can be done with generators can also be done with class-based iterators as described in the previous
section. What makes generator so compact is that the __iter__() and __next__() methods are created automatically.

Another key feature is that the local variables and execution state are automatically saved between calls. This made
the function easier to write and much more clear than an approach using instance variables like self.index and 
self.data. 

In addition to automatic method creation and saving program state, when generators terminate, they automatically raise
StopIteration. In combination, this feature make it easy to create iterators with no more effort than writing a regular 
function.

9.10. Generator Expressions

Some simple generators can be code succinctly as expressions using a syntax similar to list comprehensions but with
parentheses instead of brackets. These expressions are designed for situations where the generator is used right away
by an enclosing function. Generator expression are more compact but less versatile than full generator definitions and 
tend to be more memory friendly than equivalent list comprehensions. 

10. Brief tour of the standard library

10.1. Operating system interface

The os module provides dozens of functions for interacting with the operating system:

Be sure to use the import os style instead form os import *. This will keep os.open() from shadowing the built-in open()
function which operates much differently.

The built-in dir() and help() functions are useful as interactive aids for working with large modules like os:

for daily file and directory management tasks, the shutil module provides a higher level interface that is easier to 
use:

10.2. File wildcards

The glob module provides a function for making file lists from directory wildcard searches:

10.3. Command Line Arguments

Common utility scripts often need to process command line arguments. These arguments are stored in the sys module's 
argv attribute as a list. For instance the following output results from running Python demo.py one tow three at the 
command line:

The getopt module process sys.argv using the convention of hte Unix getopt() function. More powerful and flexible
command line processing is provided by the argparse module.

10.4. Error output redirection and program termination

The sys module also has attributes for stdin, stdout, stderr. The latter is useful for emitting warnings and erros 
messages to make them visible even stdout has been redirected:

The most direct way to terminate a script is to use sys.exit().

10.5. String Pattern Matching

The re module provides regular expression tools for advanced string processing. For complex matching and 
manipulation, regular expressions offer succinct, optimized solutions:

when only simple capabilities are needed, string methods are preferred becuase they are easier ot read and debug:

10.6. Mathematics

The math module gives access to the underlying C library functions for floating point math:

The random module provides tools for making random selections;

The statistics module calculates basic statistical properties (the mean, median, variance, etc) of numeric data:

10.7. Internet Access

There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are
urllib.request for retrieving data from URLs and smtplib from sending mail:

10.8. Dates and Times

The Datetime module supplies classes for manipulating dates and times in both simple and complex ways. While data and 
time arithmetic is supported,the focus of the implementation is on efficient member extraction for output formating
and manipulation. The module also supports object that ar timezone aware.

10.9. Data compression

Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz2, lzma, 
zipfile, and tarfile.

10.10. Performance Measurement 

Some Python users develop a deep interest in knowing the relative performance of different approaches to the same 
problem. Python provides a measurement tool that answers those questions immediately.

For example, it may be tempting to use the tuple packing and unpacking feature instead of the traditional approach to 
swapping argument. the timeit mdoule quickly demonstrates a modest performance advantage.

In contrast to timeit's fine level of granularity, the profile and pstats modules provide tools for identifying time 
critical sections in larger blocks of code.

10.11. Quality control

One approach for developing high quality software is to write tests for each function as it is developed and to run 
those tests frequently during the development process.

The doctest module provides a tool for scanning a module and validating tests embedded in a program's docstrings. Test
construction is as simple as cutting-and-pasting a typical call along with its results into th docstring. This improves
the documentation by providing hte user with an example and it allows the doctest module to make sure the ode remains 
true to the documentation:

The unittest module is not as effortless as the doctest module, but it allows a more comprehensive set of tests to be 
maintained in a separate file:

10.12. Batteries Included

Python has a "batteries included" philosophy. This is best seen through the sophisticaled and robust capabilities of 
its large packages. For example:
    
    - The xmlrpc.client and xmlrpc.server module make implementing remote procedure calls into an almost trivial task. 
    Despite the modules names, no direct knowledge or handling of XML is needed.
    
    - The email package is a library for managing email massages, including MINE and other RFC 2822-based message 
    documents. Unlike smtplib and poplib which actually send and receive messages, the email package has a complete
    toolset for building or decoding complex message structures (including attachments) and for implementing internet 
    encoding and header protocols.
    
    - The json package provides robust support for parsing this popular dat interchange format. The csv module supports 
    direct reading and writing of fies in comma-separated value format, commonly supported by databases and 
    spreadsheets. XML processing is supported by xml.etree.ElementTree, xml.doom and xml.sax packages. Together, these
    modules and packages greatly simplify data interchange between Python applications and other tools.
    
    - The sqlite3 module is wrapper for SQLite database library, providing a persistent database that can be updated and
    accessed using slightly nonstandard SQL syntax. 
    
    - internationalization is supported by a number of modules including gettext, locale, and the codecs package.
    
11. Brief tour of the standard library - part II

This second tour covers more advanced modules that support professional programming needs. These modules rarely occur in 
small scripts.
"""
