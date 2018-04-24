"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how mach water
it is able to trap after raining.

For example,

Given [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], return 6

"""


class Solution:
    def trap(self, height):
        lmax, rmax, left, right, total = 0, 0, 0, len(height) - 1, 0
        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            if lmax <= rmax:
                total += lmax - height[left]
                left += 1
            else:
                total += rmax - height[right]
                right += 1

        return total


"""
15.1 Representation Error

This section explains the "0.1" example in detail,  and shows how you can perform an exact analysis of cases like this
yourself. Basic familiarity with binary floating-point representation is assumed.

Representation error refers to the fact that some (most, actually) decimal fractions cannot be represented exactly as 
binary (base 2) fractions. This is the chief reason why Python (or perl, C, C++, Java, Eortran, and many others) often
won't display the exact decimal number you expect. 

Why is that? 1/10 is not exactly representable as a binary fraction. Almost all machines today use IEEE-754 floating 
point arithmetic, and almost all platforms map Python floats to IEEE-754 "double precision". 754 doubles contain 53 
bits of precision, so on input the computer strivers to convert 0.1 to the closest fraction it can of from J/2**N where
J is an integer containing exactly 53 bits. Rewriting

1 / 10 ~= J / (2**N)

as 

J ~= 2 ** N /10

and recalling that J has exactly 53 bits (is >= 2**52, but < 2**53), the best value for N is 56:

That is, 56 is the only value for N that leaves J with exactly 53 bits. The best possible value for J is that quotient
rounded:

Since the remainder is more than half of 10,  the best approximation is obtained by rounding up:

Therefore the best possible approximation to 1/10 in 754 double precision is :

Dividing both the numerator and denominator by two reduces the fraction to:

Note that since we rounded up, this is actually a little bit larger than 1/10; if we had not rounded up, the quotient 
would have been a little bit smaller than 1/10. But in no case can be exactly 1/10!

So the computer never sees 1/10: what is sees is the exact fraction given above, the best 754 double approximation it
can get

if we multiply that fraction by 10 ** 55, we can see the value out of 55 decimal digits:

meaning that the exact number stored in the computer is equal to  teh decimal value. Instead of displaying the full 
decimal value, many languages (including older version of Python), round the result to 17 significant digits:

The fractions and decimal modules make these calculations easy:

16. Appendix

16.1. Interactive mode

16.1.1 Error Handling

When an error occurs, the interpreter prints an error message and a stack trace. In interactive mode, it then returns 
to the primary prompt; when input came from a file, it exits with a nonzero exit status after printing the stack trace.
(Exception handled by an except clause in a try statement are not errors in this context.) Some errors are 
unconditionally fatal and cause an exit with a nonzero exit; this applies to internal inconsistencies and some cases of 
running out of memory. All messages are written to the standard error stream; normal output from executed commands is 
written to standard output.

Typing the interrupt character (usually Control-C or Delete) to the primary or secondary prompt cancels the input and 
returns to the primary prompt. Typing an interrupt while a command is executing raises the KeyboardInterrupt 
exception, which may be handled by a try statement.

16.1.2. Executable Python scripts

On BSD'ish unix systems, Python scripts can be made directly executable, like shell scripts, by putting the line

#!/usr/bin/env python3.5

(assuming that the interpreter is on the user's PATH) at the beginning of the script and giving the file an executable
mode. The #! must be the first tow characters of the file. On some platforms, this first line must end with Unix-style 
line ending ('\n'), not a Windows ('\r\n') line ending. Note that the hash, or pound, character, '#', is used to start 
a comment in Python.

The script can be given an executable mode, or permission, using chmod command.

On Windows systems, there is no notion of an "executable mode". The python installer automatically associates .py files 
with python.exe so that do a double-click on a python file will run it as a script. The extension can also be .pyw, in
that case, the console window that normally appears is suppressed.

16.1.3. The interactive startup file

When you use Python interactively, it is frequently handy to have some standard commands executed every time the 
interpreter is started. you can do this by setting an environment variable named PYTHONSTARTUP to the name of a file 
containing your start-up commands. This is similar to the .profile feature of the Unix shells.

This file is only read in interactive sessions, not when Python reads commands from a script, and not when /dev/tty is 
given as the explicit source of commands (which otherwise behaves like an interactive session). It is executed in the 
same namespace where interactive commands are executed, so that objects that it defines or imports can be used without 
qualification in the interactive session. You can also change the prompts sys.ps1 and sys.ps2 in this file.

If you want to red an additional start-up file from the current directory, you can program this in the global start-up 
file using code like if os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read()). if you want to use the 
startup file in a script, you must do this explicitly in the script:

16.1.4. The customization modules

Python provides two  hooks to let you customize it: sitecusomize and usercustomize. To see how it works, you need first 
to find the location of your user site-packages directory, Start Python and run this code:

now you can create a file named usercustomize.py in that directory and put anything you want in it. It will affect every
invocation of Python, unless it is started with the -s option to disable the automatic import.

The Python Standard Library

While The Python Language Reference describes the exact syntax and semantics of the Python Language, this library 
reference manual describes the standard library that is distributed with Python. It also describes some of the optional
components that are commonly included in Python distributions.

Python's standard library is very extensive, offering a wide range of facilities as indicated by the long tale of 
contents listed below. The library contains built-in modules (written in C) that provide access to system functionality 
such as file I/O what would otherwise be inaccessible to Python programmers, as well as modules written in Python that 
provide standardized solutions for many leetcode that occur in everyday programming. Some of these modules are 
explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics 
into platform-neutral APIs.

The Python installers for the Windows platform usually include the entire standard library and often also include many 
additional components. For Unix-like operating systems Python is normally provided as collection of packages, so it may 
be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional 
components.

In addition to the standard library, there is a growing collection of several thousand components (from individual 
programs and modules to packages and entire application development frameworks), available from the Python Package 
Index.
    1. Introduction
    2. Built-in Functions
    3. Built-in Constants
        3.1. Constants added by the site module
    4. Built-in Types
        4.1. Truth Value Testing
        4.2. Boolean Operations - and, or, not
        4.3. Comparisons
        4.4. Numeric Types - int, float, complex
        4.5. Iterator Types
        4.6. Sequence Types - list, tuple, range
        4.7. Text sequence types - str
        4.8. Binary Sequence Types - bytes, bytearray, memoryview
        4.9. Set Types - set, frozenset
        4.10. Mapping Types - dict
        4.11. Context Manager Types
        4.12. Other built-in Types
        4.13. Special Attributes
    5. Built-in Exceptions
        5.1. Base classes
        5.2. Concrete exceptions
        5.3. Warnings
        5.4. Exception hierarchy
    6. Text Processing Services
        6.1. string - Common string operations
        6.2. re - Regular expression operations
        6.3. difflib - Helpers for computing deltas
        6.4. textwrap = Text wrapping and filling
        6.5. unicodedata - Unicode Database
        6.6. stringprep -Internet string preparation
        6.7. readline - GUN readline interface
        6.8. rlcoompleter - Completion function for GUN Readline
    7. Binary Data Services
        7.1 struct - Interpret bytes as packed binary data
        7.2. codecs - Codec registry and base classes
    8. Date Types
        8.1. datetime - Basic date and time types
        8.2. calendar - General calendar-related functions
        8.3. collections - Container datatypes
        8.4. collections.abc - Abstract Base Classes for Containers
        8.5. heapq - Heap queue algorithm
        8.6. bisect - Array bisection algorithm
        8.7. array - Efficient arrays of numeric values
        8.8. weakref - Weak references
        8.9. types - Dynamic type creation and names for built-in types
        8.10. copy - Shallow and deep copy operations
        8.11. pprint - Dta pretty printer
        8.12. reprlib - Alternate repr() implementation
        8.13. enum - Support for enumerations
    9. Numeric and Mathematical Modules
        9.1. numbers - Numeric abstract base classes
        9.2. math - Mathematical functions
        9.3. cmath - Mathematical functions for complex numbers
        9.4. decimal - Decimal fixed point and floating point arithmetic
        9.5. fractions - Rational numbers
        9.6. random - Generate pseudo-random numbers
        9.7. statistics - Mathematical statistics functions
    10. Functional Programming Modules
        10.1. itertools - Functions creating iterators for efficient looping
        10.2. functools - Higher-order functions and operations on callable objects
        10.3. operator - Standard operators as functions
    11. File and Directory Access
        11.1. pathlib - Object-oriented filesystem paths
        11.2. os.path - common pathname manipulations
        11.3. fileinput - Iterate over lines from multiple input streams
        11.4. stat - interpreting start() results
        11.5. filecmp - File and Derecotry Comparisons
        11.6. tempfile - Generate temporary files nd directories
        11.7. glob - Unix style pathname pattern expansion
        11.8. fnmatch - Unix filename pattern matching
        11.9. linecache - Random access to text lines
        11.10. shutil - High-level file operations
        11.11. macpath - Mac OS 9 path manipulation functions
    12. Data Persistence
        12.1. pickle - Python object serialization
        12.2. copyreg - Register pickle support functions
        12.3. shelve - Python object persistence
        12.4. marshal - Internal Python object serialization
        12.5. dbm - Interfaces to Unix "databases"
        12.6. sqlite3 - DB-API 2.0 interface for SQLite databases
    13. Data Compression and Archiving
        13.1. zlib - Compression compatible with gzip
        13.2. gzip - Support for gzip files
        13.3. bz2 - Support for bzip2 compression
        13.4. lzma - compression using the lZMA algorithm
        13.5. zipfile - work with zip archives
        13.6. tarfile - read and write tar archive files
    14. File Formats
        14.1. csv - SSV file reading and writing
        14.2. configparser - configuration file parser
        14.3. netrc - netrc file processing
        14.4. xdrlib - encode and decode xdr data
        14.5. plistlib - generate and parse max osx .plist files
    15. Cryptographic Services 
        15.1. hashlib - Secure hashes and message digests
        15.2. hmac - keyed-hashed for message authentication
    16. generic operating system services
        16.1. os - Miscellaneous operating system interfaces
        16.2. io - Core tools for working with steams
        16.3. time - Time access and conversions
        16.4. argparse - Parser for command-line options, arguments and sub-commands
        16.5. getopt - C-style parser for command line options
        16.6. logging - Logging facility for Python
        16.7. logging.config - Logging configuration
        16.8. logging.handlers - Logging handlers
        16.9. getpass - Portable password input
        16.10. curses - Terminal handling for character-cell displays
        16.11. curses.textpad - Text input widget for curses programs
        16.12. cruses,ascii - Utilities for ascii characters
        16.13. curses.panel - A panel stack extension for curses
        16.14. platform - Access to underlying platform's identifying data
        16.15. errno - Standard errno system symbols
        16.16. ctypes - A foreign function library for Python
    17. Concurrent Execution
        17.1. threading - Thread-based parallelism
        17.2. multiprocessing - Processed-based parallelism
        17.3. The concurrent package
        17.4. concurrent.futures - Launching parallel tasks
        17.5. subprocess - Subprocess management
        17.6. sched - Event scheduler
        17.7. queue - A synchronized queue class
        17.8. dummy_threading - Drop-in replacement for the threading module
        17.9. _thread - low-level threading api
        17.10. _dummy_thread - drop-in replacement for the _thread module
    18. Interprocess Communication and Networking
        18.1. socket - low-level networking interface
        18.2. ssl - TLS/SSL wrapper for socket objects
        18.2. select - waiting for i/o completion
        18.4. selectors - high-level i/o multiplexing
        18.5. asyncio - Asynchronous i/o, event loop, coroutines and tasks
        18.6. asyncore - Asynchronous socket handler
        18.7. asynchat - Asynchronous socket command /response handler
        18.8. signal - set handlers for asynchronous events
        18.9. mmap - Memory-mapped file support
    19. Internet Data handling
        19.1. email - An email and MINE handling package
        19.2. json - JSON encoder and decoder
        19.3. mailcap - Mailcap file handling
        19.4. mailbox - Manipulte mailboxes in various formats
        19.5. minetypes - Map filenames to MINE types
        19.6. base64 - Base16, Bse32, Base64, Base85 Data Encodings
        19.7. binhex - Encode and decode binhex4 files.
        19.8. binascii - convert between binary and ascii
        19.9. quopri - encode and decode MINE quoted-printable data
        19.10. uu - Encode and decode uuencode files
    20. Structured Markup Processing Tools
        20.1. html - HyperText Markup Language support
        20.2. html.parser - Simple HTML and XHTML parser
        20.3. html.entities - Definitions of HTML general entities
        20.4. XML Processing Modules
        20.5. xml.etree.ElementTree - the elementtree xml api
        20.6. xml.dom - The document object model api
        20.7. xml.dom.minidom - minimal dom implementation
        20.8. xml.dom.pulldom - support for building partial dom trees
        20.9. xml.sax - support for sax2 parsers
        20.10. xml.sax.handler - Base classes for sax handlers
        20.11. xml.sax.saxutils - sax utilities
        20.12. xml.sax.xmlreader - interface for xml parsers
        20.13. xml.parsers.expat - fast xml parsing using expat
    21. internet protocols and support
        21.1. webbrowser - convenient web-browser controller
        21.2. cgi - common gateway interface support
        21.3. cgitb - traceback manager for cgi scripts
        21.4. wsgiref - wsgi utilities and reference implimentation
        21.5. urllib - url handling modules
        21.6. urllib.request - extensible library for opening urls
        21.7. urllib.response - response classes used by urllib
        21.8. urllib.parse - Parse urls into components
        21.9. urllib.error - exception classes raised by urllib.request
        21.10. urllib.robotparser - parer for robots.txt
        21.11. http - http moduules
        21.12. http.client - http protocal client
        21.13. ftplib - ftp protocol client
        21.14. poplib - pop3 protocol client
        21.15. imaplib - imap4 protocol client
        21.16. nntplib - nntp protocol client
        21.17. smtplib - smtp protocol client
        21.18. smtpd - smtp server
        21.19. telnetlib - Telnet client
        21.20. uuid - uuid objects according to RFC 4122
        21.21. socketserver - A framework for network servers
        21.22. http.server - http servers
        21.23. http.cookies - http state management
        21.24. http.cookiejar - cookie handling for http clients
        21.15. xmlrpc - xmlrpc server and client modules
        21.26. xmlrpc.client - xml-rpc client access
        21.27. xmlrpc.server - basic xml-rpc servers
        21.28. ipaddress - ipv4/ipv6 manipulation library
    22. Multimedia service
        22.1. audioop - manipulate raw audio data
        22.2. aifc - read and write aiff and aifc files
        22.3. sunau -read and write sun au files
        22.4. wave - read and write wav files
        22.5. chunk - read and write wav files
        22.6. colorsys - conversions between color systems
        22.7. imghdr - determine the type of an image
        22.8. sndhdr - determine type of sound file
        22.9. ossaudiodev - access to oss-compatible audio devices
    23. internationalization
        23.1. gettext - multilingual internationalization services
        23.2. locale - Internationalization services 
    24. Program Frameworks
        24.1. turtle - turtle graphics
        24.2. cmd - support for line-oriented command interpreters
        24.3. shlex - simple lexical analysis
    25. Graphical user interfaces with TK
        25.1. tkinter - Python interface to Tcl/TK
        25.2. tkinter.ttk - Tk themed widgets
        25.3. tkinter.tix - extension widgets for tk
        25.4. tkinter.scrolledtext - scrolled text widget
        25.5. IDLE
        25.6. other graphical user interface packges
    26. Development tools
        26.1. typing - support for type hints
        26.2. pydoc - documentation generator and online help system
        26.3. doctest - test interactive python examles
        26.4. unittest - unit testing framework
        26.5. unittest.mock - mock object library
        26.6. unittest.mock - getting started
        26.7. 2to3 - automated python 2 to 3 code translation
        26.8. test - regression tests package for python
        26.9. tet.support - utilities for the python test suite
    27. Debugging and profiling
        27.1 bdb - Debugger framework
        27.2. faulthandler - Dump th python traceback
        27.3. pdb - the python debugger
        27.4. the python profilers
        27.5. timeit - measure execution time of small code snippets
        27.6. trace - Trace or track python statement execution
        27.7. tracemalloc - trace memory allocations
    28. Software packaging and distribution
        28.1. distutils - building and installing python modules
        28.2. ensurepip - bootstrapping the pip installer
        28.3 venv - creation of vertual environments
        28.4. zipapp - Mange executable python zip archives
    29. Python runtime services
        29.1. sys - system-specific parameters and functions
        29.2. sysconfig - provide access to python's configuration information
        29.3. builtis - built-in objects
        29.4. __main__ - top-level script environment
        29.5. warnings - warning control
        29.6. contextlib - utilities for with-statement contexts
        29.7. abc - abstract base classes
        29.8. atexit - exit handlers
        29.9. traceback - print or retrieve a stack traceback
        29.10. __future__ - future statement definitions
        29.11. gc - garbage collector interface
        29.12. inspect - inspect live objects
        29.13. site - site-specific configuration hook
        29.14. fpectl - Floating point exception control
    30. Custom Python Interpreters
        30.1. code - interpreter base classes
        30.2. codeop - compile python code
    31. Importing modules
        31.1. zipiimmport - import modules from zip archives
        31.2. pkgutil - package extension utility
        31.3. modulefinder - find modules used by a script
        31.4. runpy - locating and executing python modules
        31.5. importlib - teh implementation of import
    32. Python language services
        32.1. parser - access python parser trees
        32.2. ast - abstract syntax trees
        32.3. symtable - access to the compiler's symbol tables
        32.4. symbol - constants used with python parse trees
        32.5. token - constants used with python parse trees
        32.6. keyword - testing for python keywords
        32.7. tokenize - tokenizer for python source
        32.8. tabnanny - detection of ambiguous indentation
        32.9. pyclbr - python class browser support
        32.10. py_compile - compile Python source files
        32.11. compileall - byte-compile python libraries
        32.12. dis - disassembler for python bytecode
        32.13. pickletools - tools for pickle developers
    33. Miscellaneous services
        33.1 formatter - generic output formatting
    34. MS windows specific services
        34.1. msilib - read and write microsoft installer files
        34.2. msvcrt - useful routines from the ms vs++ runtime
        34.3. winreg - windows registry access
        34.4. winsound - sound-plying interface for windows
    35. Unix specific services
        35.1. posix - the most common posix system calls
        35.2. pwd - the password database
        35.3. spwd - the shadow password database
        35.4. grp - the group database
        35.5. crypt - function to check unix passwords
        35.6. termios - posix style tty control
        35.7. tty - terminal control functions
        35.8. pty - pseudo-terminal utilities
        35.9. fcntl - teh fcntl and ioctl sytem calls
        35.10. pipes - interface to shell pipelines
        35.11. resource - resource usage information
        35.12. nis - interface to sun's nis (yellow pages)
        35.13. syslog - unix syslog library routines
    36. Superseded Modules
        36.1. optparse -parse for command line options
        36.2. imp - access the import internals
    37. undocumented Modules
        37.1. Platform specific modules
        
