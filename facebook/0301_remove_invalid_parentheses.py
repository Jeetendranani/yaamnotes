"""
301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contains letters other than the parentheses ( and ).

Examples:
    "()())()" -> ["()()()", "(())()"]
    "(a)())()" -> ["(a)()()", "(a())()"]
    ")(" -> [""]


Thought process
    1. We try to find out all answers for the possible solution to get the string valid with minimum deletion of '(' or
    ')'.
    2. Since it is search problem, probably we should go BFS or DFS with pruning.
    3. Fist of all we need figure out the minimum of deletion to get it valid.
    4. Go though the string to find out how many '(' need to delete and how many ')' need to delete.
    5. If we know how many characters need to be deleted, we have the idea to go DFS,
        - If number need to delete = 0, return string.
        - Find a '(' or ')'.
        - Delete it, then check the number of the ns to delete to get it valid.
            - If new number < original number then DFS new string
            - Else pruning.
    6. One more thing is about to remove duplicates. We can put the visited string to a set, If the string is already in
    set, then pruning.

Solution with DFS + pruning:
"""
import os
from queue import Queue


def remove_invalid_parentheses(s):
    def dfs(s):
        mi = calc(s)
        if mi == 0:
            return [s]

        ans = []
        for x in range(len(s)):
            if s[x] in ('(', ')'):
                ns = s[:x] + s[x+1:]
                if ns not in visited and calc(ns) < mi:
                    visited.add(ns)
                    ans.extend(dfs(ns))
        return ans

    def calc(s):
        a = b = 0
        for c in s:
            a += {'(': 1, ')': -1}.get(c, 0)
            b += a < 0
            a = max(a, 0)
        return a + b

    visited = set([s])
    return dfs(s)


"""
Depth-first search

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. One starts at the 
root (selecting some arbitrary node as the root in the case of a graph) and explores as for as possible along each 
branch before backtracking.

A version of depth-first search was investigated in the 19th century by French mathematician Charles Pierre as a 
strategy for solving mazes.

Properties
    The time and space analysis of DFS differs according to its application area. In theoretical computer science, DFS
    is typically used to traverse an entire graph, and takes time O(|V| + |E|), linear in the size of the graph. In 
    these applications it also uses space O(|V|) in the worst case to store the stack of vertices on the current 
    search path as well as the set of already-visited vertices. Thus, in this setting. the time and space bounds are 
    the same as for Breadth-first search and the choice of which of these two algorithms to use depends less on their
    complexity and more on the different properties of hte vertex orderings the two algorithms produce.
    
    For applications of DFS in relation to specific domains, such as searching for solution in artificial intelligence 
    or web-crawling, the graph to be traversed is often either too large to visit in its entirety or infinite (DFS may 
    suffer from non-termination). In such cases, search is only performed to a limited depth; due to limited resources, 
    such as memory or disk space, one typically does not use data structures to keep track of the set of all previously
    visited vertices. when search is performed to a limited depth, the time is still linear in terms of the number of 
    expanded vertices and edges ( although this number is not the same as th size of the entire graph because some 
    vertices may be searched more than once and others not al all) but the space complexity of the variant of DFS is 
    only proportional to the depth limit, and as a result, is much smaller thant the space needed for searching to the 
    same first search applies DFS repeatedly with a sequence of increasing limits. In the artificial intelligence mode 
    of analysis, with a branching factor greater than one, iterative deepening increases the running time by only a 
    constant factor over the case in which the correct depth limit is known due to the geometric growth of the number of
    nodes per level.
    DFS may also be used to collect a sample of graph nodes. However, incomplete DFS, similarly to incomplete BSF, is 
    biased towards nodes of high degree.
    
Example
For the following graph:
    A depth-first search starting at A, assuming that the left edges in the show graph are chosen before right edges, 
    and assuming the search remembers previously visited nodes and will not repeat them (since this is a small graph),
    will visit the nodes in the following order: A, B, D, F, E, C, G. The edges traversed in this search from a Tremaux 
    tree, a structure with important application in graph theory. Performing the same search without remembering 
    previously visited nodes results in visiting nodes in the order A, B, D, F, E, A, B, D, F, E, etc. forever, caught i
    n the A, B, D, F, E cycle and never reaching C or G. 
    iterative deepening is one technique to avoid this infinite loop and would reach all nodes.
    
Output of a depth-first search
    A convenient description of a depth-first search of a graph is the terms of a spanning tree of the vertices reached 
    during the search. Based on this spanning tree, the edges of the original graph can be divided into three classes:
    forward edges, which point from a node from the tree to one of its descendants, back edges, which point from a 
    node to one of its ancestors, and cross edges, which do either. Sometimes tree edges, edges which belong to the
    spanning tree itsef, are classified separately from forward edges. If the original graph is undirected then all of 
    its edges are tree edges or back edges.
    
DFS ordering
    An enumeration of the vertices of a graph is said to be a DFS ordering if ti is the possible output of the 
    application of DFS to this graph.
    
Vertex orderings
    It is also possible to use depth-first search to linearly order the vertices of a graph or tree. There are three 
    common ways of doing this:
    - A pre-ordering is a list of the vertices in the order that they were first visited by the depth-first search 
    algorithm. This is a compact and natural way of describing the progress of search. as was done earlier in this 
    article. A pre-ordering of an expression tree is the expression in Polish notation.
    -  A post-ordering 
    - A level-ordering
    
    For example, when searching the directed graph below beginning at node A, the sequence of traversals is either A B
    D B, A, C, A or A C D C A B A (choosing to first to visit B or C from A is up to the algorithm). Note that repeat 
    visits in the from of backtracking to a node, to check if it has still unvisited neighbors, are included here (even
    if it is found to have none). Thus the possible pre-orderings ar A B D C and A C D B, while the possible 
    post-orderings are D B C A and D C B A, and the possible reverse post-orderings are A C B D and A B C D.
    
    Reverse post-ordering produces a topological sorting of any directed acyclic graph. This ordering is also useful in 
    control flow analysis as it often represents a natural linearization of the control flows. The graph above might 
    represent the flow of control in the code fragment below, and it is natural to consider the code in th order A, B, 
    C, D or A, C, B, D but not natural to use the order A, B, D, C or A, C, D B.
"""


