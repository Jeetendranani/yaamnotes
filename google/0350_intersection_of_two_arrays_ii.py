"""
350 Intersection of Two arrays II

Given two arrays, write a function to compute their intersection.

Example:
    Given number1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2]

Note:
    - Each element in the result should appear as many times as it shows in both arrays.
    - The result can be in any order.

Follow up:
    - What is the given array is already sorted? How would you optimized your algorithm?
    - What if nums1's size is small compared to nums2's size? Which algorithm is better?
    - What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements
    into the memory at once?


Thought process:

    1. Try to find common numbers in both array. Ideally we can solve this with one scan of both arrays.
    2. Scan one of them and convert it to dictionary with its repeated number.
    3. Scan the other one and update the number set and result.
    4. Return the result.
"""
import collections


def intersect(nums1, nums2):

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    :param nums1:
    :param nums2:
    :return:
    """
    num_set = collections.Counter(nums1)
    res = []
    for i in nums2:
        if i in num_set.keys():
            res.append(i)
            num_set[i] _= 1
            if num_set[i] == 0:
                del num_set[i]
    return res


"""
    If given array is sorted, then we dont need the counter to remember the number of elements, we just need to scan 
    with two pointers.
    1. if a1[i] == a2[j], then add it to result
    2. if a1[i] < a2[j], then i += 1
    3. if a1[i] > a2[j], then j += 1
    4. if one ot then finished, exit the loop
    5. return the result.
    
    
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into 
    the memory at once?
    - if only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that into the 
    memory, and record the intersections. 
    - If both nums 1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort), 
    then read 2 element from each array at a time in memory, record intersections.
"""


"""
The python tutorial

Python is an easy to lean, powerful programming language. It has efficient high-level data structures and simple but 
effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its 
interpreted nature, make it an ideal language for scripting an rapid application development in many areas on most 
platforms.

The Python interpreter and the extensive standard library are freely available in source or binary form for all major
platforms from the Python Web site, https://www.python.org/, and may be freely distributed. The same site also contains 
distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.

The Python interpreter is easily extended with new functions and data types implemented in C and C++ (or other languages
callable from C). Python is also suitable as an extension language for customizable applications.

This tutorial introduces the reader informally to teh basic concepts and features of the Python language and system. It
helps to have Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial 
can be read off-line as well.

For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives
a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python
Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.

This tutorial does not attempt to be comprehensive and cover every single feature. Or even every commonly used feature.
Instead, it introduces many of Python's most noteworthy features, and will give you a good idea of the language's flavor
and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to 
learn more about the various Python Library modules described in The Python Standard Library.

