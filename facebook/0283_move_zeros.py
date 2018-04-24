"""
283 Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
    1. You must do this in-place without making a copy of the array.
    2. Minimize the total number of operations.

Thinking process:
1. It is a unsorted array, so at least we need O(n) time to check the element. We need loop through all elements:
    - From left to right
        The problem is after we move current one we need to check the current position again, because we move its right
        to current position. From right to left doesn't have this problem. So we choose from right to left.
    - From right to left
        Scan from right side if found 0 , then move all elements at its right to left by 1, put 0 to the last position.
        And move on.
2. How about nums is None or nums doesn't have anything. We don't need to do anything. just return nums.

Solution:
If nums is None or nums is empty. then return nums.
Else scan nums from right to left, when find 0, move all elements at its right then put 0 to the last position.
"""


def move_zeroes(nums):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    :param nums:
    :return:
    """
    if nums is None or len(nums) == 0:
        return nums

    for i in range(len(nums)-1, -1 , -1):
        if nums[i] == 0:
            for j in range(i+1, len(nums)):
                nums[j-1] = nums[j]
            nums[-1] = 0


"""
Solution 2:

This question comes under a broad category of "Array Transformation". Thi category is the meet of tech interview. Mostly
because arrays are such a simple and easy to use data structure. Traversal or representation doesn't require any 
boilerplate code and most of your code will look like the Pseudocode itself.
The 2 requirements of the questions are:
    1. Move all teh 0's to the end of array.
    2. All the non-zero elements must retain their original order.
it's good to realize here that both the requirements are mutually exclusive, i.e., You can solve the individual sub
leetcode and then combine them for teh final solution.

To reduce its Time complexity, we create an new array to store the result, just put the non-zero one instead. Then 
copy the ans back to the nums.
"""


def move_zeroes1(nums):
    res = [0] * len(nums)
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            res[j] = nums[i]
            j += 1
    for i in range(len(nums)):
        nums[i] = res[i]


"""
Solution 3:

This approach works the same way as above, i.e., first fulfills one requirement and then another. The catch? It does it 
in a clever way. The above problem can also be stated in alternate way, "Bring all the non 0 elements to the front of 
array keeping their relative order same".

This is a 2 pointer approach. The fast pointer which is denoted by variable "cur" does the job of processing new 
elements. If the newly found element is not a 0, we record it just after the last found non-0 element. The position of 
last found non-0 element is denoted by the slow pointer "lastNonZeroFoundAt" variable. As we keep finding new non-0 
elements, we just override them at the "lastNonZeroFound+1'th index. This overwrite will not result in any loss of data 
becuase we already processed what ws there (if it were non-0, it already is now written at it's corresponding index, or 
if it were 0 it will be handled later in time).

After the "cur" index reaches the end of array, we now know that all the non-0 elements have been moved to beginning of 
array in their original order. Now comes the time to fulfil other requirements, "Move all 0's to the end". We now 
simply need to fill all the index after "lastNoneZeroFoundAt" index with 0.
"""


def move_zeroes2(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param nums:
    :return:
    """

    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0


"""
Solution 4:

the total number of operations of the previous approach is sub-optimal. For example, the array which has all (except
last) leading zeroes: [0, 0, 0, ... 0, 1]. How many write operations to the array? for the previous approach, it writes
0's n-1 times, which is not necessary. We could have instead written just once? How? ... By only fixing the non-0 
element, i.e. 1.
The optimal approach is agian a subtle extension of above solution. A simple realization is if the current element is 
non-0, it's correct position can at best be it's current position or a position earlier. If it' the latter one. The 
current position will be eventually occupied by a non-0, or a 0, which lies at teh index greater then 'cur' index. We 
fill the current position by 0 right away, so that unlike the previous solution, we don't need to come back here in 
next iteration.

In order words, the code will maintain the following invariant:
    1. All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.
    2. All elements between teh current and slow pointer are zeroes
    
Therefore, when we encounter a non-zero element, we need to swap elements pointed by current and slow pointer, then 
advance both pointers. If it's zero element, we just advance current pointer.
With this invariant in-place, it's easy to see that the algorithm will work.
"""


