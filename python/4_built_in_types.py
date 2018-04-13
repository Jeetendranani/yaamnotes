"""
4. Built-in Types

The following sections describe the standard types that are built into the interpreter.

The principal built-in types are numerics, sequences, mappings, classes, instances and exceptions.

Some collection classes are mutable. The methods that add, subtract, or rearrange their numbers in place, and dont'
return a specific item, never return the collection instance itself but None.

Some operations are supported by several object types; in particular, practically all objects can be compared, tested
for truth value, and converted to a string (with the repr() function or the slightly different str() function). The
latter function is implicitly used when an object is written by the print() function.

4.1. Truth Value Testing

Any object can be tested for truth value, for use in an if or while condition or as operand of the boolean operations
below. The following values are considered false:

    - None
    - False
    - zero of any numeric type, for example, 0, 0.0, 0j.
    - any empty sequence, for example, '', (), [].
    - any empty mapping, for example {}
    - instances of use-defined classes, if the class defines a __bool__() or __len__() method, when that method returns
    the integer zero or bool value False.

All other values are considered true - so objects of many types are always ture.

Operations and built-in functions that have a boolean result always return 0 and False for false and 1 or True for true,
unless otherwise stated. (Important exception: the boolean  operations or and and already return one of their operands.)

4.2. Boolean operations - and, or , not

4.3. Comparisons

4.4. Numeric Types - int, float, complex

4.4.4. Hashing of numeric types

For numbers x and y. possibly of different types, it's a requirement that hash(x) == hash(y) (see the __hash__() method
documentation for more details). For ease of implementation and efficiency across a variety of numeric types (including
int, float, decimal.Decimal and fractions.Fraction) Python's hash for numeric types is based on a single mathematical
function that's defined for any rational number, and hence applies to all instance of int, and fractions.Fraction, and
all finite instances of float and decimal.Decimal. Essentially this function is given by reduction module P for fixed
prime P. The value of P is made available to Python as the modulus attributes of sys.bash_info.

CPython implementation detail: Currently, the prime used is P = 2**31-1 on machine with 32-bit C longs and 2**61 - 1
on machine with 64-bit C longs.

Here are the rules in detail:


4.5. Iterator Types

Python supports a concept of iteration over containers. This is implemented using tow distinct methods; these are used
to allow user-defined classes to support iteration. Sequences, described below in more detail, always support the
iteration methods.

One method needs to be defined for container objects to provide iteration support:

container.__iter__()
    return an iterator object. The object is required to support the iterator protocol described below. If a container
    supports different types of iteration, additional methods can be provided to specifically request iterators for
    those iteration types. (An example of an object supporting multiple forms of iteration would be a tree structure
    which supports both breadth-first and depth-first traversal.) This method corresponds to the tr_iter slot of the
    type strcture for Python objects in the Python /C API.

The iterator objects themselves are required to support the following two methods, which together from the iterator
protocol:

iterator.__iter__()
    return the iterator object itself. This is required to allow both containers and iterators to be used with the for
    and in statements. This method corresponds to he tp_iter slot of the type structure for Python /C API.

iterator.__next__()
    return the next item from th container. If there are no further items, raise the StopIteration exception. this
    method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.

Python defines several iterator objects to support iteration over general and specific sequence types, dictionaries,
and other more specialized forms. The specific types are not important beyond their implementation of teh iterator
protocol.

Once an iterator's __next__() method raised StopIteration, it must continue to do so on subsequent calls.
Implementations that do not obey this property ar deemed broken.

4.5.1. Generator Types

Python's generators provide a convenient way to implement the iterator protocol. If a container object's __iter__()
method is implemented as a generator, it will automatically return an iterator object (technically, a generator object)
supplying the __iter__() and __next__() methods. More information about generators can be found in the documentation
for the yield expression.

4.6. Sequence Types - list, tuple, range

There are three basic sequence type: lists, tuples, and range objects. Additional sequence types tailored for
processing of binary data and text strings are described in dedicated sections.

4.6.1. Common sequence operations

The operations in the following table are supported by most sequence types, both mutable and immutable. The
collections.abc.Sequence ABC is provided to make it easier to correctly implement this operations on custom sequence
types.

This table lists the sequence operations sorted in ascending priority. In the table, s and t are sequences of the same
type, n, i, j and k are integers and x is an arbitrary object that meets any type and value restrictions imposed by s.

The in and not in operations have the same priorities as the comparison operations. The + (concatenation) and *
(repetition) operations have the same priority as the corresponding numeric operations.

x in s
x not in s
s + t
s * n or n * s
s[i]
s[i:j]
s[i:l:k]
len(s)
min(s)
max(s)
s.index(x[, i[, j]])
s.count(x)


"""