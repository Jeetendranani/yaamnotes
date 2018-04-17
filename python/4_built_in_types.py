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

Sequence of the same type also support comparisons. In particular, tuples and lists are compared lexicographically by
comparing corresponding elements. This means that to compare equal, every element must compare equal and the two
sequence must be of the same type and have the same length. (For full details see Comparisons in the language
reference.)

Notes:
    1. While the in and not in operation are used only for simple containment testing in the general case, some
    specialised sequences (such as str, bytes and bytearray) also use them for subsequence testing:

    2. values of n less than 0 are treated as 0 (which yields an empty sequence of the same type as). Note that
    items in the sequence s are not copied; they are referenced multiple times. This often haunts new Python programmers

    What has happened is that [[]] is a one-element list containing an empty list, so all three elements of
    [[]] * 3 are references to this single empty list. Modifying any of the elements of lists modifies this single
    list. You can create a list of different list this way.

    Further explanation is available in FAQ entry How to I create multidimensional list?.

    3. If i or j negative, the index is relative to the end of sequence s: len(s) + i or len(s) + j is substituted.
    But note that -0 is still 0.

    4. The slice of s from i to j is defined as the sequence of items with index k such that i <= k < j. If i or j
    is greater than len(s), use len(s). If i is omitted or None, use 0. If j is omitted or None, use len(s). If i
    is greater than or equal to j, the slice is empty.

    5. The slice of s from i to j with step k is defined as the sequence of items with index x = i + n*k such that
    0 <= n < (j-i)/k. In other words, the indices are i, i+k, i+2k, i+3k and so on, stopping when j is reached (but
    never include j). When k is positive, i and j are reduced to len(s) if they are greater, When k is negative,
    i and j are reduced to len(s) -1 if they are greater. If i or j are omitted or None, they becomes "end" value
    (which end depends on the sign of k). Note, k cannot be zero, if k is None, it is treated as 1.

    6. Concatenating immutable sequences always results in a new object. This means that building up a sequence
    by repeated concatenation will have a quadratic runtime cost in the total sequence length. To get a linear
    runtime cost, you must switch to one of the alternatives below:

        - If concatenating str object, you can built a list and use str.join() at the end or else write to
        io.StringIO instance and retrieve its value when complete.
        - If concatenating bytes objects, you can similarly use bytes.join() or io.BytesIO, or you can do in-place
        concatenation with bytearray object. bytearray objects are mutable and have efficient over allocation
        mechanism
        - if concatenating tuple objects, extend a list instead.
        - for other types, investigate the relevant class documentation

    7. Some sequence types (such as range) only support item sequences that follow specific patterns, and hence don't
    support sequence concatenation or repetition.

    8. index raises ValueError when x is not found in s. Not all implementations support passing the additional
    arguments i and j. These arguments allow efficient searching of subsections of the sequence. Passing the extra
    arguments is roughly equivalent to using s[i:j].index(x), only without copying any data and with the returned
    index being relative to teh start of the sequence rather than the start of teh slice.

4.6.2. Immutable sequence types

The only operation that immutable sequence types generally implement that is not also implemented by mutable
sequence types is supported for the hash() built-in.

This support allows immutable sequences, such as tuple instances, to be used as dict keys and stored in set
and frozenset instances.

Attempting to hash an immutable sequence contains unhashable values will result in TypeError.

4.6.3. Mutable sequence types

The operations in the following table are defined on mutable sequence types. The collections.abc.MutableSequence
ABC is provided to make it easier to correctly to implement these operations on custom sequence types.

In the table s is an instance of a mutable sequence type, t is an iterable object and x is an arbitrary object
that meets any type and value restrictions imposed by s (for example, bytearray only accepts integers that meet
the value restriction 0 <= x <= 255).

s[i] = x
s[i:j] = t
del s[i:j]
s[i:j:k] = t
del s[i:j:k]
s.append(x)
s.clear()
s.copy()
s.extend(t) or s += t
s *= n
s.insert(i, x)
s.pop([i])
s.remove(x)
s.reverse()