1. Introduction

The "Python library" contains several diffeent kinds of commponets.

It contains data types that would normally be considered part of the core of a language, such as numbers and lists. For 
these types, the python language core defines the form of literals and places osme constraints on their semantics, 
but does not fully define the semantics. (On the other hand, the language core does define syntactic properties like 
the spelling and priorities of operators.)

The library also contains built-in functions and exceptions - objects that can be used by all python code without the
need of an import statement. Some of these are defined by the core language, but many are not essential for the core
semantics and are only described here

The bulk of the library, however, consists of a collection of modules. There are many ways to dissect this collection.
Some modules are written in C and built in to the Python interpreter; others are written in Python and imported in 
source from. Some modules provide interfaces that are highly specific to Python. like printing a stack trace; some 
provide interfaces that are specific to particular operating systems, such as access to specific hardware; other 
provide interfaces that are specific to a particular application domain, like the world wide web. Some modules are 
available  in all versions and ports of Python; others are only available when the underlying system supports or 
requires them; yet others are available only when a particular configuration option was chosen at the time when python
was compiled and installed.

This manual is organized "from the inside out:? it first describes the built-in functions, data types, and exceptions.
and finally the modules, grouped in chapters of related modules.

This means that if you start reading this manual from the start, and skip to teh next chapter when you get bored, you 
will get a reasonable  overview of the available modules and applications areas that are supported by the Python 
library. Of course, you dont' have to read it like a novel - you can also browser the table of contents (in front fo the 
manual), or look for a specific function, module or term in th index ( in the back). And finally, if you enjoy learning 
about random subjects, you choose a random page number (see module random) and read a section to two, regardless of the 
order in which you read the sections of this manual, it helps to start with chapter built-in functions, as the 
remainder of the manual assumes familiarity with this mateial.

Let th show begin!

2. built-in functions

The python interpreter has a number of functions and types built into it and are always available. They are listed here
in alphabetical order.

abs(x)
    Return the absolute value fo a number. The argument may be an integer or floating point number. If the argument is 
    a complex number, its magnitude is returned.
    
all(iterable)
    Return True if all elements of the iterable are true (or if the iterable is empty), Equivlaent to
"""


def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


"""
any(iterable)
    Return True if any element of the iterable is true. If teh iterable is empty, return False. Equivalent to:
"""


def any(iterable):
    for element in iterable:
        if element:
            return  True

    return False

