"""
200. Number of islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You map assume all four edges of the grid are all
surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3


Thought process:
    1. This is a graph search problem, basically we have two way to do it:
        - DFS
        - BFS
    2. We need remember the position already visited or change the land to water to avoid duplicate.
"""
from collections import deque, namedtuple, OrderedDict, Counter
import itertools
import csv
import sqlite3


def num_islands(grid):
    def dfs(grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                res += 1
    return res


"""
Solution 1: DFS

Intuition

Treat the 2d grid map as undirected graph and there is an edge between two horizontally or vertically adjacent nodes of 
values '1'.

Algorithm:

Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search. During
DFS, every visited node should be set as '0' to mark as visited node. Count the number of root nodes that trigger DFS, 
this number would be the number of islands since each DFS starting at some root identifies an island.

Complexity Analysis
    - Time complexity: O(M x N) where M is the number of rows and N is the number of columns.
    - Space complexity: worst case O(M x N) in case that the grid map is filed with lands where DFS goes by M x N deep.
"""


"""
Solution 2: BFS

Algorithm

Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a BFS. Put it into a queue 
and set its value as '0' to mark as visited node. Iteratively search the neighbors of enqueued nodes until the queue 
becomes empty.

Complexity Analysis
    - time complexity: O(M x N) where M is the number of rows and N is the number of columns.
    - Space complexity: O(min(M, N)) because in worst case wher the grid is filled with lands, the size of queue can 
    group up to min(M, N).
"""


"""
Solution 3: Union Find (aka Disjoint Set)

Algorithm

Traverse the 2d grid map and union adjacent lands horizontally or vertically, at the end, return the number of 
connected components maintained in the UnionFind data structure.

Complexity Analysis

    - Time complexity: O(M x N) where M is the number of rows and N is the number of columns. Note that Union operation 
    takes essentially constant time when UnionFind is implemented with both path compression and union by rank.
    - Space complexity: O(M x N) as required by UnionFind data structure.
"""


"""
collections.Counter([iterable-or-mapping])
    Several mathematical operations are provided for combining Counter objects to produce multi-sets (counters that have
    counts greater that zero). Addition and subtraction combine counters by adding or subtracting the counts of 
    corresponding elements. Intersection and union return the minimum and maximum of corresponding counts. Each 
    operation can accept inputs with signed counts, but the output will exclude with counts of zero or less.
    
    Unary addition and subtraction are shortcuts for adding an empty counter or subtracting from an empty counter.
    
    Note: Counters were primarily designed to work with positive integers to represent running counts; however, care 
    was taken to not unnecessarily preclude use cases needing other types or negative values. To help with those use 
    cases, this section documents the minimum range and type restrictions.
        - The Counter class itself is a dictionary subclass with no restrictions on its keys and values. The values are 
        intended to be numbers representing counts, but you could store anything in the value field.
        - The most_common() method requires only that the values be order-able.
        - For in-place operations such as c[key] += 1, the value type need only support addition and subtraction. So 
        fractions, floats, and decimals would work and negative values are supported. The same is also true for update()
        and subtract() with allow negative and zero values for both inputs and outputs.
        - The multiset methods are designed only for use cases with positive values. The inputs may be negative or zero,
        but only outputs with positive values are created. there are no type restrictions, but the value type needs to
        support addition, subtraction, and comparison.
        - The elements() method requires integer counts. It ignores zero and negative counts.
        
    See also:
        - Bag class in smalltalk.
        - Wikipedia entry for multi-sets.
        - C++ multisets tutorial with examples.
        - For mathematical operations on multisets and their use cases, see Knuth Donald. The art of computer 
        programming volume II, section 4.6.3, Exercise 19.
        - The enumerate all distinct multisets of a given size over a given set of elements, see 
        itertools.combinations_with_replacement(): 
        
deque objects

class collections.deque([iterable[, maxlen])
    Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not 
    specified, the new deque is empty.
    
    Deques are a generalization of stacks and queue (the name is pronounced 'deck' and is short for 'double-ended 
    queue'). Deques support thread-safe, memory efficient appends and pops from either side of the deque with 
    approximately the same O(1) performance in either direction.
    
    Though list objects support similar operation, they are optimized from fast fixed-length operations and incur O(n)
    memory movement costs fro pop(0) and insert(0,v) operations which change both the size and position of the 
    underlying dta representation.
    
    if maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded to 
    the specified maximum length. Once a bounded length deque is full, when new items are added, a corresponding number 
    of items are discarded from the opposite end. bounded length deques provide functionality similar to the tail filter
    in Unix. They are also useful for tracking transactions and other pools of data where only the most recent activity 
    is of interest.
    
    Deque objects support the following methods:
    
    append(x)
        Add x to the right side of the deque.
        
    appendleft(x)
        Add x to the left side of the deque.
        
    clear()
        Remove all elements from the deque leaving it with length 0.
        
    copy()
        Create a shallow copy of the deque.
        
    count(x)
        Count the number of deque elements equal to (x).
        
    extend(iterable)
        Extend the right side of the deque by appending elements from the iterable argument.
        
    extendleft(iterable)
        Extend the left side of the deque by appending elements from the iterable. Note, the series of left appends
        results in reversing the order or elements in the iterable argument.
        
    index(x[, start[, strop])
        Return the position of x in the deque (at or after index start and before index stop). Returns teh first match 
        or raise ValueError if not found.
        
    insert(i, x)
        insert x into the deque at position i. 
        
        If the insertion would cause a bounded deque to grow beyond maxlen, an IndexError is raised.
        
    pop()
        Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.
        
    popleft()
        Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.
        
    remove(value)
        Remove the first occurrence of value. If not found, raise a ValueError.
        
    reverse()
        Reverse the elements of the deque in-place and then return None.
        
    rotate(n)
        Rotate the deque n steps to the right. if n is negative, rotate the left. rotating one step to the right is 
        equivalent to d.appendleft(d.pop()).
        
    Deque objects also provided one read-only attribute:
        
    maxlen
        Maximum size of a deque or None if unbounded.
        
    In addition to the above , deques support iteration, pickling, len(d), reversed(d), copy.copy(d), copy.deepcopy(d),
    membership testing with the in operator, and subscript references such as d[-1]. Indexed access is O(1) at both 
    ends but slows to O(n) in the middle. For fat random access, use lists instead.
    
    Starting in version 3.5, deques support __add__(), __mul__(), and __imul__().
    
deque recipes
    
    This section shows various approaches to working with deques.
    
    Bounded length deques provide functionality similar to the tail filter in Unix:
"""


def tail(filename, n=10):
    'REturn the last n lines of a tile'
    with open(filename) as f:
        return deque(f, n)


"""
    Another approach to using deques is to maintain a sequence of recently added elements by appending to the right and 
    popping to the left:
"""


def moving_arverage(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


"""
    The rotate() method provides a way to implement deque slicing and deletion. For example, a pure Python 
    implementation of del d[n] relies on the rotate() method to position elements to be popped:
"""


def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)


"""
    To implement deque slicing, use a similar approach applying rotate() to bring a target element to the left side of 
    the deque. Remove old entries with popleft(), add new entries with extend(), and then reverse the rotation. With
    minor variations on that approach, it is easy to implement Forth style manipulation such as dup, drop, swap, over, 
    pick, rot, and roll.
"""


"""
defaultdict objects

class collections.defaultdict([default_factory[]])
    Return a new dictionary-like object. defaultdict is subclass of the built-in dict class. It overrides one method and
    adds one writable instance variable. The remaining functionality is the same as for the dict class and is not 
    documented here.
    
    The first argument provides the initial value for the default_factory attribute; it defaults to None. All remaining
    arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
    
    defaultdict objects support the following method in addition to the standard dict operations:
    
    __missing__(key)
        if the default_factory attributes is None, this raises a KeyError exception with the key as argument.
        
        if default_factory is not None, it is called without arguments to provide a default value for the given key, 
        this value is inserted in the dictionary for the key, and returned.
        
        If calling default_factory raises an exception this exception is propagated unchanged.
        
        This method is called by the __getitem__() method of the dict class when the requested key is not found; 
        whatever it returns or raises is then returned or raised by __getitem__().
        
        Note that __missing__() is not called for any operations besides __getitem__(). This means that get() will, 
        like normal dictionaries, return None as a default rather that using default_factory.
        
    defaultdict objects support the following instance variable:
    
    default_factory
        This attributes is used by the __missing__() method; it is initialized from the first argument to the 
        constructor, if present, or to None, if absent.
        
defaultdict Examples
    using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists:
    
    When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically 
    created using the default_factory function which returns an empty list. The list.append() operations then attaches
    the value to the new list. When keys are encountered again, the look-up proceeds normally (returning the list for 
    that key) and the list.append() operation adds another value to the list. This technique is simpler and faster than
    an equivalent technique using dict.setdefault():
    
    Setting the default_factory to int makes the defaultdict useful for counting (like a bag or multiset in other 
    languages):
    
    when a letter is first encountered, it is missing rom the mapping, so the default_factory function calls int() to 
    supply a default count of zero. the increment operation then builds up the count for each letter.
    
    The function int() which always returns zero is just a special case of constant functions. A faster and more 
    flexible way to create constant functions is to use a lambda function which can supply any constant value (not just
    zero)
    
    Settings the default_factory to set makes the defaultdict useful for building a dictionary of sets:
"""


"""
namedtuple() Factory function for tuples with named fields

    Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can
    be sued wherever regular tuples are used, and they add the ability to access fields by name instead of position 
    index.
    
    collections.namedtuple(typename, field_names, verbose=False, rename=False)
        Return a new tuple subclass named typename. The new subclass is used to create tuple-like objects tht have 
        fields accessible by attribute lookup as well as being index-able and iterable. Instances of the subclass also 
        have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple 
        contents in a name=value format.
        
        The field_name are a single string with each fieldname separated by whitespace and /or commas, for example 'x y'
        or 'x, y'. Alternatively, field_names can be a sequences of string such as ['x', 'y'].
        
        Any valid Python identifier may be used for a fieldname except for names starting with an underscore. Valid
        identifiers consist of letters, digits, and underscores but do not start with a digit or underscore and cannot
        be a keyword such as class, for , return, global, pass, or raise.
        
        If rename is true, invalid fieldnames re automatically replaced with positional names. For example, ['abc', 
        'def', 'ghi', 'abc'] is converted to ['abc', 'def', 'ghi', '_3'], eliminating the keyword def and the duplicate 
        fieldname abc.
        
        If verbose is true, the class definition is printed after it is built. This option is outdated; instead, it is 
        simpler to print the _source attribute.
        
        Named tuple instances do not have per-instance dictionaries, so they are lightweight and require no more memory 
        than regular tuples.
        
    Named tuples are especially useful for assigning field names to result tuples returned by csv or sqlite3 modules:
"""

EmployeeRecord = namedtuple('EmplyeeRecord', 'name, age, title, department, paygrade')

for emp in map(EmployeeRecord._make, csv.reader(open("employee.csv", "rb"))):
    print(emp.name, emp.title)

conn = sqlite3.connect('/companydta')
cursor = conn.cursor()
cursor.execute('Select name, age, title, department, paygrade from employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)


"""
    In addition to the methods inherited from tuples, named tuples support three additional methods and two attributes.
    To prevent confilects with field names, the method and attribute name start with an underscore.
    
    classmethod somenamedtuple._make(iterable)
        Class method that makes a new instance from an existing sequence of iterable.
    
    somenamedtuple._asdict()
        Return a new OrderedDict which maps field names to their corresponding values:
        
    somenamedtuple._replace(**kwargs)
        Return a new instance of the named tuple replacing specified fields with new values:
        
    somenamedtuple._source
        A string with the pure Python source code used to created the named tuple class. the source makes the named
        tuple self-documenting. It can be printed, executed using exec(), or saved to a file and imported.
        
    somenamedtuple._fields
        Tuple of string listing the field names. Useful for introspection and for creating new named tuple types from 
        existing named tuples.
        
    To retrieve a field whose name is stored in a string, use the getattr() function:
    
    To convert a dictionary to a named tuple, use the double-star-operator (as described in unpacking arguments Lists):
    
    Since a named tuple is a regular Python class, it is easy to add or change functionality with a subclass, Here is 
    how to add a calculated field and a fixed-width print format:
"""


class Point(namedtuple('Point', 'x, y')):
    __slots__ = ()
    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point: x=%6.3f y=%6.3f hypot=%6.3f' % (self.x, self.y, self.hypot)


"""
    The subclass shown above sets __slots__ to an empty tuple. This helps keep memory requirements low by preventing the
    creation of instance dictionaries.
    
    Subclassing is not useful for adding new, stored fields. Instead, simply create a new anmed tuple type from the 
    _fields attribute.
    
    Docstrings can be customized by making direct assignments to the __doc__ fields:
"""


"""
OrderedDict objects

    Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted. When 
    iterating over an ordered dictionary, the items are returned in the order their keys were first added.
    
    class collections.OrderedDict([items])
        Return an instance of a dict subclass, supporting the usual dict methods. An orderedDict is a dict that 
        remembers the order that key were first inserted. If a new entry overwrites an existing entry, the original 
        insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.
        
        popitem(last=True)
            The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are 
            returned ini LIFO order if last is true or FIFO order if false.
            
        move_to_end(key, last=True)
            Move an existing key to either end of ordered dictionary. The item is moved to the right end if last is true
            (the default) or to the beginning if last is false. Raises KeyError if the key does not exist:
            
    In additional to the usual mapping methods, ordered dictionaries also support reverse iteration using reversed()
    
    Equality tests between OrderedDict objects are order-sensitive and are implemented as 
    list(od1,items())==list(od2.items()). Equality tests between OrderedDict objects and other Mapping objects are 
    order-insensitive like regular dictionaries. This allows OrderedDict objects to be substituted anywhere a regular 
    dictionary is used.
    
    The OrderedDict constructor and update() method both accept keyword arguments, but their order is lost because
    Python's function call semantics pass in keyword arguments using a regular unordered dictionary.
    
OrderedDict Examples and recipes

    Since an ordered dictionary remembers its insertion order, it can be used in conjunction with sorting to make a 
    sorted dictionary:
    
    The new sorted dictionaries maintain their sort order when entries are deleted. But when new keys are added, the 
    keys are appended to the end and teh sorted is not maintained.
    
    It is also straight-forward to create an ordered dictionary variant that remembers the order the keys were last 
    inserted. If a new entry overwrites an existing entry, the original insertion position is changed and moved to 
    the end:
"""


class LastUpdatedOrderedDict(OrderedDict):
    "Store items in the order the keys were last added"

    def __setitem__(self, key, value):
        if key  in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)


"""
    An ordered dictionary can be combined with the Counter class so that the counter remembers the order elements are 
    first encountered:
"""


class OrderedCounter(Counter, OrderedDict):
    "Counter that remembers the order elements are first encountered"

    def __repr__(self):
        return '%s(%r' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


"""
UserDict objects
    
    The class, UserDict acts as wrapper around dictionary objects. The need for this class has been partially supplanted
    by the ability to subclass directly from dict; however, this class can be easier to work with because the underlying
    dictionary is accessible as an attribute.
    
    class collections.UserDict([initialdata])
        Class that simulates a dictionary. The instance's contents are kept in a regular dictionary, which is accessible
        via the data attribute of UserDict instances. if initialdata is provided, data is initialized with its contents;
        note that a reference to initialdata will not be kept, allowing it be used for other purposes.
        
        In addition to supporting the methods and operations of mappings, UserDict instances provide the following
        attribute:
        
        data
            A real dictionary used to store the contents of UserDict class.
"""