"""
Breadth-first search

Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the 
tree root (or some arbitrary node of a graph, sometimes referred to as a search key) and explores the neighbor nodes
first, before moving to the nest level neighbors.

BFS and its applications in finding connected components fo graphs were invented in 1945 by Konrad Zuse and Michael 
Burke, in there (rejected) Ph.D. thesis on the Plankalkul programming language, but this was not published until 1972. 
it was reinvented in 1959 by Edward F. Moore, who used it to find the shortest path out of maze, and later developed by
C. Y. Lee into a wire routing algorithm.

Pseudocode
Breadth first traversal is accomplished by enqueueing each level of the tree sequentially as the root of any subtree is 
encountered. There are 2 cases in the iterative algorithm.
    - Root cases: The traversal queue is initially empty so the root node must be added before the general case.
    - General cases: Process any items in the queue, while also expanding there children, stop if the queue was empty.
    The general case will halt after processing the bottom level as leaf nodes have no children.
    
    Input: A search problem. A search-problem abstract out the problem specific requirements from the actual search 
    algorithm.
    Output: An ordered list of actions to be followed to reach from start start state to the goal state.
    Below is a Python listing for a breadth first problem, where the exact nature of the problem is abstracted in the 
    problem object.
"""


def breadth_first_search(problem):
    # a FIFO open_set
    open_set = Queue()
    # an empty set to maintain visited nodes
    closed_set = set()
    # a dictionary to maintain meta information (used for path formation)
    meta = dict()

    # initialize
    root = problem.get_root()
    meta[root] = (None, None)
    open_set.enqueue(root)

    # For each node on the current level expand and process, if no children (leaf, then unwind)
    while not open_set.is_empty():
        subtree_node = open_set.dequeue()

        # We found the node we wanted so stop and emit a path
        if problem.is_goal(subtree_node):
            return construct_path(subtree_node, meta)

        # For each child of the current tree process
        for (child, action) in problem.get_successors(subtree_node):
            if child in closed_set:
                continue

            # The child is not enqueued to be processed, so enqueue this level of children to be expanded
            if child not in open_set:
                # create metadata for this nodes
                meta[child] = (subtree_node, action)
                # enqueue these nodes
                open_set.put(child)

        # We finished processing the root of the subtree, so add it to the closed set
        closed_set.add(subtree_node)

    def construct_path(state, meta):
        action_list = []

        while True:
            row = meta[state]
            if len(row) == 2:
                state = row[0]
                action = row[1]
                action_list.append(action)
            else:
                break
        return action_list.reverse()