def move_zero3(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param nums:
    :return:
    """
    slow = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[slow] = nums[slow], nums[i]
            slow += 1


"""
Built-in Functions:
abs(x)

all(iterable)

any(iterable)

ascii(object)
    as repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters
    in the string returned by repr() using \x, \u or \U escapes. This generate a string similar to that returned by 
    repr() in Python 2.
    
bin(x)
    Convert an integer number to a binary string prefixed with "0b". The result is a valid Python expression. If x is 
    not a Python int object, it has to define an __index__() method that returns an integer. Some examples:
    if prefix "0b" is desired or not, you can use either of the following ways.
    format(14, '#b'), format(14, 'b')
    
class bool([x])
    
class bytearray([source[, encoding[, errors]]])
    Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256. It
    has most of the usual methods of mutable sequences, described iin Mutable Sequence Types, as well as most methods 
    that the bytes type has, see Bytes and Bytearray Operations.
    
    The optional source parameters can be used to initialize the array in a few different ways:
        - If it is a string, you must also give the encoding (and optionally, errors) parameters; bytearray() then 
        converts the string to bytes using str.encode()
        - If it is a integer, the array will have that size and will be initialized with null bytes.
        - If it is a object conforming to the buffer interface, a read-only buffer of the object will be used to 
        initialize the bytes array.
        - If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the 
        initial contents of the array.
    
    Without an argument, an array of size 0 is created.
    
class bytes([source[, encoding[, errors]]])
    Return a new "bytes" object, which is an immutable sequence of integers in teh range 0 <= x < 256. bytes is an 
    immutable version of bytearray - it has the same non-mutating methods nd teh same indexing and slicing behavior.
    Accordingly, constructor arguments are interpreted as for bytearray().
    Bytes objects can also be created with literals, see String and Bytes literals.
    
callable(object)
    Return True if the object arguments appear callable, False if not. If this returns true, it is still possible that 
    a call fails, but if it is fales, calling object will never succeed. Note that classes are callable (calling a
    class returns a new instance); instances are callable if their are class has a __call__() method.
    
chr(i)
    Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) return 
    the string 'a', while chr(8364) return the string '€'. This is the inverse of ord().
    the valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i 
    is outside that range.
    
@classmethod
    Transform a method into a class method.
    A class method receives the class as implicit first argument, just like an instance method receives the instance. 
    To declare a class method, use this idiom:
    
    class C:
        @classmethod
        def f(cls, arg1, arg2, ...):...
    
    The @classmethod form is a function decorator - see th description of function definitions for Function definitions 
    for details.
    It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored 
    except for its class. If a class method is called for a derived class, the derived class object is passed as the 
    implied first argument.
    
    Class methods are different than C++ or Java static methods. If you want those, see staticmethod() in this section.
    For more information on class methods, consult the documentation on the standard type hierarchy in The standard
    type hierarchy.
    
compile(source, filename, node, flags=0, dont_inherit=False, optimize=-1)
    Compile the source into a code or AST object. Code objects can be executed by exec() or eval(). source can either be
    a normal string, a byte string, or a AST object. Refer to the ast module documentation for information on how to 
    work with AST objects.
    The filename argument should give the file from which teh code was read; pass some recognizable value if it wasn't 
    from a file ('<string>' is commonly used).
    The mode argument specifies wht kind of code must be compiled; it can be 'exec' if source consists of a sequence of 
    statements, 'eval' if it consists of a single expression, or 'single' if it consists of a single interactive 
    statement (in the latter case, expression statements that evaluate to something other than None will be printed).
    The optional arguments flags and dont_inherit control which future statements affect the compilation of source. If 
    neither is present (or both are zero) the code is complied with those future statements that are in effect in the 
    code that is calling compile(). If the flags argument is given and dont_inherit is not (or is zero) then the future 
    statements specified by the flags argument are used in addition to those that would be used anyway. If dont_inherit 
    is a non-zero integer then the flags argument is it - the future statements in effect around the call to compile 
    are ignored.
    Future statements are specified by bits which can be bitwise ORed together to specify multiple statements. The 
    bitfield required to specify a given feature can be found as the compiler_flag attribute on teh _Feature instance
    in the __future__ module.
    The argument optimize specifies the optimization level of the compiler; the default value of -1 selects the 
    optimization level of the interpreter as given by -O options.Explicit levels are 0 (no optimization; __debug__ is
    true), 1(asserts re removed, __debug__ is false) or 2(docstrings are removed too).
    This function raises SyntaxError if the compiled source is invalid, and ValueError if the source contains null
    bytes.
    If you want to parse Python code into its AST representation, see ast.parse().
    