Notes:
    1. t must have the same length as the slice it is replacing
    2. The optional argument i defaults to -1, so that by default the last item removed and returned.
    3. remove raises ValueError when x is not found in s.
    4. The reverse() method modifies the sequence in place for economy of space when reversing a large sequence.
    To remind users that it operates by side effect, it does not return the reversed sequence.
    5. clear() and copy() are included for consistency with the interfaces of mutable containers that don't
    support slicing operations (such as dict and set).
    6. The values n is an integer, or an object implementing __index__(). zero and negative values of n clear the
    sequence. items in the sequence are not copied; they are referenced multiple imes, as explained for s * n
    under Common Sequence Operations.

4.6.4. Lists

Lists are mutable sequences, typically used to store collections of homogeneous  items (where the precese degree
of similarity will vary by application).

class list([iterable])
    Lists may be constructed in several ways:

        - Using a pair of square brackets to denote the empty list: []
        - using square brackets, separating items with commas: [a], [a, b, c]
        - using a list comprehension: [x for x in iterable]
        - using the type constructor: list() or list(iterable)

    The constructor builds a list whose items are the same and in teh same order as iterable's items. iterable
    may be either a sequence, a container that supported iteration, or an iterable object. If iterable is already
    a list, a copy is made and returned, similar to iterable[:]. For example, list('abc') returns ['a', 'b', 'c']
    and list((1, 2, 3)) returns [1, 2, 3]. If no arguments is given, the constructor creates a new empty list, [].

    Many other operations also produce lists, including the sorted() built-in.

    Lists implement all the common and mutable sequence operations. Lists also provide the following additional
    method:

    sort(*, key=None, reverse=False)
        This method sorts the list in place, using only < comparisons between items. Exceptions are not suppressed
        - if any comparison operation fail, the entire sort operation will fail (and the list will likey be left
        in partially modified state).

        sort() accept two arguments that can only be passed by keyword (keyword-only arguments):

        key specifies a function of one argument that is used to extract a comparison key from each list element
        (for example, key=str.lower). The key corresponding to each item in the list is calculated once and then used
        for the entire sorting process. The default value of None means that list items are sorted directly without
        calculating a separate key value.

        The functools.cmp_to_key() utility is available to convert a 2.x style cmp function to a key function.

        Reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were
        reversed.

        This method modifies the sequence in place for economy of space when sorting a large sequence. To remind users
        that it operates by side effect, it does not return the sorted sequence (use sorted() to explicitly request
        a new sorted list instance).

        The sort() method is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order
        of elements that compare equal - this is helpful for sorting in multiple passes (for example, sort by
        department, then by salary grade).

        CPython implementation detail: while a list is being sorted, the effect of attempting to mutate, or even
        insert, the list is undefined. The C implementation of Python makes the list appear empty for the duration,
        and raises ValueError if it can detect that the list has been mutated during a sort.

4.6.5. Tuples

