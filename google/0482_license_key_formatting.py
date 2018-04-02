"""
482. License Key Formatting

You are given a license key represented as a string S with consists only alphanumeric character and dashes. The string
is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the stings such that each group contains exactly K characters, except for
the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must
be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:

Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters. Note that the two extra dashes are
not needed and can be removed.

Example 2:

Input: S = "2-5g-3-J",  K = 2

Output: "2-5G-3J"

Explanation: The string S has been split ito three parts, each part has 2 characters except the first part as it could
be shorter as mentioned above.

Note:
    1. The length of string S will not exceed 12,000, and K is a positive integer.
    2. String S consists only of alphanumerical characters (a-z and /or A-Z and / or0-9) and dashes(-).
    3. String S is non-empty.
"""
import sys


class Solution:
    def license_key_formatting(self, S, K):
        s_list = S.split('-')
        new_str = ''.join(s_list)
        new_list = []

        while len(new_str) > k:
            new_list.insert(0, new_str[-K:])
            new_str = new_str[:len(new_str) - K]
        new_list.insert(0, new_str)

        return '-'.join(new_list).upper()


"""
8.3 Handling Exception
"""


try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())

except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


"""
The try ... except statement has an optional else clause, which , when present, must follow all except clauses. It is 
useful for code that must be executed if the try clause does not raise an exception. For example:
"""


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has' , len(f.readline()), 'lines')
        f.close()


"""
The use of the else clause is better than adding additional code to the try clause because it avoids accidentally 
catching an exception that wasn't raised by the code being protected by the try ... except statement.

When an exception occurs, it may have an associated value, also known as the exception's argument. The presence and type
of the argument depend on the exception type.

The except clause may specify a variable after the exception name. The variable is bound to an exception instance with 
the arguments stored in instances.args. For convenience, the exception instance defines __str__() so the arguments can 
be printed directly without having to reference .args. One may also instantiate an exception first before raising it
and add any attributes to it as desired.

If an exception has arguments, they are printed as the last part ('detail') of the message for unhandled exceptions.

Exception handlers don't just handle exceptions if they occur immediately in the try clause, but also if they occur 
inside functions that are called (even indirectly) in the try clause. For example:

8.4 Raising Exceptions

The raise statement allows the programmer to force a specified exception to occur. For example:

The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an 
exception class (a class that derives from Exception). If an exception class is passed, it wil be implicitly 
instantiated by calling its constructor with no arguments:

If you need to determine whether an exception was raised but don't intend to handle it, a simpler from of the raise 
statement allows you to re-raise the exception:

8.5 User-defined Exceptions

Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes). 
Exceptions should typically be derived from teh Exception class, either directly or indirectly.

Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only 
offering a number of attributes that allow information about the error to be extracted by handlers for the exception. 
When creating a module that can raise several distinct errors, a common practice is to create a base class for 
exceptions defined by that module, and subclass that to create specific exception classes for different error
conditions:
"""


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


"""
Most exceptions are defined with names that end in "Error", similar to the naming of the standard exceptions.

Many standard modules define their own exceptions to report error that may occur in functions they define. More 
information on classes is presented in the chapter Classes.

8.6. Defining Clean-up Actions

The try statement has another optional clause which is intended to define clean-up actions that must be executed under
all circumstances. For example:

A finally clause is always executed before leaving the try statement, whether an exception has occurred or not. When
an exception has occurred in the try clause and has not been handled by an except clause (or it has occurred in an 
except or else clause), it is re-raised after the finally clause has been executed. The finally clause is also 
executed "on the way out" when any other clause of the try statement is let via a break, continue or return statement. 
A more complicated example:

As you can see, the finally clause is executed in any event. The TypeError raised by dividing two strings is not
handled by the except clause and therefore re-raised after the finally clause has been executed.

In real world applications, the finally clause is useful for releasing external resources (such as files or network 
connections), regardless of whether the use of the resource was successful.

8.7. Predefined Clean-up Actions

Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of 
whether or not the operation using the object succeeded or failed. Look at the following example, which tries to open 
a file and print its contents to the screen.
"""