class complex([real[, image])
    Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the 
    first parameter is a string, it will be interpreted as a complex number and the function must be called without a
    second parameter. The second parameter can never be string. Each argument may be any numeric type (including 
    complex). If image is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and 
    float. If both argument are omitted, returns 0j.
    Note: when converting from a string, the string must not contain whitespace around the central + or - operator. For
    example ('1+2j') is fine but complex('1 + sj') raise ValueError.
    The complex type is described in Numeric Types - int, float, complex.
    
delattr(object, name)
    This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of 
    the object's attributes. The function deletes the named attribute, provided the object allows it. For example,
    delattr(x, 'foobar') is equivalent to del x.foobar.
    
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
    Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types - dict for 
    documentation about this class.
    For other containers see the built-in list, set, and tuple classes, as well as the collections module.
    
dir([object])
    Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list 
    of valid attributes for that object.
    If the object has a method named __dir__(), this method will be called and must return the list of attributes. 
    This allows objects that implement a custom __getattr__() or __getattribute__() function to customize the way
    dir() reports their attributes.
    If the object does not provide __dir__(), the function tries its best to gather information from the object's 
    __dict__ attribute, if defined, and from its type object. The resulting list is not necessarily complete, and may 
    be inaccurate when the object has a custom __getattr__().
    The default dir() mechanism behaves differently with different types of the object, as it attempts to produce the 
    most relevant, rather than complete, information:
    - if the object is a module object, the list contains the names of the module's attributes.
    - if the object is a type or class object, the list contains the names of its attributes, and recursively of the 
    attributes of its bses.
    - Otherwise, the list contains the object's attributes' names, the names of its class's attributes, and recursively
    of the attributes of its class's base classes.
    the resulting list is sorted alphabetically. For example.
    
divmod(a, b)
    Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder
    when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For 
    integers, the result is the same as (a//b, a%b). For floating point numbers the result is (q, a%b), where q is 
    usually math.floor(a/b) but may be 1 less that that. In any case q*b + a*b is very close to a, if a%b is non-zero 
    it has the same sign as b, and 0 <= abs(a%b) < abs(b).
    
enumerate(iterable, start=0)
    Return an enumerate object. iterable must be sequence, an iterator, or some other object which supports iteration. 
    The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which 
    defaults to 0) and the values obtained from iterating over iterable.
    Equivalent to 
"""


def enumerate1(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


"""
eval(expression, globals=None, locals=None)
    The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, 
    locals can be any mapping object.
    The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) 
    using the globals and locals dictionaries as global and local namespace. If teh globals dictionary is present and 
    lacks '__builtins__', the current globals are copied into globals before expression is parsed. This means that 
    expression normally has full access to the standard builtins module and restricted environments are propagated. If 
    the local dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the 
    expression is executed in the environment where eval() is called. The return value is the result of the evaluated 
    expression. Syntax errors are reported as exceptions. 
    The function can also be used to executed arbitrary code objects (such as those created by compile()). In this case
    pass a code object instead of a string. If the code object has been compiled with 'exec' as the mode argument, 
    eval()'s return value will be None.
    Hints: dynamic execution of statements is supported by the exec() function. The globals() and locals() functions 
    returns the current global and local dictionary, respectively, which may be useful to pass around for use by eval()
    or exec().
    See ast.literal_eval() for a function that can safely evaluate strings with expressions containing only literals.
    