Tuples are immutable sequence, typically used to store collections of heterogeneous data (such as the 2-tuples
produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous
data is needed (such as allowing storage in a set or dict instance).

class tuple([iterable])
    Tuples may be constructed in a number of ways:

        - Using a pare of parentheses to denote the empty tuple: ()
        - Using a trailing comma for a single tuple: a, or (a,)
        - Separating items with commas: a, b, c or (a, b, c)
        - Using the tuple() built-in: tuple() or tuple(iterable)

    The constructor builds a tuple whose items are the same and in the same order as iterable's items. iterable
    may be either a sequence, a container that supports iteration, or an iterator object. If iterable is already
    a tuple, it is returned unchanged.

    Note that it is actually the comma which makes a tuple, not the parentheses. the parentheses are optional,
    except in the empty tuple case, or when they are needed to avoid syntactic ambiguity.

    Tuples implement all of the common sequence operations.

For heterogeneous collections of data where access by name is clearer than access by index, collections.namedtuples()
may be a more appropriate choice than a simple tuple object.

4.6.6. Ranges

The range type presents an immutable sequence of numbers and is commonly used for looping a specific number of
items in for lops.

class range(stop)
class range(start, stop[, step])
    The arguments to the range constructor must be integers (either built-in int or any object that implements the
    __index__ special method). If the step argument is omitted, it defaults to 1, if the start argument is omitted
    it default to 0, if step is zero, ValueError is raised.

    for a positive step, the contents of a range r are determined by the formula r[i] = start + step*i where
    i >= 0 and r[i] < stop.

    For a negative step, the contents of the range are still determined by the formula r[i] = start + step*i, but
    the constraints are i >= 0 and r[i] > stop.

    A range object will be empty if r[0] does not meet the constraint. Ranges do support negative indices, but these
    are interpreted as indexing from the end of the sequence determined by the positive indices.

    Ranges containing absolute values larger than sys.maxsize are permitted but some features (such as len())
    may raised OverflowError.

    Ranges implement all of the common sequence operations except concatenation and repetition (due to the fact that
    range objects can only represent sequences tht follow a strict pattern and repetition and concatenation
    will usually violate that pattern).

    start
        The value of the start parameter (or 0 if the parameter was not supplied)

    stop
        The value of the stop parameter

    step
        The value of the step parameter (or 1 if the parameter was not supplied)

The advantage of the range type over a regular list or tuple is that a range object will always take teh same
(small) amount of memory, no matter the size of the range it represents (as it only sotres the sart, stop and
step values, calculating individual items and sub ranges as needed).

Range objects implement the collections.abc.Sequence ABC, and provide features such as containment tests,
element index lookup, slicing and support for negative indices (see Sequence Type - list, tuple, range):

Testing range objects for equality with == and != compares them as sequences. That is, two range objects are
considered equal if they represent the same sequence of values. (Note that two range objects that compare equal
might have different start, stop, and step attributes, for example range(0) == range(2,1,3) or range(1.3,2)
== range(0, 4, 2).)

4.7. Text Sequence Type - str

Textual data in Python is handled with str objects, or stings, Strings are im-mutable sequences of Unicode code
points. String literals are written in a variety of ways:

    - Single quotes:
    - Double quotes:
    - Triple quoted:

Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.

String literals that are part of a single expression and have only whitespace between them will be implicitly
converted to a single string literal.

See String and Byte literals for more about various from of string literal, including supported escape sequences,
and the r("raw") prefix that disables most escape sequence processing.

Strings may also be created from other objects using the str constructor.

Since there is no separate "character" type, indexing a string produces string of length 1. That is , for a non-empty
string s, s[0] == s[0:1].

There is also no mutable string type, but str.join() or io.StringIO can be used to efficiently construct strings
from multiple fragments.

class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
    Return a string version of object, if object is not provided, returns the empty string. Otherwise, the behavior of
    str() depends on whether encoding or errors is given, as follows.

    If neither encoding nor error is given, str(object) returns object.__str__(), which is the "informal" or nicely
    printable string representation of object. For string objects, this is the string itself. If object doesn't have
    a __str__() method, then str() falls back to return repr(objct).

    If at least one of encoding or errors is given, object should be a bytes-like object (e.g. bytes or bytearray).
    In this case, if object is a bytes (or bytearray) object, then str(bytes, encoding, errors) is equivalent to
    bytes.decode(encoding, errors). Otherwise, the bytes object underlying the buffer object is obtained before
    calling bytes.decode(). See Binary Sequence Types - bytes, bytearray, memoryview and Buffer Protocol for
    information on buffer objects.

    Passing a bytes object to str() without the encoding or error arguments falls under the first case of returning
    representation (see also the -b command-lien options to Python).

    for more information on the str class and its methods, see Text Sequence Type - str and the String Methods
    section below. To output formatted strings, see the Formatted string literals and Format Strings Syntax section.
    In addition, see the Text Processing Services section.

4.7.1. String methods

String implement all of the common sequence operations, along with the additional methods described below.

String also support two styles of string formatting. One providing a large degree of flexibility and customization
(see str.format(), Format String Syntax and Custom String Formatting) and the other based on C printf style
formatting that handles a narrower ragne of types and is slightly harder to use corectly, but is often faster
for the cases it can handle (printf-style Formatting).

The Text Processing Services section of the standard library covers a number of other modules that provide various
text related utilities (including regular expression support in the re module).

str.capitalize()
    Return a copy of the string with its first character capitalized and the rest lower cased.

str.casefold()
    REturn a casefolded copy of the string. Casefolded strings may be used for caseless matching.

    Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions
    in a string.

    The casefolding algorithm is describled in section 3.13 of the Unicode Standard.

str.center(width[, fillchar])
    Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII
    space). The original string is returned if width is less than or equal to len(s).