for line in open('myfile.txt'):
    print(line, end="")


"""
The problem with this code is that it leaves the file open for an  indeterminate amount of time after this part of the 
code has finished executing. This is not an issue in simple scripts, but can be a problem for larger applications. The 
with statement allows objects like files to be used i a way that ensures they are always cleaned up promptly and 
correctly.
"""


with open("myfile.txt") as f:
    for line in f:
        print(line, end='')


"""
After the statement is executed, the file f is always closed, even if a problem was encountered while processing the 
lines. Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.

9. Classes

Compared with other programming languages, Python's class mechanism adds classes with a minimum of new syntax and 
semantics. It is a mixture of the class mechanisms found in C++ and Modular-3. Python classes provide all teh standard
features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived 
class can override any methods of its base class or classes, and a method can call the method of a base class with the 
same name. Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the 
dynamic nature of Python: they are created at runtime, and can be modified further after creation.

In C++ terminology, normally class members (including the data members) are public (except see below Private Variables),
and all member functions are virtual. As in Modular-3, there are no shorthands for referencing the object's members
from its methods: the method function is declared with an explicit first argument representing the object, which is 
provided implicitly by the call. As in Smalltalk, classes themselves are objects. This provides semantics for importing
and renaming. Unlike C++ and Modular-3, built-in types can be used as base classes for extension by the user. Also like
in C++, most built-in operators with special syntax (arithmetic operators, subscripting etc.) can be redefined for 
class instances.

(Lacking universally accepted terminology to talk about classes, I will make occasional use of Smalltalk and C++ terms.
I would use Modular-3 terms, since its object-oriented semantics are closer to those of Python than C++, but I expect 
that few readers heard of it.)

9.1. A word about names and objects

Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. This is known as 
aliasing in other languages. This is usually not appreciated on a first glance at Python, and can be safely ignored 
when dealing with immutable basic types (numbers, strings, tuples). However, aliasing has a possibly surprising effect
on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types. This is 
usually used to the benefit of the program, since aliases behave like pointers in some respects. For example, passing an
object is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as 
an argument, the caller will see the change. - this eliminates teh need for two different arguments passing mechanisms 
as in Pascal.

9.2. Python scopes and Namespaces

Before introducing classes, I first have to tell you something about Python's scope rules. Class definitions play some 
neat tricks with namespaces, and you need to know how scopes and namespaces work to fully understand what's going on.
Incidentally, knowledge about this is useful for any advanced Python programmer.

Let's begin with some definitions.

A namespace is mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but 
that's normally not noticeable in any way (except for performance), and it may change in the future. Examples of 
namespaces are: The set of built-in names (containing functions such as abs(), and built-in exception names); the 
global names in a module; and the local names in a function invocation. In a sense teh set of attributes of an object 
also from a namespace. The important thing to know about namespaces is that there is absolutely no relation between 
names in different namespaces; for instance, two different modules may both define a function maximize without 
confusion - users of the modules must prefix it with the module name.

By the way, I use the word attribute for any name following a dot - for example, in the expression z.real, real is an 
attribute of the object z. Strictly speaking, references to names in modules are attribute reference: in the expression
modname.funcname, modname is a module object and funcname is an attribute of it. In this case there happens to be a 
straightforward mapping between the modules's attributes and the global names defined in the module: they share the same
namespaces!

Attributes amy be read-only or writable. In the latter case, assignment to attributes is possible. Module attributes are
writable: you can write modname.the _answer = 42. Writeable attributes may also be deleted with the del statement. For
example, del modname.the_answer will remove the attribute the_answer from the object named by modname.

Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names 
is created when the Python interpreter starts up, and is never deleted. the global namespace for a module is created 
when module definitions is read in; normally, module namespaces also last until the interpreter quits. The statements 
executed by the top-level invocation of the interpreter, either read form a script file or interactively, are considered
part of a module called __main__, so they have their own global namespaces. (The built-in names actually also live in 
a module; this is called builtins.)

The local namespaces for a function is created when the function is called, and deleted when the function returns or 
raise an exception that is not handled within the function. (Actually, forgetting would be better way to describe what 
actually happens.) Of course, recursive invocations each have their own local namespace.

A scope is textual region of a Python program where a namespace is directly accessible. "Directly accessible" here means 
that an unqualified reference to a name attempts to find the name in the namespace. 

Although scopes are determined statically, they are used dynamically. At any tie during execution, there are at lest 
three nested scopes whose namespaces are directly accessible:

    - The innnermost scope, which is searched irst, contains the local names.
    
    - The scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains
    non-local, but also non-global names
    
    - The next-to-last scope contains the current modules's global names
    
    - the outermost scope (searched last) is the namespace containing built-in names
    
If a name is declared global, then all references and assignments go directly to the middle scope containing the 
module's global names. To rebind variables found outside of the innermost scope, the nonlocal statement can be used; 
if not declared nonlocal, those variable are read-only (an attempt to write to such a variable will simply create a new 
local variable in teh innermost scope, leaving the identically named outer variable unchanged).

Usually, the local scope references the local names of the (textually) current function. Outside function, the local 
scope references the same namespaces as the global scope: the modules's namespaces. Class definitions place yet another
namespace in the local scope.

It is important to realize that scopes are determined textually: teh global scope of a function defined in a module is 
that module's namespace, no matter from where or y what alias the function is called. On the other hand, teh actual 
search for names is done dynamically, at run time - however, the language definitions is evolving towards static name
resolution, at "compile" time, so don't rely on dynamic name resolution! (In fact, local variables are already 
determined statically.)

A special quirk of Python is that - if no global statement is in effect - assignments to names always go into the 
innermost scope. Assignments do not copy data - they just bind names to objects. The same is true for deletions: The 
statement dex removes the binding of x form the namespace referenced by the local scope, In fact, all operations that 
introduce new names use the local scope: in particular, import statements and function definitions bind the module or 
function name in the local scope.

The global statement can be used to indicate that particular variables live in the global scope and should be rebound
there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound 
there.

9.2.1. Scopes and Namespaces Example

This is an example demonstrating how to reference the different scopes and namespaces, and how global and nonlocal 
affect variable binding:
"""


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal  spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After non_local assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


