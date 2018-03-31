"""
686. Repeated String Match

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If
no such solution, return -1.

For example, with A = 'abcd' and B = 'cdabcdab'.

Return 3, because by repeating A three times ("abcdabcdabcd"), B is a subsring of it; and B is not a substring of A
repeated two times ("abcdabcd").

Note:
    The length of A and B will be between 1 and 10000.

Thought process:
    1. Just continue to + A to A one by one.
    2. The check the string B is in the new string.
    3. When the new sting is longer than 3 * length(B) if still can't find string B then return -1.
"""
import math


def repeated_string_match(A, B):

    """
    This is brute force solution.
    Time complexity: O(n)
    Space complexity: O(n)

    :param A:
    :param B:
    :return:
    """
    tem = A
    count = 1
    if tem.find(B) != -1:
        return count
    while len(tem) < 3 * len(B):
        if tem.find(B) != -1:
            return count
        count += 1
        tem += A
    return -1


"""
Solution 2:

Let n be the answer, the minimum number of times A has to be repeated.

for B to be inside A, A has to be repeated sufficient times such that it is at least as long as B (or one more), hence
we can conclude that the theoretical lower bound for the answer would be the length of B / length of A.

Let x be the theoretical lower bound, which is ceil(len(B)/len(A)).

The answer n can only be x or x+1 (in the case where len(B) is a multiple of len(A) like in A = 'abcd' and B = 
'cdabcdab") and not more. Because if B is already in A * n, Bis definitely in A * (n + 1_.

Hence we only need to check whether B in A * x or B in A * (x+1), and if both are not possible return -1.

Here's the cheeky tow-line
"""


def repeated_string_match1(A, B):
    t = math.ceil(len(B)/len(A))
    return t * (B in A * t) or (t + 1) * (B in A * (t + 1)) or -1


"""
But don't do  the above in interview. Doing the following is more readable.
"""


def repeated_string_match2(A, B):
    times = math.ceil(len(B)/len(A))
    for i in range(2):
        if B in (A * (times + i)):
            return times + i
    return -1


"""
3.1.3. Lists

Python knows a number of compound data types, used to group together other values. The most versatile is the list, 
which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of 
different types, but usually the items all have hte same type.

Like strings (and all other built-in sequence type), lists can be indexed and sliced:

All slice operations return a new list containing the requested elements. This means that the following slice returns a 
new (shallow) copy of the list:

Lists also support operations like concatenation:

Unlike Strings, which immutable, lists are a mutable type, i.e. it is possible to change their content:

You can also add new items at the end of list, by using the append() method (we will see more about methods later):

Assignment to slice is also possible, and this can even change the size of the list or clear it entirely:

The built-in function len() also applies to lists:

It is possible to nest lists (create lists containing other lists), for example:

3.2. First steps towards programming

Of course, we can use Python for more complicated tasks then adding two and tow together. For instance, we can write
an initial sub-sequence of the Fibonacci series as follows:
"""


a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b


"""
This example introduces several new features.

    - The first line contains a multiple assignment: the variables a and b simultaneously get the new values 0 and 1.
    On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated 
    first before any of the assignments take place. the right-hand side expressions are evaluated from the left to the
    right.
    
    - the while loop executes as long as the condition (here b < 10) remains true. In Python, like in C, any non-zero 
    integer value is true; zero is false. The condition may also be a string or list value, in fact any sequence; 
    anything with a non-zero length is true, empty sequences are false. The test used in the example is a simple 
    comparison. The standard comparison operators are written the same as in C: < (less than), > (greater than), == (
    equal to), <= (less than or equal to), >= (greater than or equal to) and != (not equal to).
    
    - The body of the loop is indented: indentation is Pythons's way of grouping statements. At the interactive prompt, 
    you have to type a tab or space(s) for each indented line. In practice you will prepare more complicated input for 
    Python with a text editor; all decent text editors have an auto-indent facility. When a compound statement is 
    entered interactively, it must be followed by a blank line to indicate completion (since the parser cannot guess
    when you have typed the last line). Note that each line within a basic block must be indented by the same amount.
    
    - The print() function writes the value of the arguments(s) it is given. It differs from just writing the expression
    you want to write (as we did earlier in the calculator examples) in the way it handles multiple arguments, floating 
    point quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can
    format things nicely, like this:
    
    The keyword argument end can be used to avoid the newline after the output, or end the output with a different 
    string:
    
    
4. More Control Flow Tools

Besides the while statement just introduced, Python knows the usual control flow statements known from other languages, 
with some twists.

4.1. if Statements

Perhaps the most well-known statement type is the if statement. For example:
"""


x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


"""
There can be zero or more elif parts, and the else part is optional. The keyword 'elif' is short for 'else if', and is 
useful to avoid excessive indentation. An if ... elif ... elif ... sequence is a substitute for the switch or case 
statements found in other languages.

4.2. for statements

The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating 
over an arithmetic progression of numbers (like in Pascal), or giving the user teh ability to define both the iteration
step and halting condition (as C), Python's for statement iterates over the items of any sequence (a list or a string),
in the order that they appear in the sequence. For example (no pun intended):
"""


words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))


"""
If yo uneed to modify the sequence yo are iterating over while inside the loop (for example t duplicate selected items),
it is recommended that you first make a copy. Iterating over a sequence does not implicitly make a copy. The slice 
notation makes this especially convenient:
"""


for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)


"""
4.3. The range() Function

If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates 
arithmetic progressions:
"""


for i in range(5):
    print(i)


"""
The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items
of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment
(even negative; sometimes this is called the 'step'):

To iterate over the indices of a sequence, you cna combine range() and len() as follows:
"""

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])