exec(object[, globals[, locals]])
    This function supports dynamic execution of Python code. object must be either a string or a code object. If it is 
    a string, the string is parsed as a suite of Python statements which is the executed (unless a syntax error occurs). 
    If it is a code object, it is simply executed. In all cases, the code that's executed is expected to be valid as 
    file input (see the section "File input" in the Reference Manual). Be aware that the return and yield statements 
    may not be used outside of function definitions even within the context of code passed to the exec() function. The 
    return value is None.
    In all cases, if the optional parts are omitted, the code is executed in the current scope. If only globals is 
    provided, it must be a dictionary, which will be used for both the global and the local variables. If globals and 
    locals are given, they are used for the global and local variables, respectively. If provided, locals can be any
    mapping object. remember that at module level, globals and locals are the same dictionary. If exec gets two 
    separate objects as globals and locals, the code will be executed as if it were embedded in a class definition.
    If the globals dictionary does not contain a value for the key __builtins__, a reference to the dictionary of the 
    bult-in module builtins is inserted under that key. That way you can control what builtins are available to 
    executed code by inserting your own __builtins__ dictionary into globals before passing it to exec().
    Note: The built-in functions globals() and locals() return the current global and local dictionary, respectively, 
    which may be useful to pass around for use as the second and third argument to exec().
    Note: The default locals act as described for function locals() below: Modifications to the default locals 
    dictionary should not be attempted. Pass an explicit locals dictionary if you need to see effects of the code on 
    locals after function exec() returns.
    
filter(function, iterable)
    construct an iterator from those elements of iterable for which function returns true. iterable may be either a 
    sequence, a container which supports iteration, or an iterator. If function is None, the identity function is 
    assumed, that is, all elements of iterable that are false are removed. 
    Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if 
    function(item)) if function is not None and (item for item in iterable if item) if function is None.
    See itertools.filterfalse() for the complementary function that returns elements of iterable for which function 
    returns false.
    
class float([x])
    Return a floating point number constructed from a number or string x.
    If the argument is a string, it should contains a decimal number, optionally preceded by a sign, and optionally 
    embedded in whitespace. The optional sign may be '+' or '-'; a '+' sign has no effect on the value produced. The 
    argument may also be a string representing a NaN (not-a-number), or a positive or negative infinity. More 
    precisely, the input must conform to the following grammar after leading and trailing whitespace characters are 
    removed:
    here floatnumber is the form of a Python floating-point literal, described in Floating Point literals. Case is not 
    significant, so, for example, "inf", "Inf", "INFINITY" and "inFiNiTY" are all acceptable spellings for positive
    infinity.
    Otherwise, if the argument is an integer or a floating point number, a floating point number with the same value (
    within Python's floating point precision) is returned. if the argument is outside the range of a Python float, an 
    OverflowError will be raised.
    For a general Python object x float(x) delegates to x.__float__().
    If no argument is given, 0.0 is returned.
    The float type is described in Numeric Types - int, float, complex.
    
format(value[, format_spec])
    convert a value to a "formatted" representation, as controlled by format_spec. The interpretation of format_spec 
    will depend on the type of the value argument, however there is a standard formatting syntax that is used by most 
    built-in types: Format Specification Mini-Language.
    The default format_spec is an empty string which usually gives the same effect as calling str(value).
    A call to format(value, format_spec) is translated to type(value).__format__(value, format_spec) which bypasses the 
    instance dictionary when searching for the value's __format__() method. A TypeError exception is raised if the 
    method search reaches object and the format_spec is non-empty, or if either the format_spec or the return value are
    not strings.
    
class frozenset9[iterable])
    Return a new frozenset object, optionally with elements taken from iterable. frozenset is a bulit-in class.
    
getattr(object, name[, default])
    Return the value of the named attribute of object. name must be a string. if the string is the name of one of the 
    object's attributes, teh result is the value of that attributes. If the named attribute does not exist, default is 
    returned if provided, otherwise AttributeError is raised.
    
globals()
    Return a dictionary representing the current global symbol table. This is always the dictionary of the current 
    module, this is the module where it is defined, not the module from which is called)
    
hasattr(object, name)
    The arguments are an object and a string. The result is True if the string is the name of one of the object's 
    attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an 
    AttributeError or not).
    