"""
The output of the example code is:

Note how the local assignment (which is default) didn't change scope_test's binding of spam. the nonlocal assignment
changed scope_test's binding of spam, and the global assignment changed the module-level binding.

You can also see that there was no previous binding for spam before the global assignment.

9.3. A fist look at classes

Classes introduce a little bit of new syntax, three new object types, and some new semantics.

9.3.1. Class definition syntax

The simplest form of class definition looks like this
"""


class ClassName:
    pass


"""
Class definitions, like function definitions (def statements) must be executed before they have any effect. (You could 
conceivably place a class definition in a branch of an if statement, or inside a function.)

In practice, the statements inside a class definition will usually be functions, but other statements are allowed, and 
sometimes useful - we'll come back to this later. The function definitions inside a class normally have a peculiar form 
of argument list, dictated by the calling conventions for methods - again, this is explained later.

When a class definition is entered, a new namespace is created, and used as the local scope - thus, all assignments to 
local variables go into this new namespace. In particular, function definitions bind the name of the new function here.

when a class definition is left normally (via the end), a class object is created. This is basically a wrapper around 
the contents of the namespace created by the class definition; we'll learn more about class objects in the next section.
The original local scope (the one in effect just before the class definition was entered) is reinstated, and the class
object is bound here to the class name given in the class definition header (ClassName in the example).


"""