"""
map(function, iterable, ...)
    Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable 
    arguments are passed, function must take that many arguments and is applied the items from all iterable in parallel.
    With multiple iterable, the iterator stops when the shortest iterable is exhausted. For cases where the function 
    inputs are already arranged into argument tuples, see itertools.starmap().
    
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
    Return the largest item in an iterable or the largest of two or more arguments.
    
    If one positional argument i provided, it should be the iterable, The largest item in the iterable is returned. If 
    two or more positional arguments are provided, the largest of the positional arguments is returned.
    
    There are two optional keyword-only arguments. The key argument specifies a non-argument ordering function like that
    used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If the 
    iterable is empty and the default is not provided, a ValueError is raised.
    
    if multiple items are maximal, the function returns the first one encountered. This consistent with other 
    sort-stability preserving tools such as sorted(iterable, key=keyfunc, reverse=True)[0] and heapq.nlargest(1, 
    iterable, key=keyfunc).
    
memoryview(obj)
    Return a "memory view" object created from the given argument. See Memory Views for more information.
    
min(iterable, *[, key, default])
min(arg1, arg2, %args[, key])
    Return the smallest item in an iterable or the smallest of two or more arguments.
    
    if one positional argument is provided, it should be an iterable. The smallest item in the iterable is returned. If
    two or more positional arguments are provided, the smallest of the positional arguments is returned.
    
    The are two optional keyword-only arguments. The key argument specifies a one-argument ordering function like that 
    used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If the 
    iterable is empty and the default not provided, a ValueError is raised.
    
    If multiple items ar minimal, the function returns the first one encountered. This is consistent with other 
    sort-stability preserving tools such as sorted(iterable, key=keyfunc)[0] and heapq.nsmallest[1, iterable, 
    key=keyfunc).
    
next(iterator[, default])
    Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if 
    the iterator is exhausted, otherwise StopIteration is raised.
    
class object
    Return a new featureless object. object is base for all classes. It has the methods that are common to all instances
    of Python classes. This function does not accept any arguments.
    
    Note: object does not have a __dict__, so you can't assign arbitrary attributes to an instance of the object class.
    
oct(x)
    Convert an integer number to an octal string prefixed with "0o". The result is a valid Python expression. If x is 
    not a Python int object, it has to define an __index__() method that returns an integer. For example:
    
    If you want to convert an integer number to octal string either with prefix "0o" or not, you can use either of the 
    following ways.
    >>> format(10 , '#o'), format(10, 'o)
    also see format() for more information.
    
open(file, mode='r', buffering=-1, encoding=None, error=None, newline=None, closedfd=True, opener=None)
    Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised.
    
    file is a path-like object giving the pathname (absolute or relative to the current working directory) of the file 
    to be opened or an integer file descriptor of the file to be wrapped. (if a file descriptor is given, it is closed 
    when the returned I/O object is closed, unless closedfd is set to False.)
    
    Mode is an optional string that specifies the mode in which the file is opened. It defaults to 'r' which means open 
    file reading in text mode. Other common values are 'w' for writing (truncating the file if it is already exists), 
    'x' for exclusive creation and 'a' for appending (which on some Unix Systems, means that all writes append to the 
    end of the file regardless of the current seek position). In text mode, if encoding is not specified the encoding 
    used is platform dependent: local.getpreferredencoding(False) is called to ge the current locale encoding. (For 
    reading and writing raw bytes use binary mode and leave encoding unspecified.) The available modes are:
        'r'     open for reading (default)
        'w'     open for writing, truncating the file first
        'x'     open for exclusive creation, failing if the file already exists
        'a'     open for writing, appending to the end of the file if it exists
        'b'     binary mode
        't'     text mode (default)
        '+'     open a disk file for updating (reading and writing)
        'U'     universal newlines mode (deprecated)
        
    The default mode is 'r' (open for reading text, synonym of 'rt'). For binary read-write access, the mode 'w+b' open 
    and truncates the file to 0 bytes. 'r+b' open the file without truncation.
    
    As mentioned in the Overview, Python distinguishes between binary and text I/O. Files opened in binary mode (
    including 'b' in the mode argument) return contents as bytes objects without any decoding. In text mode (The 
    default, or when 't' is included in the mode argument), the contents of the file are returned as str, the bytes 
    having been first using a platform-dependent encoding or using the specified encoding if given.
    
    Note: Python doesn't depend on th underlying operating system's notion of text files; all the processing is done by 
    Python itself, and is therefore platform-independent.
    
    buffering is an optional integer used to set the buffering policy. Pass 0 to switch buffering off (only allowed in 
    binary mode), 1 to select line buffering (only usable in text mode), and an integer > 1 to indicate the size in 
    bytes of a fixed-size chunk bugger. When no buffering argument is given, the default buffering policy works as 
    follows:
        - binary fies are buffered in fixed-size chunks; the size of the buffer is chosen using a heuristic truing to 
        determine the underlying device's "block size" and falling back on io.DEFAULT_BUFFER_SIZE. On many systems, the
        buffer will typically be 4096 or 8192 bytes long.
        - "Interactive" text fies (files for which isatty() return True) use line buffering. Other text files use the 
        policy described above for binary files.
        
    Encoding is the name of the encoding used to decode or encode the file. This should only be used in text mode. The
    default encoding is platform dependent (whatever locale.getpreferredencoding() returns), but any text encoding 
    supported by Python can be used. See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to be handled - this cannot be used in binary 
    mode. A variety of standard error handlers are available (listed under Error Handlers), though any error handling 
    name that has been registered with codes.register_error() is also valid. The standard names include:
        - 'strict'          to raise aValueError exception if there is an encoding error. The default value of None has 
                            the same effect.
        - 'ignore'          ignore errors. Note that ignoring encoding errors can lead to data loss.
        - 'replace'         causes a replacement marker (such as '?') to be inserted where there is malformed data.
        - 'surrogateescape' will represent any incorrect bytes as code points in the Unicode Private Use Area ranging 
                            from U+DC80 to U+DCFF. This private code points will then be turned back into the same types
                            when the surrogateescape error handler is used when writing dta. This is useful for 
                            processing files in an unknown encoding.
        - 'xmlcharrefreplace'   is only supported when writing to a file. Characters not supported by the encoding are 
                            replaced with the appropriate XML character reference &#nnn;
        - 'backslashreplace' replaces malformed data by Python's back-slashed escape sequences.
        - 'namereplace' ( also only supported when writing) replaces unsupported characters with \N{...} escape 
                            sequences.
                            
    newline controls how universal newlines mode works (it only applies to text mode). It can be None, '', '\n', '\r',
    and '\r\n'. It works we follows:
    - When reading input from the stream, if newline is None, universal newline is enabled. Lines in the input can end 
    in '\n', '\r', or '\r\n', and these are translated into '\n' before being returned to the caller. If it is '', 
    universal newlines mode is enabled, but line endings are returned to teh caller untranslated. If it has any of the 
    other legal values, input lines are only terminated by the given string, and the line ending is returned to the 
    caller untranslated.
    - when writing output to the stream, if newline is None, any '\n' characters written are translated to the system 
    default line separator, os.linesep. if newline is '' or '\n', no translation takes place. If newline is any of the 
    other legal values, any '\n' characters written are translated to the given string.
    
    if closedfd is False and the file descriptor rather than a filename was given, the underlying file descriptor will 
    be kept open when the file is closed. if a filename is given closefd must be True (the default) otherwise an error 
    will be raised.
    
    a custom opener can be used by passing a callable as opener. The underlying file descriptor for the file object is 
    then obtained by calling opener with (file, flags). opener must return an open file descriptor (passign os.open as 
    opener results in functionality similar to passing None).
    
    The newly created created file is non-inheritable.
    
    The following example used the dir_fd parameter of the os.open() function to opoen a file relative to a given 
    directory: 
"""