"""
In most such cases, however, it is convenient to use the enumerate() function, see Looping Techniques.

A strange thing happens if you just print a range:

In many ways the object returned by range() behaves as if it is a list, but in fact it isn't. It is an object which 
return the successive items of the desired sequence when you iterate over it, but it doesn't really make the list, thus 
saving space.

We say such an object iterable, that is, suitable as a target for functions and constructs that expect something from
which they can obtain successive items until the supply is exhausted. We have seen that the for statement is such an 
iterator. The function list() is another; it creates lists from iterables:

Later we will see more functions that return iterables and take iterables as argument.

4.4. break and continue Statements, and else Clauses on Loopes

The break statement, like in C, breaks out of the innermost enclosing for or while loop.

Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with
for ) or when the condition becomes false (with while), but not when the loop is terminated by break statement. This is 
exemplified by the following loop, which searches for prime numbers:
"""


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


"""
(Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement.)

When used with a loop, the else clause has more in common with teh else clause of a try statement than it does that of 
if statements: a try statement's else clause runs when no exception occurs, and a loop's else clause runs when no break 
occurs. For more on the try statement and exceptions, see Handling Exceptions.

The continue statement, also borrowed form C, continues with the next iteration of the loop:
"""


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


"""
4.5. pass Statements

The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no 
action. For example:
"""


while True:
    pass


"""
This is commonly used for creating minimal classes:
"""


class MyEmptyClass:
    pass


"""
Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, 
allowing you to keep thinking at a more abstract level. The pass is silently ignored:
"""


def initlog(*args):
    pass


"""
4.6. Defining Functions

We can create a function that writes the Fibonacci series to an arbitrary boundary:
"""


def fib(n):
    """ Print a Fibonacci series up to n. """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


"""
The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list 
of formal parameters. The statements that form the body of the function start at the next line, and must be indented.

The first statement of the function body can optionally be a string literal; this string literal is the function's 
documentation string, or docstring. (More about docstrings can be found in the section Documentation Strings.) There are
tools which use docstrings to automatically produce online of printed documentation, or to let the user interactively 
browse through code; it's good practice to include docstrings in code that you write, so make a habit of it.
 
The execution of a function introduces a new symbol table used for the local variables of the function. More precisely,
all variable assignments in a function store the value in the local symbol table; whereas variable references first look
in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, 
and finally in the table of built-in names. Thus, global variables cannot be directly assigned a value with in a 
within a function (unless named in a global statement), although they may be referenced.

The actual parameters (arguments) to a function call are introduced in the local symbol table of teh called function
when it is called; thus arguments are passed using call by value ( where the value is always an object reference, not 
the value of the object). When a function calls another function, a new local symbol table is created for that call.

A function definition introduces the function name in the current symbol table. The value of teh function name has a 
type that is recognized by the interpreter as a user-defined function. This value can be assigned to another name which
can then also be sued as a function. This serves as a general renaming mechanism:

Coming from other languages, you might object that fib is not a function but a procedure since it doesn't return a 
value. In fact, even functions without return statement do return a value, albeit a rather boring one. This value is 
called None (it's a built-in name). Writing the value None is normally suppressed by the interpreter if it would be the 
only value written. You can see it fi you really want to using print():

It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:
"""


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


"""
This example, as usual, demonstrates some new Python features:

    - The return statement returns with a value from a function. return without an expression argument returns None.
    Falling off the end of function also returns None.
    
    - The statement result.append(a) calls a method of the list object result. A method is a function that 'belongs' to
    an object and its named obj.methodname, where obj is some object (this may be an expression), and methodname is 
    the name of a method that is defined by the object's type. Different types define different methods. methods of 
    different types may have the same name without causing ambiguity (It is possible to define your own object types 
    and methods, using classes, see Classes) The method append() shown in the example is defined for list objects; It 
    adds a new element at the end of the list. In this example it is equivalent to result = result + [a], but more 
    efficient.
    
4.7. More on Defining Functions

It is also possible to define functions with a variable number of arguments. There are three forms, which can be 
combined.

4.7.1. Default Argument Values

The most useful form is to specify a default value for one or more arguments. This cretes a function that can be called
with fewer arguments than it is defined to allow. For example:
"""


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


"""
This function can be called in several ways:

    - Giving only the mandatory argument: ask_ok('Do you really want to quit?)
    - Giving one of the optional argument: ask_ok('Ok to overwrite the file?', 2)
    - Or even giving all arguments: ask_ok('Ok to overwrite the file?, 2, 'Come on, only yes or no!)
    
This example also introduces the in keyword. This tests whether or not a sequence contains a certain value.

The default values are evaluated at the point of function definition in the defining scope, so that
"""

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


"""
will print 5.

Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable 
object such as a list, dictionary, or instance of most classes. For example, the following function accumulates the 
passed to it on subsequent calls.
"""


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


"""
this will print:
[1]
[1, 2]
[1, 2, 3]

If you don't want the default to be shared between subsequent calls, you can write the function like this instead:
"""


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


"""
4.7.2. Keyword arguments

Function can also be called using keyword arguments of the form kwarg=value. For instance, the following function:
"""


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=" ")
    print("If you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's ", state, '!')


"""
accepts one required argument (voltage) and three optional arguments (state, action, and type). This function can be
called in any of the following ways:

parrot(10000)                                           # 1 positional argument
parrot(voltage=10000)                                   # 1 keyword argument
parrot(voltage=1000, action="voom")                     # 2 keyword arguments
parrot(action="voom", voltage=1000)                     # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')           # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')    # 1 positional, 1 keyword

But all the following calls would be invalid:

parrot()                                                # required argument missing
parrot(voltage=5.0, 'dead')                             # non-keyword argument after keyword argument
parrot(110, voltage=220)                                # duplicate value for the same argument
parrot(actor='John Cleese')                             # unknown keyword argument
"""