str.count(sub[, start[, end]])
    Return the number of non-overlapping occurrences of substring sub in the range [start, end], Optional arguments
    start and end are interpreted as in slice notation.

str.encode(encoding='utf-8', errors='strict')
    Return an encoded version of string as a bytes object. Default encoding is 'utf-8'. Errors may be given to set
    a different error handling scheme. The default for error is 'strict', meaning that encoding errors raise a
    UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and
    any other name registered via codecs.register_error(), see section Error handlers. For a list of possible encodings,
    see section Standard Encodings.

str.endswith(suffix[, start[, end])
    Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple
    of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing
    at that position.

str.expandtabs(tabsize=8)
    Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the
    current column and the given tab size. Tab positions occur every tabsize characters (default is 8, giving tab
    positions at columns 0, 8, 16 and so on). To expand the string, the current column is set to zero and the string
    is examined character by character. If the character is a tab (\t), one or more space characters are inserted
    in the result until the current columns is equal to the next tab position. (The tab character itself is not copied.)
    If the character is a newline (\n| or return (\r), it is copied and the current column is reset to zero. Any other
    character is copied unchanged and the current column is incremented by one regardless of how the character is
    presented when printed.

str.find(sub[, start[, end]])
    Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional
    arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

    Note: The find() method should be used only if you need to know the position of sub. to check if sub is a substring
    or not, use the in operator.

str.format(*args, **kwargs)
    Perform a string formatting operation. The string on which this method is called can contain literal text or
    replacement fields delimited by braces {}. Each replacement field contains either the number index of a positional
    argument, or the name of the keyword argument. Returns a copy of the string where each replacement field is replaced
    with the string value of the corresponding argument.

    See Format String Syntax for a description of the various formatting options that can be specified in format
    strings.

    Note: When formatting a number (int, float, float and subclass) with the n type (ex: '{:n}'.format(1234),
    the function sets temporarily the LC_CTYPE local to teh LC_NUMERIC locale to decode decimal_point and
    thousands_sep fields of localeconv() if they are non-ASCII or longer than 1 byte, and the LC_NUMERIC locale
    is different than the LC_CTYPE locale. This temporary change affects other threads.

str.format_map(mapping)
    Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict. This is
    useful if for example mapping is a dict subclass:

str.index(sub[, start[, end]])
    Like find(), but raise ValueError when the substring is not found.

str.isalnum()
    Return true if all characters in the strings are alphanumeric and there is at east one character, false
    otherwise. A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal()
    c.isdigit(), or c.isnumeric().

str.isalpha()
    Return true if all characters in teh string are alphabetic and there is at least one character, false otherwise.
    Alphabetic characters are those characters defined in the Unicode character database as "Letter", i.e., those with
    general category property being one of 'Lm', 'Lt', 'Lu', 'Li', or 'Lo'. Note that this is different from
    alphabetic property defined in the Unicode Standard.

str.isdecimal()
    Return true if all characters in the string are decimal characters and there is at least one character, false
    otherwise. Decimal characters are those that can be used to from numbers in base 10, e.g, U+0660, ARABIC-INDIC
    DIGIT ZERO. Formmaly a decimal character is a character in the Unicode General Category "Nd".

str.isdigit()
    Return true if all characters in the string are digits and there is at least one character, false otherwise.
    Digits include decimal characters and digits that need special handling, such as the compatibility superscript
    digits. This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formatlly,
    a digit is a character that has the property value Numeric_Type = Digit or Numeric_Type = Decimal.

str.isidentifier()
    Return true if the string is a valid identifier according to the language definition, section identifiers and
    keywords.

    Use keyword.iskeyword() to test for reserved identifiers such as def and class.

str.islower()
    Return true if all cased characters in the string are lowercase and there is at least one cased character,
    false otherwise.


"""