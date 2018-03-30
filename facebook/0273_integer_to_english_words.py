"""
273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less that 2**31 - 1.
For example,
    123 -> "One Hundred Twenty Three"
    12345 -> Twelve Thousand Three Hundred Forty Five"
    1234567 -> One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Thought progress:
    1. Every three digits, we have a different unit. Such as thousand, million, billion, trillion.
    2. Thus, if we solve 3 digits number, then we can solve the problem.
    3. Try to figure out how to solve three digits number.
    4. From 0 to 19 we have single word to represent it.
    5. From 20 to 99, we need tens and single digits number to represents it.
    6. From 100 to 999, we need the hundreds and #5.
"""
from collections import ChainMap
import builtins
import os, argparse


def number_to_words(num):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen ' \
        'Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n//10-2]] + words(n%10)
        if n < 1000:
            return [to19[n//100-1]] + ['Hundred'] + words(n%100)
        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            if n < 1000**(p+1):
                return words(n//1000**p) + [w] + words(n%1000**p)
    return ' '.join(words(num)) or 'Zero'


"""
reversed(seq)
    Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol
    (the __len__() method and teh __getitem__() method with integer arguments starting at 0).
    
round(number[, n-digits])
    Return number rounded to n-digits precision after the decimal point. If n-digits is omitted or is None, it returns
    the nearest integer to its input.
    
    For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus 
    n-digits; if two multiples are equally close, rounding is done toward the even choice ( so, for example, both 
    round(0.5) and round(-0.5) are 0 and round(1.5) is 2). Any integer value is valid for n-digit (positive, zero, or 
    negative). the return value is an integer if called with one argument, otherwise of the same type as number.
    
    For a general Python object number, round(number, n-digits) delegates to number.__round__(n-digits).
    
    Note: the behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the 
    expected 2.68. This is not a bug: it's a result of the fact tht most decimal fractions can't be represented exactly 
    as a float. See Floating Point Arithmetic: Issues and Limitations for more information.
    
class set([iterable])
    Return a new set object, optionally with elements taken from iterable. set is a built-in class. See set and Set 
    Types - set, frozenset for documentation about this class.
    For other containers see the built-in frozenset, list, tuple, and dict classes, as well as the collections module.
    
setattr(object, name, value)
    This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may 
    name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object
    allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
    
class slice(stop)
class slice(start, stop[. step])
    Return a slice object representing the set of indices specified by range(start, stop, step). The start and step 
    arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return 
    the argument values (or their default). They have no other explicit functionality; however they are used by 
    Numerical Python and other third party extensions. Slice objects are also generated when extended indexing syntax
    is used. for example a[start:stop:step]
    or a[start:stop, i]. See itertools.islice() for an alternate version that returns an iterator.
    
sorted(iterable, *, key=None, reverse=False)
    Return a new sorted list fom teh items in iterable.
    has two optional arguments which must be specified as keyword arguments.
    key specifies a function of one argument that is used to extract a comparison key from each list element: 
    key=str.lower. The default value is None. (Compare the elements directly).
    reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
    Use functools.com_to_key() to convert an old-style cmp function to a key function.
    
    The built-in sorted() is guaranteed to be stable. A sort is stable if guarantees not change the relative order of 
    elements that compare equal - this is helpful for multiple passes (for example, sort by department, then sort by
    salary).
    
    For sorting examples and sorting tutorial, see Sorting How to.
    
@staticmethod
    Transform a method to a class static method.
    
    A static method does not receive an implicit first argument. To declare a static method, use this idiom.
 """


class C:

    def __init__(self):
        pass

    @staticmethod
    def f(arg1, arg2):
        pass


"""
    The @staticmethod form is a function decorator, - see the description of the function definitions in Function 
    Definition for detail.
    
    It can be called either on the class (such as C.f()), or on an instance (such as C().f()). The instance is ignored
    except for its class.
    
    Static method are similar found in Java or C++. Also see @classmethod for a variant that is useful for creating 
    alternate class constructor.
    
    Like all decorator, it is also possible to call staticmethod as a regular function and do something with its result.
    This is needed in some cases where you need reference to a function from class body and you want to avoid 
    automatically transformation to instance method. For this case, use this idiom:
"""


class C1:
    builtin_open = staticmethod(open)


"""
    For more information on static method, consult the documentation on the standard type hierarchy in The Standard 
    Type hierarchy.
    
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
    Return a str version of object. See str() function for detail.
    
    str is a built-in string class. For general information from string, see text Sequence Type - str.
    
sum(iterable[, start])
    Sums start and teh items of an iterable from left to right and returns the total. start defaults to 0. The iterable's
    items are normally numbers, and teh start value is not allowed to be a string.
    
    For some use cases, there are good alternatives to sum(). The preferred, fast way to concatenate a sequence of 
    string is by calling ''.join(sequence). To add floating point value with extended precision, see math.fsum(). To 
    concatenate a series of iterable, consider using itertools.chain().
    
super([type[, object-or-type]])

    Return a proxy object that delegates method calls to parent or sibling class of type. This is useful for accessing 
    inherited methods that have been overridden in a class. The search order is same as that used by getattr() except 
    that the type itself is skipped.
    
    The __mro__ attribute of the type lists the method resolution search order used by both getattr() and super(). The 
    attribute is dynamic and can change whenever the inheritance hierarchy is updated. 
    
    If the second argument is omitted, the super object returned is unbound. If the second argument is a object, 
    isinstance(obj, type) must be true. If the second argument is a type, issubclass(type2, type) must be true (this is 
    useful for classmethods).
    
    This are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer
    to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels
    the use of super in other programming languages.
    
    The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case
    is unique to Python and is not found in statically compiled languages or languages that only support single 
    inheritance. This makes it possible to implement "diamond diagrams" where multiple base classes implement the same 
    methods. Good design dictates that this method have the same calling signature in every case (because the order of 
    calls is determined at runtime, because that order adapts to changes in teh class hierarchy, and because that order 
    include sibling classes that are unknown prior to runtime).
    
    For both use cases, a typical superclass call looks like this:
"""


class C(B):
    def method(self, arg):
        super().method(arg)


"""
    Note that super() is implemented as part of the binding process for explicit dotted attribute lookups such as 
    super().__getitem__(name). It does so by implementing its own __getattribute__() method for searching class in a 
    predictable order that supports cooperative multiple inheritance. Accordingly, super() is undefined for implicit 
    lookups using statements for operators such as super()[name].
    
    Also note that, aside from the zero argument form, super() is not limited to use inside methods. The tow argument 
    form specifies the argument exactly and makes the appropriate references. The zero argument form only works inside 
    a class definition, as the compiler fills in the necessary details to correctly retrieve the class being defined. as 
    well as accessing the current instance for ordinary methods.
    
    For practical suggestions on how to design cooperative classes using super(), see guide to using super().
    
tuple([iterable])

    Rather than being a function, tuple is actually an immutable sequence type, as documented in Tuples and Sequence
    Types - list, tuple, range.
    
class type(object)
class type(name, bases, dict)

    With one argument, return the type of an object. The return value is a type object and generally the same object as
    returned by object.__class__.
    
    The isinstance() built-in function is recommended for testing the type of an object, because it takes subclasses
    into account.
    
    with three arguments, return a new type object. This is essentially a dynamic form of the class statement. The name
    string is the class name and becomes the __name__ attribute; the bases typle itemizes the base classes and becomes 
    the __bases__ attribute; and the dict dictionary is the namespace containing definitions for class body and is 
    copied to a standard dictionary to become the __dict__ attribute. For example, the following two statements create 
    identical type objects:
    
    See also Type Objects.
    
vars([object])
    
    Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
    
    Objects such as modules and instances have an updateable __dict__ attribute; however, other objects may have write 
    restrictions on their __dict__ attributes (for example, classes use a types.MappingProxyType to prevent direct 
    dictionary updates).
    
    Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads since updates 
    to the locals dictionary are ignored.
    
zip(*iterables)
    
    Make an iterator that aggregates elements from each of the iterables.
    Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences 
    or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it 
    returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to:
"""


def zip1(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


"""
    The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a 
    data series into n-length groups using zip(*[iter(s)]*n). This repeat the same iterator n times so that each output
    tuple has the result of n calls to the iterator. This has the effect of dividing the input into n-length chunks.
    
    zip() should only be used with unequal length inputs when you don't case about trailing, unmatched values from  the 
    longer iterables. If those values are important, use itertools.zip_longest() instead.
    
    zip() in conjunction with the * operator can be used to unzip a list:
    
    
__import__(name, globals=None, locals=None, fromlist=(), level=0)

    Note: This is an advanced function that is not needed in everyday Python programming, unlike 
    importlib.import_module().
    
    This functions is invoked by the import statement. It can be replaced (by importing the builtins module and 
    assigning to builtins.__import__) in order to change semantics of the import statement, but doing so is strongly 
    discouraged as it is usually simpler to use import hooks (see PEP 302) to attain the same goals and does not cause 
    issues with code which assumes the default import implementation is in use. Direct use of __import__() is also 
    discouraged in favor of importlib.import_module().
    
    The function imports the module name, potentially using the given globals and locals to determine how to interpret 
    the name in a package context. The fromlist gives the names of objects or submodules that should be imported from 
    the module given by name. The standard implementation does not use its locals argument at all, and uses its globals
    only to determine the package context of the import statement.
    
    level specifies whether to use absolute or relative imports. 0 (the default) means only perform absolute imports. 
    Positive values for level indicate the number of parent directories to search relative to the directory of the 
    module calling __import__() (see PEP 328 for the details).
    
    when the name variable is of the form package.module, normally, the top-level package (the name up till the first 
    dot) is returned, not the module named by name. However, when a non-empty fromlist argument is given, the module 
    named by name is returned.
    
    For example, the statement import spam results in bytecode resembling the following code:
    
    The statement import spam.ham results in this call:
    
    Note now __import__() returns the top-level module here because this is the object that is bound to a name by the 
    import statement.
    
    On the other hand, the statement from spam.han import eggs, sausage as saus result in:
    
    Here, the spam.ham module is returned from __import__(). From this object, the names to import are retrieved and 
    assigned to their respective names.
    
    If you simply want to import a module (potentially within a package) by name, use importlib.import_module().
    
enumerate(iterable, start=0)
    
    Return an enumerate object. iterable must be a sequence, an iterator, or some other object which support iteration.
    The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which 
    defaults to 0) and the values obtained from iterating over iterable.
    
    Equivalent to:
"""


def enumerate1(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


"""
collections - Container datatypes

This module implements specialized container datatypes providing alternatives to Python's general purpose built-in 
containers, dict, list, set, and tuple.

namedtuple()        factory function for creating tuple subclasses with named fields
deque               list-like container with fast appends and pops on either end
ChainMap            dict-like class for creating a single view of multiple mappings
Counter             dict subclass for counting hashable objects
OrderedDict         dict subclass that remembers the order entries were added
defaultdict         dict subclass that calls a factory function to supply missing value
UserDict            wrapper around dictionary objects for easier dict subclassing
UserList            wrapper around list objects fro easier list subclassing
userString          wrapper around string objects for easier string subclassing

ChainMap objects
    
    A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. It is 
    often much faster then creating a new dictionary and running multiple update() calls. 
    
    The class can be used to simulate nested scopes and is useful in templating.
    
    class collection.ChainMap(*maps)
    
    A ChainMpa groups multiple dicts or other mappings together to create a single, updateable view. If no maps are 
    specified, a single empty dictionary is provided so that a new chain always has at least one mapping.
    
    The underlying mappings are sorted in a list. That list is public and can be accessed or updated using the maps 
    attribute. This is no other state.
    
    Lookups search the underlying mappings successively until a key is found. In contrast, writes, updates, and 
    deletions only operate on the first mapping.
    
    A ChainMap incorporates the underlying mappings by reference. So, if one of the underlying mappings gets updated, 
    those changes will be reflected in ChainMap.
    
    All of the usual dictionary methods are supported. In addition, there is a maps attribute, a method for creating 
    new sub-contexts, and a property for accessing all but the first mapping:
    
    maps
        A user updateable list of mappings. The list is ordered from first-searched to last-searched. It is th only 
        stored state and can be modified to change which mappings are searched. The list should always contains at 
        least one mapping.
        
    new_child(m=None)
        Returns a new ChainMap containing a new map followed by all of the maps in the current instance. If m is 
        specified, it becomes the new map at the front of the list of mappings; if not specified, an empty dict is used,
        so that a call to d.new_child() is equivalent to: ChainMap({}, *d.maps). This method is used for creating 
        sub-contexts that can be updated without altering values in any of the parent mappings.
        
    parents
        Property returning a new ChainMap containing all of the maps in teh current instance except the first one. This
        is useful for skipping the first map in the search. Use cases are similar to those for the nonlocal keyword
        used in nested scopes. The use cases also parallel those for the built-in super() function. A reference to 
        d.parents is equivalent to: ChainMap(*d.maps[1:]).
        
    See also:
        - The multiContext class in the Enthought CodeTools package has options to support writing to any mapping in 
        the chain.
        - Django's Context class for templating is a read-only chain of mappings. It also features pushing and popping
        of contexts similar to the new_child() method and the parents() property.
        - The Nested Contexts recipe has options to control whether writes and other mutations apply only to the first 
        mapping or to any mapping in the chain.
        
ChainMap Examples and Recipes

    This section shows various approaches to working with chained maps.
    
    Example of simulating Python's internal lookup chain: 
"""


pylookup = ChainMap(locals(), globals(), vars(builtins))


"""
    Example of letting user specified command-line arguments take precedence over environment variables which in turn
    take precedence over default values:
"""

defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k:v for k, v in vars(namespace).items() if v}

combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])


"""
    Example patterns for using the ChinMap class to simulate nested contexts:
"""


c = ChainMap()          # Create root context
d = c.new_child()       # Create nested child context
e = c.new_child()       # Child of c, independent from d
e.maps[0]               # Current context dictionary -- like Python's locals()
e.maps[-1]              # Root context -- like Python's globals()
e.parents               # Enclosing context chain -- like Python's non-locals

d['x']                  # Get first key in the chain of contexts
d['x'] = 1              # Set value in current context
del d['x']              # Delete from current context
list(d)                 # All nested values
k in d                  # Check all nested values
len(d)                  # Number of nested values
d.items()               # All nested items
dict(d)                 # Flatten into a regular dictionary


"""
    The ChainMap class only makes updates (writes and deletions) to the first mapping in the chain while lookups will
    search the full chain. However, if deep writes and deletions re desired, it is easy to make a subclass that updates
    keys found deeper in the chain:
"""


class DeepChainMap(ChainMap):
    'Variant of ChainMap that allows direct updtes to inner scopes'

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)


"""
Counter objects

    A counter tool is provided to support convenient and rapid tallies. For example:
    
    class collections.Counter([iterable-or-mapping])
    
    A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements ar stored
    as dictionary keys and there counts are stored as dictionary values. Counters are allowed to be any integer value 
    including zero or negative counts. The Counter class is similar to bags or multi-sets in other language.
    
    Elements are counted from an iterable or initialized from another mapping (or counter):
    
    Counter objects have a dictionary interface except that they return a zero count for missing items instead of 
    raising a KeyError:
    
    Setting a count to zero does not remove an element from a counter. Use del to remove it entirely.
    
    Counter objects support three methods beyond those available for all dictionaries:
    
    elements()
        Return an iterator over elements repeating each as many times as its count. Elements are returned in arbitrary
        order. If an element's count is less tht one, elements() will ignore it.
        
    most_common[n]
        Return a list of the n most common elements and their counts from teh most common to the list. If n is omitted 
        or None, most_common() returns all elements in the counter. Elements with equal counts are ordered arbitrarily:
        
    subtract([iterable-to-mapping])
        Elements are subtracted from an iterable or from another mapping (or counter). Like dict.update() but adds 
        counts instead of replacing the. Also, the iterable is expected to be a sequence of elements, not a sequence of
        (key, value) pairs.
        
    Common patterns for working with Counter objects:
"""


sum(c.values())         # total of all counts
c.clear()               # reset all counts
list(c)                 # list unique elements
set(c)                  # convert to a set
dict(c)                 # convert to a regular dictionary
c.items()               # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pair)) # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]   # n least common elements
+c                      # remove zero and negative counts