hash(object)
    Return the hash value of the object(if it has one). Hash values are integers. They are used to quickly compare 
    dictionary keys during a dictionary lookup. Numeric values that compare equal has the same hash value (even if they 
    are of different types, as is the case for 1 and 1.0).
    Note: For objects with custom __hash__() methods, note that hash() truncates the return value based on the bit 
    width of the host machine. See __hash__() for details.
    
help([object])
    Invoke the built-in help system. (This function is intended for interactive use.) if no argument is given, the 
    interactive help system starts on the interpreter console. If the argument is a string, then the string is looked 
    up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on 
    the console. If the argument is any other kind of object, a help pge on the object is generated.
    This function is added to buld-in namespace by the site module.
    
hex(x)
    Convert an integer number to a lowercase hexadecimal string prefixed with '0x'. If x is not a python int object, it
    has to defined an __index__() method that returns an integer. 
    If you want to convert an integer number to an uppercase or lower hexadecimal string with prefix or not, you can use
    either of the following ways:
    >>> format(255, "#x"), format(255, 'x'), format(255, 'X')
    see also format() for more information. 
    see also int() for converting a hexadecimal string to an integer using a base of 16.
    Note: To abtain a hexadecimal string representation for a float, use the float.hex() method. 
    
id(object)
    Return the "identity" of an object. This is an integer which is guaranteed to be unique and constant for this object
    during its lifetime. Two objects with non-overlapping lifetimes may have teh same id() value.
    
input([prompt])
    If the prompt argument is present, it is written to standard output without a trailing new line. the function then 
    reads a line from input, converts it to a string (strpping a trailing newline). and returns that. When EOF is 
    read, EOFError is raised.
    If the readline module was loaded, then input() will use it to provide elaborate line editing and history features.
    
class int(x=0)
class int(x, base=10)
    Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x is a 
    number, return x.__int__(). if x defines x.__trunc__() but not x.__int__(), then return x.__trunc__(). For floating 
    point numbers this truncates towards zero.
    If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an 
    integer literal in radix base. Optionally, the literal can be preceded by + or - (with no space in between) and 
    surrounded by whitespace. A based-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 
    10 to 35. The default base is 10. the allowed values are 0 and 2-36. Base-2, -8, and -16 literals can be optionally 
    prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code. Base 0 means to interpret exactly as a code 
    literal, so that the actual base is 2, 8, 10, or 16, and so that int('010', 0) is not legal, while int('101') is, 
    as well as int('010', 8).
    The integer type is described in Numeric Types - int, float, complex.
    
isinstance(object, classinfo)
    Return true if the object argument is an instance of teh classinfo argument, or of a (direct, indirect or virtual) 
    subclass thereof. If object is not an object of the given type, the function always returns false. If classinfo is 
    a tuple of type objects (or recursively, other such tuples), return true if object is an instance of any of the 
    types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.
    
issubclass(class, classinfo)
    Return true if class is subclass (direct, indirect, or virtual) of classinfo. A class is considered a subclass of 
    itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked. In any 
    other case, a TypeError exception is raised.
    
iter(object[, sentinel])
    Return an iterator object. The first argument is interpreted very differently depending on the presence of the 
    second argument. Without a second argument, object must be a collection object with supports the iteration protocol
    (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments 
    starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, 
    sentinel, is given, then object must be a callable object. The iterator created in this case will call object with 
    no arguments for each call to its __next__()
    See also Iterator Types
    One useful application of the second form of iter() is to read lines of a file until a certain line is reached. The 
    Following example reads a file until the readline() method returns an empty string:
"""


def process_line(linei):
    print(linei)


with open('mydata.text') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)

"""
len(s
    Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, 
    tuple, list, or range) or collection (such as a dictionary, set, or frozen set).
    
class ilst([iterable])
    Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types
    - list, tuple, range.
    
locals()
    Update and return a dictionary representing the current local symbol table. Free variables are returned by locals()
    when it is called in functions, but not in class blocks.
    Note: The contents of this dictionary should not be modified; change may not affect the values of local and free 
    variables used by the interpreter.
"""