The Glossary is also worth going through.
    1. Whetting your Appetite     
    2. Using the Python interpreter
        2.1. Invoking the interpreter
            2.1.1. Argument Passing
            2.1.2. Interactive Mode
        2.2 The interpreter and its Environment
            2.2.1. Source Code Encoding
    3. An informal Introduction to Python
        3.1 using Python as a Calculator
            3.1.1. Numbers
            3.1.2. Strings
            3.1.3. Lists
        3.2 Fist Steps Towards Programming
    4. More Control Flow Tools
        4.1. if Statements
        4.2. for Statements
        4.3. The range() Function
        4.4. break and continue Statements, and else Clauses on Loops
        4.5. pass Statements
        4.6. Defining Functions
        4.7. More on Defining Functions
            4.7.1. Default argument Values
            4.7.2. Keyword Arguments
            4.7.3. Arbitrary Arguments Lists
            4.7.4. unpacking Argument Lists
            4.7.5. Lambda Expressions
            4.7.6. Documentation Strings
            4.7.7. Function Annotations
        4.8. Intermezzo: Coding Style
    5. Data Structures
        5.1. More on Lists
            5.1.1. using Lists as Stacks
            5.1.2. Using Lists as Queues
            5.1.3. List Comprehensions
            5.1.4. Nested List Comprehensions
        5.2. The del Statement
        5.3. Tuples and sequences
        5.4. Sets
        5.5. Dictionaries
        5.6. Looping Techniques
        5.7. More on conditions
        5.8. Comparing sequences and other types
    6. Modules
        6.1. More on Modules
            6.1.1. Executing modules as scripts
            6.1.2. The modules search path
            6.1.3. "Compiled" Python files.
        6.2. Standard Modules
        6.3. The dir() Function
        6.4. Packages
            6.4.1. Importing * from a package
            6.4.2. Intra-package References
            6.4.3. Packages in Multiple Directories
    7. Input and Output
        7.1. Fancier Output Formatting
            7.1.1. Old string formatting
        7.2. Reading and Writing Files
            7.2.1. Methods of File Objects
            7.2.2. Saving structured data with json
    8. Errors and Exceptions
        8.1. Syntax Errors
        8.2. Exceptions
        8.3. handling Exceptions
        8.4. Raising Exceptions
        8.5. User-defined Exceptions
        8.6. Defining Clean-up Actions
        8.7. Predefined Clean-up Actions
    9. Classes
        9.1. A Word About Names and Objects
        9.2. Python Scopes and Namespaces
            9.2.1. Scopes and Namespaces Exammple
        9.3. A First Look at Classes
            9.3.1. Class Definition Syntax
            9.3.2. Class Objects
            9.3.3. Instance Objects
            9.3.4. Method Objects
            9.3.5. Class and instance Variables
        9.4 Random Remarks
        9.5 Inheritance
            9.5.1. Multiple Inheritance
        9.6 Private Variables
        9.7 odds and Ends
        9.8 iterators
        9.9 Generators
        9.10. Generator Expressions
    10. Brief Tour of the standard library
        10.1. Operating System Interface
        10.2. File Wildcards
        10.3. Command Line Arguments
        10.4. Error Output Redirection and Program Termination
        10.5. String Pattern Matching
        10.6. Mathematics
        10.7. Internet Access
        10.8. Dates and Times
        10.9. Data Compression
        10.10. Performance Measurement
        10.11. Quality Control
        10.12. Batteries Included
    11. Brief Tour of the Standard Library - Part II
        11.1. Output Formatting
        11.2. Templating
        11.3. Working with Binary Data Record Layouts
        11.4. Multi-threading
        11.5. Logging
        11.6. Weak References
        11.7. Tools for Working with Lists
        11.8. Decimal Floating Point Arithmetic
    12. Virtual Environments and Packages
        12.1. Introduction
        12.2. Creating Virtual environments
        12.3. Managing Packages with pip
    13. What Now?
    14. Interactive input Editing and History Substitution
        14.1. Tab Completion and History Editing
        14.2. Alternatives to the interactive Interpreter
    15. Floating Point Arithmetic: Issues and Limitations
        15.1 Representation Error
    16. Appendix
        16.1 Interactive Mode
            16.1.1. Error Handling
            16.1.2. Executable Python Scripts
            16.1.3. The Interactive Startup File
            16.1.4. The Customization Modules
        
        
1. Whetting Your Appetite

If you do much work on computers, eventually you find that three's some task you'd to automate. For example, you may
wish to perform a search-and-replace over a large number of text files, or rename and rearrange a bunch of photo files
in a complicated way. Perhaps you'd like to write a small custom database, or a special GUI application, or a simple 
game.

if you are professional software developer, you may have to work with several C/C++Java libraries but find the usual
write/compile/test/re-compile cycle is too slow. Perhaps you're writing a test suite for such a library and find
writing test testing code a tedious task. Or maybe you've writen a program that could use an extension language, and 
you don't want to design and implement a whole new language for your application.

Python is just the language for you.

You could write a Unix shell script or Windows batch files for some  of these tasks, but shell scripts are best at 
moving around files and changing text data, not well-suited GUI applications or games. You could write a C/C++/Java 
program, but it can take a lot of development time to get even a first-draft program. Python si simpler to use, 
available on Windows, Mac OSX, and Unix operating systems, and will help you get the job done more quickly.

Python is simple to use, but it is a ral programming language, offering much more structure and support for large
programs thant shell scripts or batch files can offer. On other hand, Python also offers much more error checking than 
C, and, being a very-high-level language, it has high-level data type built in, such as flexible arrays and 
dictionaries. Because of its more general data types Python is applicable to a much larger problem domain than Awk or 
even Perl, yet many things are at least as easy in Python as in those languages.

Python allows you to split your program into modules that can be reused in other Python programs. It comes with a large
collection of standard modules that you can use as the basis of your programs - or as example to start learning to 
program in Python. Some of these modules provide thins like file I/O, system calls, sockets, and even interfaces to 
graphical user interface toolkits like Tk.

Python is an interpreted language, which can save you considerable time during program development because no 
compilation and linking necessary. The interpreter can be used interactively, which makes it easy to experiment with 
features of the language, to write throw-away programs, or to test functions during bottom-up program development. It 
is also a handy desk calculator.

Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than
equivalent C, C++, or Java programs, for several reasons:
    - the high-level data types allow you express complex operations in a single statement;
    - statement grouping is done by indentation instead of beginning and ending brackets;
    - no variable of argument declaration are necessary.
    