dir_fd = os.open('somedir', os.O_RDONLY)


def opener(path, flags):
    return os.open(path, flags, dir_fd=dir_fd)


with open('spanmspam.txt', 'w', opener=opener) as f:
    print('This will be written to somedir/spamspam.txt', file=f)

os.close(dir_fd)


"""
    The type of file object returned by the open() function depends on the mode. When open() is used to open a file in a 
    text mode ('w', 'r', 'wt', 'rt', etc), it returns a subclass of io.TextIOBase (specifically io.TextIOWrapper). When
    used to open a file in a binary mode with buffering, the returned class is a subclass of io.BufferedIOBase. The 
    exact varies: in read binary mode, it returns an io.BufferedReader; in write binary and append binary modes, it 
    return an io.BufferedWriter, and in read/write mode, it returns an io.BufferedRandom. When buffering is disabled, 
    the raw stream, a subclass of io.RawIOBase, io.FileIO, is returned.
    
    See also the file handling modules, such as fileinput, io (where open() is declared), os , os.path, tempfile, and 
    shutil.
    
ord(c)
    Given a string representing one unicode character, return an integer representing the Unicode code point of that
    character. For example, ord('a') returns the integer 97 and ord('€') (Euro Sign) returns 8364. This is the inverse 
    of chr().
    
pow(x, y[, z])
    Return x to the power y; if z present, return x to the power y, module z (computed more efficiently than 
    pow(x, y) % z). The two-argument from pow(x, y) is equivalent to using the power operator:
    x**y.
    
    the arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators
    apply. for int operands, the result has the same type as teh operands (after coercion) unless the second argument is
    negative; in that case, all arguments are converted to float and a float result is delivered. For example, 10**-2
    returns 0.01. If the second argument is negative, the third argument must be omitted. If z is present, x and y must 
    be of integer types, and y must be non-negative.
    
print(*objects, sep='', end='\n', file=sys.stdout, flush=False)
    Print objcets to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, 
    must be given as keyword arguments.
    
    All non-keyword arguments are converted to strings like str() does and written to teh stream, separated by sep and 
    following by end. both sep and end must be strings; they can also be None, which means to use hte default values. If
    no objects are given, print() will just write end.
    
    The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be 
    used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. 
    For these, use file.write(...) instead.
    
    Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is 
    forcibly flushed.
    
class property(fget=None, fset=None, fdel=None, doc=None)
    Return a property attribute.
    fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a f
    unction for deleting an attribute value. And doc creates a docstring for the attribute.
    
    A typical use is to define a managed attribute x:
"""


