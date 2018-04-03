"""
340. Longest Substring with At most K distinct characters

Given a string, find the length of the longest substring T that contains at most K distinct characters.

For examples, Given s = "eceba" and k = 2,

T is "ece" which its length is 3.
"""


class Solution:
    def length_of_longest_substring_k_distinct(self, s, k):
        cmap = {}
        slow, fast, maxlen = 0, 0, 0
        while fast < len(s):
            cmap[s[fast]] = cmap.get(s[fast]) + 1
            fast += 1
            while len(cmap) > k:
                if s[slow] in cmap.keys():
                    cmap[s[slow]] = cmap.get(s[slow], 0) - 1
                if cmap[s[slow]] < 1:
                    del cmap[s[slow]]
                slow += 1
            maxlen = max(maxlen, sum(cmap.values()))

        return maxlen


"""
ascii(object)
    As repr(), return a string containing a printable representation of an object, but escape the non-ascii characters
    in the string returned by repr() using \x, \u or \U escapes. This generates a string similar to that returned by
    repr() in Python 2.
    
bin(x)
    Convert an integer number to a binary string. The result is a valid Python expression. If x is not a Python int 
    object, it has to define an __index__() method that returns an integer.
    
class bool([x]) 
    Return a boolean value, i.e. one of True of False. x is converted using the standard truth testing 
    procedure. if x is false or omitted, this return False; otherwise it returns True. The bool class is a subclass of 
    int (see Numeric Types - int, float, complex). It can not sub classed further. Its only instances are False and 
    True (see Boolean Values).
    
class bytearray([source[, encoding[, errors]]])
    Return a new array of bytes. The byterarray class is a mutable sequence of integers in the range 0 <= x < 256. it 
    has most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods
    that the bytes type has, see Bytes and Byterarray Operations.
    
    The optional source parameter can be used to initialize the array in a few different ways:
         - If it is a string, you must also give the encoding (and optionally, errors) parameters; bytearray() then  
         converts the string to bytes using str.encode().
         - If it is an integer, the array will have that size and will be initialized with null bytes.
         - If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to 
         initialized the bytes array.
         - If it is an iterable, it must be a iterable of integers in the range 0 <= x < 256, which are sued as the 
         initial contents of the array.
         
    Without an argument, an array of size 0 created.
    
    See also Binary Sequence types - bytes, bytearray, memoryview and bytearray objects.
    
class bytes([source[, encoding[, errors]]])
    Return a new "bytes" object, which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an 
    immutable version of bytearray - it has the same non-mutating methods and the same indexing and slicing behavior.
    
    Accordingly, constructor arguments are interpreted as for bytearray()
    
    Bytes object can also be created with literals, see String and Bytes literals.
    
    See also Binary Sequence Types - bytes, bytearray, memoryview, bytes, and bytes and bytearray operations.
    
callable(object)
    Return True if the object argument appears callable, False if not. if this return true, it is still possible that
    a call fails, but if it is false, calling object will never succeed. Note that classes are callable (calling a 
    class returns a new instance); instances are callable if their class has a __call__() method.
    
chr(i)
    Return the string representing a character whose Unicode code point is the integer i. For example, char(97) returns
    the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord(). 
    
    The valid range for the argument is from 0 through 1, 114, 111 (0x10FFFF in base 16). ValueError will be raised if
    i is outside that range.
    
classmethod(function)
    Return a class method for function.
    
    A class method receives the class as implicit first argument, just like an instance method receives the instance. 
    To declare a class method, use this idiom:
    
    class C:
        @classmethod
        def f(cls, arg1, arg2, ...): ...
        
    The @classmethod form is a function decorator - see the description of function definitions in Function Definitions
    for details.
    
    It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored 
    except for its class. if a class method is called for a derived class, the derived class object is passed as the 
    implied first argument. 
    
    Class methods ara different than C++ or Java static methods. If you want those, see staticmethod() in this section.
    
    For more information on class methods, consult the documentation on the standard type hierarchy in The Standard type
    hierarchy.
    
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
    Compile the source into a code or AST object. Code objects can be executed by exec() or eval(). Source can either 
    be a normal string, a byte string, or an AST object. Refer to the ast module documentation for information on how
    to work with AST objects.
    
    The filename argument should give the file from which the code was read; pass some recognizable value if it wasn't 
    read from a file ('<string>' is commonly used.)
    
    The mode argument specifies what kind of code must be compiled; it can be 'exec' if source consists of a sequence 
    of statements, 'eval' if it consists of a single expression. or 'single' if it consists of a single interactive 
    statement (in the latter case, expression statements that evaluate to something other than None will be printed).
    
    The optional arguments flags and dont_inherit control with future statements (see pep236) affect the compilation 
    of source. If neither is present (or both are zero) the code is compiled with those future statements that are in
    effect in the code that is calling compile(). If the flags argument is given and dont_inherit is not (or is zero)
    then the future statements specified by the flags argument are sued in addition to those what would be used anyway.
    if dont_inherit is a non-zero integer than the flags argument is it - the future statements in effect around the 
    call to compile are ignored. 
    
    Future statements are specified by bits which can be bitwise Ored together to specify multiple statements. The 
    bitfield required to specify a given feature can be found as the compiler_flag attribute on the _Feature instance 
    in the __future__ module.
    
    The argument optimize specifies the optimization level of the compiler; the default value of -1 selects the 
    optimization level of the interpreter as given by -O options. Explicit levels are 0 (no optimization; __debug__ is
    true), 1 (asserts are removed, __debug__ is false) or 2 (docstrings are removed too).
    
    This function raise SyntaxError if the compiled source is invalid, and ValueError if the source contains null bytes.
    
    If you want to parse python code into its AST representation, see ats.parse().
    
    Note: When compiling a string with multi-line code in 'single' or 'eval' node, input must be terminated by at least 
    one newline character. This is to facilitate detection of incomplete and complete statements in the code module.
    
class complex([real[, imag]])
    Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the 
    first parameter is a string, it will be interpreted as a complex number and the function must be called without a 
    second parameter. The second parameter can never be a string. Each argument may be any numeric type (including 
    complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and 
    float. If both arguments are omitted, returns 0J.
    
    Note: When converting from a string, the string must not contain whitespace around the central + and - operator. 
    For example, complex('1+2j') is fine, but complex('1 + 2j') raise ValueError.
    
    The complex type is described in Numeric Types - int, float, complex.
    
delattr(object, name)
    This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of 
    the object's attributes. The function deletes the named attribute, provided the project allows it. For example, 
    delattr(x, 'footbar') is equivalent del x.foobar.
    
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
    Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types - dict for 
    documentation about this class.
    
    For other containers see the built-in list, set, and tuple class, as well as the collections module.
    
dir([object])
    Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list
    of valid attributes for that object.
    
    If the object has a method named __dir__(), this method will be called and must return the list of attributes. This
    allows objects that implement a custom __getattr__() or __getattribute__() function to customize the way dir()
    reports their attributes.
    
    If the object does not provide __dir__(), the function tries its best to gather information from the object's 
    __dict__ attribute, if defined, and from its type object. The resulting list is not necessarily complete, and 
    may be inaccurate when the object has a custom __getattr__().
    
    The default dir() mechanism behaves differently with different types of objects. as it attempts to produce the most 
    relevant, rather than complete, information:
        - If the object is a module object, the list contains the name of the module's attributes.
        - If the object is a type or class object, the list contains the names of its attributes, and recursively of
        the attributes of its bases.
        - otherwise the list contains the object's attributes' names, the names of the class's attributes, and 
        recursively of the attributes of its class's base classes.
        
    The resulting list is sorted alphabetically. 
    
    Note: Because dir() is supplied primarily as a convenience for use at an interactive prompt, it tries to supply an
    interesting set of names more than it tries to supply a rigorously or consistently defined set of names, and its
    detailed behavior may change across releases. For example, metaclass attributes are not in the result list when the 
    argument is a class.
    
divmod(a, b)
    Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder
    when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For 
    integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b), where q is 
    usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very closed to a, if a % b is 
    non-zero it has the same sign as b, and 0 <= abs(a % b). 
    
enumerate(iterable, start=0)
    Return an enumerate object. iterable must be sequence, an iterator, or some other object which supports iteration. 
    The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from stat which 
    default to 0) and the values obtained from iterating over iterable.
    
    Equivalent to:
    
    def enumerate(sequence, start=0):
        n = start
        for elem in sequence:
            yield n, elem
            n += 1
            
eval(expression, globals=None, locals=None)
    The arguments are string and optional globals an locals. If provided, globals must be a dictionary, if provided, 
    local can be any mapping object.
    
    The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) 
    using the globals and locals dictionaries as local namespace. If the globals dictionary is present and lacks 
    '__builtins__', the current globals are copied into globals before expression is parsed. This means that expression
    normally has full access to the standard builtins module and restricted environments are propagated. If the locals
    dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is 
    executed in the environment where eval() is called. the return value is the result of the evaluated expression. 
    Syntax errors are reported as exceptions. 
    
    This function can also be sued to execute arbitrary code objects (such as those created by compile()). In this case
    pass a code object instead of a string. If the code object has been compiled with 'exec' as the mode argument, 
    eval()'s return value will be None.
    
    Hints: dynamic execution of statements is supported by the exec() function. The globals() and locals() functions 
    returns the current global and local dictionary, respectively which may be useful to pass around for use eval() or
    exec().
    
    See ast.literal_eval() for a function that can safely evaluate strings with expressions containing only literals.
    
exec(object[, globals[, locals]]])
    This function supports dynamic execution of Python code. object must be either a string or a code object. If it is 
    a string, the string is parse as a suite of python statements which is then executed (unless a syntax error occurs).
    If it is a code object, it is simply executed. In all cases, the code that's executed is expected to be valid the
    file input (see the section "File input" in the Reference Manual). Be aware that the return and yield statements may
    not be used outside of function definitions even with in the context of code passed to the exec() function. The 
    return value is None.
    
    In all cases, if th optional parts are omitted, the code is executed in the current scope. If only globals is 
    provided, it must be a dictionary, which be sued for both the global and the local variables. If globals and locals 
    are given, they are sued for the globals and locals variables, respectively. If provided, locals can be any mapping
    object. Remember that at module level, globals and locals are the same dictionary. If exec gets two separate objects
    as global and locals, the code will be executed as if it where embedded in a class definition.
    
    If the globals dictionary does not contain a value for the key __builtins__, a reference to the dictionary of the 
    built-in module builtins is inserted under that key. That way you can control what builtins are available to the 
    executed code by inserting your own __builtins__ dictionary into globals before passing it to exec().
    
    Note: The built-in functions globals() and locals() return the current global and local dictionary, respectively, 
    which may be useful to pass around for use as the second and third argument to exec().
    
    Note: The default locals act as described for function locals() below: modifications to the default locals 
    dictionary should not be attempted. Pass an explicit locals dictionary if you need to see effects of the code on 
    locals after function exec() returns.
    
filter(function, iterable)
    construct an iterator form those elements from iterable for which function returns true. iterable may be either a 
    sequence, a container which supports iteration, or an iterator. If function is None, the identity function is
    assumed, that is, all element of iterable that are false are removed.
    
    Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if 
    function(item)) if function is not None and (item for item in iterable if item) if function is None.
    
    See itertools.filterfalse() for the complementary function that returns elements of iterable for which function
    returns false.
    
class float([x])
    Return a floating point number constructed from a number of sting x.
    
    If the argument is a string, it should contains a decimal number, optionally preceded by a sign, and optionally 
    embedded in whitespace. The optional sign may be '+' or '-'; a '+' sign has no effect on the value produced. The 
    argument may also be a string representing a NaN (not a number), or a positive or negative infinity. More precisely,
    the input must conform to the following grammar after leading and trailing whitespace characters are removed:
    
    Here floatnumber is the form of Python floating-point literal, described in Floating point literals. Case is not 
    significant, so for example, 'inf', 'Inf', 'INFINITY', and 'iNfINity' are all acceptable spellings for positive 
    infinity.
    
    Otherwise, if the argument is an integer or a floating point number, a floating point number with the same value (
    within Python's floating point precision) is returned. If the argument is outside the range of a Python float, an 
    OverflowError will be raised.
    
    For a general Python object x, float(x) delegates to x.__float__().
    
    If no argument is given, 0.0 is returned.
    
    The float type is described in Numeric Types - int, float, complex.
    
format(value[, format_spec])
    Convert a value to a "formatted" representation, as controlled by format_spec. The interpretation of format_spec 
    will depend on the type of the value argument, however there is a standard formatting syntax that is used by most
    built-in types: Format Specification Mini-Language.
    
    The default format_spec is an empty string which usually gives the same effect as calling str(value).
    
    A call to format(value, format_spec) is translated to type(value).__format__(value, format_spec) which bypasses the
    instance dictionary when searching for the value's __format__() method. A TypeError exception is raised if the 
    method search reaches object and the format_spec is non-empty, or if either the format_spec or the return value are
    not strings.
    
class frozenset([iterable])
    Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class, See
    frozenset and Set types - set, frozenset for documentation about this class.
    
getattr(object, name[, default])
    Return the value of the named attribute of object. name must be a string. If the string is the name of one of the
    object's attribute. for example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not 
    exist, default is returned if provided, otherwise AttributeError is raised.
    
globals()
    Return a dictionary representing the current global symbol table. This is always the dictionary of the current 
    module (inside a function or method, this is the module where it is defined, not the module from  which it is 
    called). 
    
hasattr(object, name)
    The argument are an object and a string. The result is True if the string is the name of one of the object's 
    attributes, False if not. (This is implemented by calling getattr(object, name) and see whether it raise an 
    AttributeError no not.)
    
hash(object)
    Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare 
    dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if 
    they are of different types, as is the case for 1 and 1.0)
    
    Note: For objects with custom __hash__() methods, note that hash() truncates the return value based on the bit
    width of the host machine. see __hash__() for details.
    
help([object])
    Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the 
    interactive help system starts on the interpreter console. If the argument is a string, then the string is looked
    up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed
    on the console. if the argument is any other kind of object, a help page on the object is generated.
    
    This function is added to the built-in namespace by the site module.
    
hex(x)
    Convert an integer number to a lowercase hexadecimal string prefixed with '0x'.
    
    if x is not a python int object, it has to have __index__() method that returns an integer.
    
    See also int() for converting a hexadecimal string to a integer using a base of 16.

id(object)
    Return the 'identify' of an object. This is an integer which is guaranteed to be unique and constant for this object
    during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
    
    CPython implementation detail: This is the address of the object in memory.
    
input([prompt])
    If the prompt argument is present, it is written to standard output without a trailing newline. The function then 
    reads a line from input, converts it to a string (stripping a trailing newline), and returns that. when EOF is read
    EOFError is raised. 
    if the readline module was loaded, then input() will use it to provide elaborate line editing and history features.
    
class int(x=0)
class int(x, base=10)
    Return an integer object constructed from a number of string x, or return 0 if no arguments are given. If x is a
    number, return x.__int__(). For floating point numbers, this truncates towards zero. 
    
    If x is not a number or if base is given, then x must be a string. bytes, or bytearray instance representing an 
    integer literal in radix base. Optionally, the literal can be preceded by + or - (with no space in between) and 
    surrounded by whitespace. A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values
    10 to 35. The default base is 10. The allowed values are 0 and 2-36. Base-2, base-8, and base-16 literals can be 
    optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code. Base 0 means to interpret 
    exactly as code literal, so that actual base is 2, 8, 10 and 16, and so tht int('010', 0) is not legal, while 
    int('010') is as well as int('010', 8).
    
isinstance(object, classinfo)
    Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual)
    subclass thereof. If object is not an object of the given type, the function always returns false. If classinfo is
    a tuple of type objects (or recursively, other such tuples), return true if object is an instance of any of the 
    types. If classinfo is not type or tuple of types and such tuples, a TypeError exception is raised.
    
issubclass(object, classinfo)
    Return true if class is subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of 
    itself. classinfo may be a tuple of class objects, in which case every entry is classinfo will be checked. In any
    other case, a TypeError exception is raised.
    
iter(object[, sentinel])
    Return an iterator object. The first argument is interpreted very differently depending on the presence of the 
    second argument. Without a second argument, object must be a collection object which supports the iteration 
    protocol (the __iter__() method), or it must support the sequence protocol ( the __getitem__() method with integer 
    argument starting at 0). If it does not support either of those protocols, TypeError is raised. If the second 
    argument, sentinel , is given, then object must be a callable object. The iterator created in this case will call
    object with no arguments for each  call to its __next__() method; If the value returned is equal to sentinel, 
    StopIteration will be raised, otherwise the value will be returned.
    
    One useful application of the second form of iter() is read lines of a file until a certain line is reached. The 
    following example reds a file until the readline() method returns an empty string;
    
    with open('myfile.txt') as fp:
        for line in iter(fp.readline, '')
            process_line(line)
            
len(s)
    Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, 
    tuple, list, or range) or a collection (such as dictionary, set, or frozenset).
    
class list([iterable])
    Rather than being a function, list is actually a mutable sequence type.
    
locals()
    Update and return a dictionary representing the current local symbol table. Free variables are returned by locals()
    when it is called in function blocks, but not in class blocks.
        
    Note: The contents of this dictionary should not be modified; changes may not affect the values of local and free 
    variables used by the interpreter.
    
map(function, iterable, ...)
    Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable 
    arguments are passed, function must take that many arguments and it applied to the items from all iterables in 
    parallel. With multiple iterables, the iterator stops when the shortest iterables in exhausted. For cases where 
    the function inputs are already arranged into arguments tuples, see itertools.startmap()
    
max(iterable, *[, key, default])
max(arg1, arg2, *arg[, key])
    Return the largest item in an iterable or the largest of two or more arguments.
    
    If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned. If 
    two or more positional arguments are provided, the largest of the positional arguments is returned.
    
    There are two optional keyword-only arguments, The key argument specifies a one-argument ordering function like 
    that used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If
    the iterable is empty and default is not provided, a ValueError is raised.
    
    If multiple items are maximal, the function returns the first one  encountered. This is consistent with other 
    sort-stability preserving tools such as sorted(iterable, key=keyfunc, reverse=True)[0] and heapq.nlargest(1, 
    iterable, key=keyfunc).
    
memoryview(obj)
    Return a "memory view" object created from the given argument. See Memory Views for more information.
    
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
    Return the smallest item in an iterable or the smallest of two or more arguments.
    
    If one positional argument is provided, it should be an iterable. The smallest item in the iterable is returned. If
    two or more positional are provided, the smallest of the positional arguments is returned.
    
    There are two optional keyword-only arguments. The key arguments specifies a one-argument ordering function like
    used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If the 
    iterable is empty and default not provided, a ValueError is raised.
    
    If multiple items are minimal, the function returns the first one encountered. This is consistent with other 
    sort-stability preserving tools such as sorted(iterable, key=funckey)[0] and heapq.nsmallest(1, iterable, 
    key=funckey).
    
next(iterator[, default])
    Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if 
    the iterator is exhausted, otherwise StopIteration is raised.
    
class object
    Return a new featureless object. object is a base for all classes. It has the methods that are common to all 
    instances of Python classes. This function does not accept any arguments.
    
    Note: object does not have a __dict__, so you can't assign arbitrary attributes to an instance of the object class.
    
oct(x)
    Convert an integer number to an octal string. The result is a valid Python expression. if x is not a Python int 
    object, it has to define an __index__() method that returns an integer.
    
open(file, mode='r', bufferting=-1, encoding=None, errors=None, newline=None, closedfd=True, opener=None)
    Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised.
    
    file is either a string or bytes object giving the pathname (absolute or relative to the current working directory)
    of the file to be opened or an integer file descriptor of the file to be wrapped. (if a file descriptor is given, 
    it is closed when the returned I/O object is closed, unless closefd is set to False.)
    
    Mode is an optional string that specifies the mode in which the file is opened. It defaults to 'r' which means open 
    for reading in text mode. Other common values are 'w' for writing (truncating the file if it already exists), 'x' 
    for exclusive creation and 'a' for appending (which on some Unix systems, means that all writes append to the end of 
    the file regardless the current seek position). In text mode, if encoding is not specified the encoding used is 
    platform dependent: locale.getpreferredencodign(False) is called to get the current local encoding. (For reading 
    and writing raw bytes use binary mode and leave encoding unspecified.) The available modes are:
    'r'     open for reading (default)
    'w'     open for writing, truncating the file first
    'x'     open for exclusive creation, failing if the file already exists
    'a'     open for writing, appending to the end of the file if it exists
    'b'     binary mode
    't'     text mode (default)
    '+'     open a disk file for updating (reading and writing)
    'U'     universal newlines mode (deprecated)
    
    The default mode is 'r' (open for reading text, synonym of 'rt'). For binary read-write access, the mode 'w+b' open
    and truncates the file to 0 bytes. 'r+b' opens the file without truncation.
    
    As mentioned in the Overview, Python distinguishes between binary and text I/O. Files opened in binary mode 
    (including 'b' in the mode argument) return contents as bytes objects without any decoding. In text mode (the 
    default, or when 't' is included in the mode argument), the contents of hte file are returned as str, hte bytes 
    having been first decoded usign a platform-dependent encoding or using the specified encoding if given.
    
    Note: Python doesn't depend on the underlying operating system's notion of text files; all the processing is done by
    Python itself, and is therefore platform-independent.
    
    buffering is an optional integer used to set the buffering policy, pass 0 to switch buffering off (only allowed in 
    binary mode), 1 to select line buffering (only usable in text mode), and an integer > 1 to indicate the size in 
    bytes of a fixed-size chunk buffer. When no buffering argument is given, the default buffering policy works as 
    follows:
        
        - Binary files are buffered in fixed-size chunks; the size of the buffer is chosen using a heuristic trying to
        determine the underlying device's "block size" and falling back on io.DEFAULT_BUFFER_SIZE. on many systems, the 
        buffer will typically be 4096 or 8192 bytes long.
        - "interactive" text file (files for which isatty() returns True) use line buffering. Other text files use the 
        policy described above for binary files.
    
    encoding is the name of the encoding used to decode or encode the file. This should only be used in text mode. The
    default encoding is platform dependent (whatever local.getpregerredencoding() returns), though any error handling
    name that has been registered with codecs.register_error() is also valid. The standard name include:
"""