Python is extensible: if you know how to program in C it is easy to add a new built-in function or module to the 
interpreter, either to perform critical operations at maximum speed, or to link Python programs to libraries that may 
only be available in binary form (such as vendor-specific graphics library). Once you are really hooked, you can link 
the Python interpreter into an application written in C and use it as an extension or command language fro that 
application.

By the way, the language is named after the BBC show "Monty Python's Flying Circus" and has nothing to do with reptiles.
Making references to Monty Python skits in documentation is not only allowed, it is encouraged!

Now what you are all excited about Python, you'll want to examine it in some more detail. since the best way to learn a 
language is to use it, the tutorial invites you to play with the Python interpreter as you read.

In the next chapter, the mechanics of using the interpreter are explained. This is rather mundane information, but 
essential for trying out the examples shown later.

The rest of the tutorial introduces various features of the Python language and system through examples, beginning with
simple expressions, statements, and data types, through functions and modules, and finally touch upon advanced concepts 
like exceptions and user-defined classes.
        
        
2. using the python interpreter

2.1. Invoke the interpreter

The Python interpreter is usually installed as /usr/local/bin/python3.5 on those machines where it is available; putting
/usr/local/bin in you Unix shell's search path makes it possible to start it by typing the command:

Python3.5

to the shell. Since the choice of the directory where the interpreter lives is an installation option, other places are 
possible; check with your local Python guru on system administrator. (E.g., /usr/local/python is popular alternative 
location.)

On Windows machines, the Python installation is usually paced in c:\python35, thought you can change this when you're 
running the installer. to add this directory to your path, you can type the following command into the command prompt
in a DOS box:

set path=%path%;c:\python35

Typing an end-of-file character (control-D on unix, control-z on windows) at the primary prompt cause the interpreter to 
exit with a zero exit status. if that doesn't work, you can exit the interpreter by typing the following command: 
quit().

The interpreter's line-editing features include interactive editing, history substitution and code completion on systems
that support readline. Perhaps the quickest check to see whether command line editing is supported is typing control-P
to the first Python prompt you get. If it beeps, you have command line editing; see Appendix Interactive Input Editing 
and History Substitution for an introduction to the keys. if nothing appears to happen, or if ^P is echoed, command line
editing isn't available; you'll only be able to use backspace to remove characters from the current line.

The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it 
reads and executed commands interactively; when called with a file name argument or with a file as standard input, it
reads and executes a script from that file.

A second way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, 
analogous to the shell's -c option. Since Python statements often contain spaces or other characters that ar special to
the shell, it is usually advised to quote command in its entirety with single quotes.

Some Python modules are also useful as scripts. These can be invoked using python -m module [arg] ..., which executes 
the source file for module as if you had spelled out its full name on the command line.

When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards.
This can be done by passing -i before the script.

All command line options are described in Command line and environment.

2.1.1 Argument Passing

When know to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and 
assigned to the argv variable in the sys module. you can access this list by executing import sys. The length of the 
list is at least one; When no script and no argument are given, sys.argv[0] is an empty string. When the script name is 
given as '-' (meaning standard input), sys.argv[0] is set to '-'. When -c command is used, sys.argv[0] is set to '-c'.
When -m module is used, sys.argv[0] is set to the full name of the located module. Options found after -c command or -m
module are not consumed by the Python interpreter's option processing but left in sys.argv for the command or module to
handle.

2.1.2. Interactive Mode

When commands are read from a tty, the interpreter is said to be in interactive mode. In this mode it prompts for the 
next command with the primary prompt, usually three greater-than signs (>>>); for continuation lines it prompt withe 
secondary prompt, by default three dots (...). The interpreter prints a welcome message stating it version number
and a copyright notice before printing the first prompt:

Continuation lines are needed when entering a multi-line construct. As an example, take a look at this if statement:

For more on interactive mode, see Interactive Mode.

2.2. The interpreter and its Environment

2.2.1 Source code Encoding

By default, Python source file are treated as encoded in UTF-8. In that encoding, characters of most languages in the 
world can be used simultaneously in string literals, identifiers and comments - although the standard library only uses
ASCII characters for identifiers, a conversion that any portable code should follow. To display all these characters 
properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all th characters in 
the file.

It is also possible to specify a different encoding for source files. In order to do this, put one more special comment 
line right after the #! line to define the source file encoding:

# _*_ coding: encoding _*_

With that declaration, everything in the source file will be treated as having the encoding encoding instead of UTF-8.
The list of possible encodings can be found in the Python Library Reference, in the section on codecs.

For example, if your editor of choice does not support UTF-8 encoded files and insists on using some other encoding, 
say Windows-1252, you can write:

# _*_ coding: cp-1353 _*_

And still use all characters in the Windows-1252 character set in the source files. The special encoding comment must be
in the first or second line within the file.

3. an informal introduction to Python

In the following examples, input and output are distinguished by the presence or absence of prompts (>>> and ...): to 
repeat the example, you must type everything after the prompt, when the prompt appears; lines that do not begin with a 
prompt are output from teh interpreter. note that a secondary prompt on a line by itself in an example means you must 
type a blank line; this is used to end a multi-line command. 

Many of the examples in this manual, even those entered at teh interactive prompt, include comments. Comments in Python 
start with the hash character, #, and extend to the end of the physical line. A comment may appear at teh start of a 
line or following whitespace or code, but not with in a string literal. A hash character within a string literal is 
just a hash character. Since comments are to clarify code and are not interpreted by Python, they bay be omitted when 
when typing in examples.

Some examples:

# This is the first comment
spam = 1    # and this is the second comment
            # ... and now a third!
text = "# This is not a comment because it's inside quotes."

3.1. Using Python as a Calculator

Let's try some simple Python commands. Start the interpreter and wait for the primary prompt, >>>. (It shouldn't take
long.)

3.1.1. Numbers

The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression 
syntax is straightforward: the operators +, -, * and / work just like in most language (for example, Pascal or C);
parentheses (()) can be used for grouping. For example:

The integer number have type int, the ones with fractional part have type float. We will see more about numeric types
later in the tutorial.

Division (/) always returns a float. To do floor division and get integer result (discarding any fractional result) you 
can use the // operator; to calculate the reminder you can use %:

with Python, it is possible to use the ** operator to calculate power:

The equal sign (=) is used assign a value to a variable. Afterwards, no result is displayed before the next interactive
prompt:

If a variable is not "defined" (assigned a value), trying to use it will give you an error:

There is full support for floating point; operators with mixed type operands convert the integer operand to floating 
point:

In interactive mode, the last printed expression is assigned to teh variable _. This means that when you are using 
Python as a desk calculator, it is somewhat easier to continue calculations, for example:

This variable should be treated as read-only by the user. Don't explicitly assign a value to it - you would create an
independent local variable with the ame name masking the built-in variable with its magic behavior. 

In addition to int and float, Python supports other types of numbers, such as decimal and fraction. Python also has 
built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part.

3.1.2. Strings

Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in a 
single quotes ('...') or double quotes ("...") with the same result. \ can be used to escape quotes:

In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with 
backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two 
strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double 
quotes, otherwise it is enclosed in single quotes. The print() function produces a more readable output, by omitting
the enclosing quotes and by printing escaped and special characters:

If you don't want character prefaced by \ to be interpreted as special characters, you can use raw strings by adding 
an r before the first quote:

String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are 
automatically included in the string, but it's possible to prevent this by adding a \ at the end of the line. The 
following example:

produces the following output (not that the initial newline is not included):

Strings can be concatenated (glued together) with the + operator, and repeated with *:


Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

This only works with two literals though, not with variables or expressions:

If you want to concatenate variables or a variable and a literal, use +:

The feature is particularly useful when you want to break long strings:

Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a 
character is simply a string of size one:

Indices may also be negative numbers, to start counting from the right:

Notes that since -0 is the same as 0, negative indices start from -1.

In addition to indexing, slicing is also supported. While indexing is sued to obtain individual characters, slicing 
allows you to obtain substring:

Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i :] is always equal 
to s:

Since indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the 
size of hte string bing sliced.

One way to remember how slice work is to think of the indices as pointing between characters, with the left edge of the 
first character numbered 0. The the right edge of the last character of a string of n characters has index n, for 
example:

This first rwo of numbers gives the position of the indices 1...6 in the string; the second row gives the corresponding
negative indices. The slice form i to j consists of all characters between the edges labeled i and j, respectively.

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For
example, the length of word[1:3] is 2.

Attempting to use an index that is too large will result in an error:

However, out of range slice indexes are handled gracefully when use for slicing:

Python strings cannot be changed - they are immutable. Therefore, assigning to an indexed position in the string results
in an error:

If you need a different string, you should create a new one:

The built-in function len() returns the length of string:

See also:

Text Sequence Type - str
    Strings are exampes of sequence types, and support the common operations supported by such types.
    
String Methods
    String support a large number of methods for basic transformations and searching.
    
Format String Syntax
    Information about string formatting with str.format()
    
printf-style String Formatting
    The old formatting operations invoked when strings are the left operand of the % operator are descripted in more 
    detail here.    
"""