class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the x property")


"""
    If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.
    If given, doc will be the docstring fo the property attribute. Otherwise, the property will copy fget's docstring
    (if it exists). This makes it possible to create read-only properties easily using property() as a decorator:
"""


class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """ Get the current voltage. """
        return self._voltage


"""
    The property decorator turns the voltage() method into a "getter" for a read-only attribute with same name, and it 
    sets the docstring for voltage to "Get the current voltage."
    
    A property object has getter, setter, and deleter methods usable as decorators that create a copy of hte property 
    with the corresponding accessor function set to teh decorated function. This is the best explained with an example:
"""


class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """ I'm the 'x' property. """
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


"""
    This code is exactly equivalent to the first example. Be sure to give the additional functions the same name as the 
    original property (x, in this case)
    
    The returned property object also has the attributes fget, fset, gdel corresponding to the constructor arguments.
    
range(stop)
    range(start, stop[, step])
    Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence 
    Types - list, tuple, range.
    
repr(object)
    Return a string containning a printable representation of an object, For many types, this function makes an attempt 
    to return a string that would yield an object with the same value when passed to eval(), otherwise the 
    representation is a string enclosed in angle brackets that contains the name of the type of the object together
    with additional information often including the name and address of the object. A class can control what this 
    function returns for its instances by defining a __repr__() method.
-
"""