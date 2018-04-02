"""
688. Longest Univalue Path

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may
or may not pass through teh root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:
            5
           / \
          4   5
         / \   \
        1   1   5

Output:
2

Example 2:
Input:
            1
           / \
          4   5
         / \   \
        4   4   5

Output:
2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""

class Solution:
    def longest_univalue_path(self, root):
        """
        Time Complexity: O(n), where N is teh number of nodes in the tree. We process every node once.
        Space Complexity: O(h), where h is the height of the tree, our recursive call stack could be up to H layers
        deep.
        :param root:
        :return:
        """

        if root is None:
            return 0

        def arrow_length(root):
            left_length = arrow_lenght(root.left)
            right_length = arrow_length(root.right)
            left_arrow = 0
            right_arrow = 0
            if root.right and root.val == root.left.val:
                left_length = left_length + 1
            if root.right and root.val == root.right.val:
                right_length = right_length + 1
            self.ans = max(self.ans, left_length + right_length)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans


"""
Approach 1: Recursion

Intuition

We can think of any path (of nodes with the same values) as up to two arrows extending from its root. 

Specifically, the root of a path wil be the unique node such that the parent of the node does not appear in the path,
and an arrow will be a path where the root only has one child node in the path.

Then, for each node, we want to know what the longest possible arrow extending left, and the longest possible arrow 
extending right? We can solve this using recursion.

Algorithm

Let arrow_ength(node) be the length of the longest arrow that extends from  the node. That will be 1 + arrow_length(
node.left) if node.left exists and has the same value as node. Similarly for the node.right case.

While we are computing arrow lengths, each candidate answer will be the sum of the arrows in both directions from that 
node. We record these candidate answers and return the best one.
"""

"""
6.2. Standard Modules

Python comes with a library of standard modules, described in a separate document, the Python Library Reference 
("Library Reference" hereafter). Some modules are built into the interpreter; these provide access to operations that 
are not part of the core of the language but are nevertheless built-in, either for efficiency or to provide access to
operating system primitives such as system calls. the set of such modules is a configuration option which also 
depends on the underlying platform. For example, the winreg module is only provide on Windows systems. One particular 
module deserves some attention: sys, which is built into every Python interpreter. The variables sys.ps1 and sys.ps2 
define the strings used as primary and secondary prompts:

These two variables are only defined if the interpreter is in interactive mode.

The variable sys.path is a list of strings that determines the interpreter's search path for modules. It is initialized 
to default path taken from the environment variable PYTHONPATH, or from a built-in default if PYTHONPaTH is not set.
You can modify it using standard list operations:

6.3. The dir() function

The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:

Without arguments, dir() lists the names you have defined currently:

Note that it is lists all types of names: variables, modules, functions, etc.

dir() does not list the names of built-in functions and variables. If you want to a list of those, they are defined in 
the standard module builtins:

6.4. Packages

Packages are a way of structuring Pythons's module namespace by using "dotted module names". For example, the module 
name A.B designates a submodule named B in package named A. Just like the use of modules saves the authors of different
modules from having to worry about each other's global variable names, the use of dotted module names saves the authors 
of multi-module packages like NumPy or the Python Imaging Library from having to worry about each other's module names.

Suppose you want to design a collection of modules (a "package") for the uniform handling of sound files and sound data.
There are many different sound file formats (usually recognized by their extension, for example: .wav, .aiff, .au), so 
you may need to create and maintain a growing collection of modules for the conversion between the various file formats.
There are also many different operations you might want to perform on sound data (such as mixing, adding echo, applying 
an equalizer function, creating an artificial stereo effect), so in addition you will be writing a never-ending stream 
of modules to perform these operations. Here's a possible structure for your package (expressed in terms of a 
hierarchical filesystem):

When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

The __init__.py file are required to make python treat the directory as containing packages; this is done to prevent
directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the 
module search path. In the simplest case, __init__.py can just be an empty file, but it can also execute initialization
code for the package or set the __all__ variable, described later.

Users of the package can import individual modules from the package , for example:

This loads the submodule sound.effects,echo. It must be referenced with its full name.

An alternative way of importing the submodules is:

This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:

Yet another variation is to import the desired function or variable directly:

Again, this loads the submodule echo, but this makes its function echofilter() directly available:

Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, or 
some other name defined in the package, like a function, class or variable. The import statement first tests whether 
the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, 
an ImportError exception is raised.

Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the 
last item can be a module or a package but can't be a class or function or variable defined in the previous item.

6.4.1. Importing * from a package

Now what happens when the use write from sound.effects import *? Ideally, one would hope that this somehow goes out to 
the filesystem, finds submodules are present in the package, and imports them all. This could take a long time and 
importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly 
imported.

The only solution is for the package author to provide an explicit index of the package. The import statement uses the 
following convention: if a package's __init__.py code defines a list named __all__. it is taken to be the list of module
names that should be imported when from package import * is encountered. It is up to the package author to keep this 
list up-to-date when a new version of teh packages is released. Package authors may also decide not to support it, if 
they don't see a use for importing * from their package, For example, the file sound/effects/__init__.py could contain 
the following code:

__all__ = ['echo', 'surround', 'reverse']

This would mean that from sound effects import * would import the three named submodules of the sound package.

If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package 
sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly 
running any initialization code in __init__.py) and then imports whatever names re defined in the package. This 
includes any names defined (and submodules explicitly loaded) by __init__.py. It also includes any submodules of the 
package that where explicitly loaded by previous import statements. Consider this code:

In this example, the echo and surround modules are imported in the current namespace because they are defined in the 
sound.effects package when the from ... import statements is executed. (This also works when __all__ is defined.)

Although certain modules are designed to export only names that follow certain patterns when you use import *, it is 
still considered bad practice in production code.

Remember, there is nothing wrong with using from package import specific_submodule! In fact, this is the recommended
notation unless the importing modue needs to use submodules with the same name from different packages.

6.4.2. Intra-package references

When packages are structured into subpackages (as with the sound package in the example), you can use absolute imports 
to refer to submodules of siblings packages, if the modules sound.filters.vocoder needs to use the echo modules in the 
sounds.effects package, it can use from sound.effects import echo.

You can also write relative imports, with the form modules import name form of import statement. These imports use 
leading dots to indicate the current and parent packages involved in the relative import. From the surround module for 
example, you might use:

from . import echo
from .. import formats
from ..filters import equalizer

Note that relative imports are based on the name of the current module. Since the name of the main module is always
"__main__", modules intended for use as the main module of a Python application must always use absolute imports.

6.4.2. Packages in Multiple Directories

Packages support one more special attribute, __path__. This is initialized to be a list containing the name of the 
directory holding the package's __init__.py before the code in that file is executed. This variable can be modified;
doing so affects suture searches for modules and subpackages contained in the package.

While this feature is not often needed, it can be used to extend the set of modules found in a package.

7. Input and output

There are several ways to present the output of a program; data can be printed in a human-readable form, or written to
a file for future use. This chapter will discuss some of the possibilities;

7.1. Fancier output formatting

So far we've encountered two ways of writing values: expression statements and the print() function. (A third way is 
using the write() method of file objects; the standard output file can be referenced as sys.stdout. See the library
reference for more information on this.)

Often you'll want more control over the formatting of your output then simply printing space-separated values. There are
tow ways to format your output; the first way is to do all the string handling yourself;
using string slicing and concatenation operations you can create any layout you can image. The string type has some
methods that perform useful operations for padding strings to a given column width; these will be discussed shortly. 
The second way is to use the str.format() method.

The string module contais a Template class which offers yet another way to substitute values into strings.

One question remains, of course: how do you convert values to string? Luckily, Python has ways to convert any value to 
a string: pass it to the repr() or str() functions.

The str() function is meant to return representations of values which are fairly human-readable, while repr() is meant 
to generate representations of which can be read by the interpreter (or will force a SyntaxError if there is no 
equivalent syntax). For objects which dont' have a particular representation fo human consumption, str() will return 
the same value as repr(). Many values, such as numbers or structures like list and dictionary, have the same 
representation using either function. Strings, in particular, have two distinct representations.

Here are two ways to write a table of squares and cubes:

This example demonstrates the str.rjust() method of string objects, which right-justifies a string in a field of a
given width by padding it with spaces on the left. There are similar methods atr.ljust() and str.center(). These 
methods do not write anything, they just return a new string. If the input string is too long, they dont' truncate it, 
but return it unchanged; this will mess up your column lay-out but that's usually better than the alternative, which 
would be lying about a value. (if you really want truncation you can always add a slice operation. as in 
x.ljust(n)[:n].)

There is another method, str.zfill(), which pds a numeric string on left with zeros, it understands about plus and minus
signs:

Basic usage of the str.format() method looks like this:

This brackets and characters within them (called format fields) are replaced with the objects passed into the 
str.format() method. A number in the brackets can be used to refer to the position of the object passed into the 
str.format() method.

If keyword argument are sued in the str.format() method, their values are referred to by using the name of the argument.

Positional and keyword arguments can be arbitrarily combined:

'!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is 
formatted.

An optional ':' and format specifier can follow the field name. This allows greater control over the values is 
formatted. The following example rounds Pi to three places after the decimal.

Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for 
making tables pretty.

If you have a really long format string that you don't want to split up, it would be nice if you could reference the 
variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square
brackets '[]' to access the keys.

This could also be done by passing the table as keyword arguments with the '**' notation.

This is particularly useful in combination with the built-in function vars(), which returns a dictionary containing all
local variables.

For a complete overview of string formatting with str.format(), see Format String Syntax.

7.1.1. Old string formatting

The % operator can also be used for string formatting. It interprets the left argument much like a sprintf() - style 
format string to be applied to the right argument, and returns the string resulting from this formatting operation.
For example:

More information can be found in the printf-style String Formatting section.

7.2. Reading and Writing Files

open() returns a file object, and is most commonly used with two arguments: open(filename, mode).

>>> f = open('workfile', 'w')

The first argument is a string containing the filename. The second arguments is another string containing a few
characters describing the way in which the file be used. mode can be 'r' when the file will only be read, 'w' for only 
writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to
the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is 
optional; 'r' will be assumed if it's omitted.

Normally, files are opened in text mode, that means, you read and write stings from and to the file, which are encoded 
in a specific encoding. If encoding is not specified, the default is platform dependent (see open()). 'b' appended to 
the mode opens the file in binary mode: now the data is read and written in the form of bytes objects. This mode should
be used for all files that don't contain text.

In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to 
just \n. When writing in text mode, the default is convert occurrences of \n back to platform-specific line endings. 
this behind-the-scenes modification to file data is fine or test files, but will corrupt binary data like that in JPEG
or EXE files. Be very careful to use binary mode when reading and writing such files.

It is good practice to use the with keyword when dealing with the file objects. The advantage is that the file is 
properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter
than writing equivalent try-finally blocks:

If you're not using the with keyword, then you should call f.close() to close the file and immediately free up an system
resource used by it. If you don't explicitly close a file, Python's garbage collector will eventually destroy the object
and close the open file for you, but the file may stay open for a while. Another risk is that different Python
implementations will do this clean-up at different times.

After a file object is closed, either by a with statement or by calling f.close(), attempts to use the file object will
automatically fail.

7.2.1. Methods of file objects

The rest of the examples in this section will assume that a file object called f has already been created.

To read a file's contents, call f.read(size), which read some quantity of date and returns it as a string (in text mode)
or bytes object (in binary mode). size is an optional numeric argument. When size is omitted or negative, the entire
contents of the file will be read and returned; it's your problem if the file is twice as large as your machine's 
memory. Otherwise, at most size bytes are read and returned. If the end of the file has been reached, f.read() will 
return an empty string ('').

>>> f.read()
'This is the entire file.\n'
>>> f.read()
''

f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only
omitted on the last line of the file if the file doesn't end in a newline. this makes the return value unambiguous;
if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by 
'\n', a string containing only a single newline.

for reading lines from a file. you can loop over the file object. This is memory efficient, fast, and leads to simple
code: 
"""


for line in f:
    print(line, end='')

"""
If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

f.write(string) writes the contents of string to the file, returning the number of characters written.

Other tyoes objects need to be converted - either to a string (in text mode) or a bytes object (in binary mode) - before
writing them.

f.tell() returns an integer giving the file object's current position in the file represented as number of bytes from 
the beginning of the file when in binary mode and an opaque number when in the text mode.

To change the file object's position, use f.seek(offset, from_what). The position is computed from adding offset to a
reference point; the reference point is selected by the from_what argument. A from_what value of 0 measures from the 
beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. 
from_what can be omitted and default to 0, using the beginning of the file as the reference point.

In text files (those opened without a b in the mode string), only seeks relative to the beginning of the file are 
allowed (the exception being seeking to the very file end with seek(0, 2)) and the only valid offset values re those
returned from the f.tell(), or zero, any other offset value produces undefined behaviour.

File objects have some additional methods, such as isatty() and truncate() which are less frequently used; consult the 
Library Reference for a complete guide to file objects.

7.2.2. Saving structured data with json

String can easily be written to and read from a file. Numbers take a bit more effort, since the read() method only 
return strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its 
numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and 
serializing by hand becomes complicated.

Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows 
you to use the popular data interchange format called JSON (JavaScript Object Notation). The standard module called
json can take Python data hierarchies, and convert them to string representations; this process is called serializing.
Reconstructing the data from teh string representation is called deserializing. Between serializing and deserializing,
the string representing the object may have been stored in a file or data, or send over a network connection to some 
distant machine.

Note: The JSON format is commonly used by modern applications to allow for data exchange. Many programmers are already
familiar with it, which makes it a good choice for interoperability.

If you have an object x, you can view its JSON string representation with a simple line of code:

Another variant of the dumps() function, called dump(), simply serializes the objects to a tet file. So if f is a text
file object opened for writing, we can do this:

json.dump(x, f)

To decode the object again, if f is a text file object which has been opened for reading:

x = json.load(f)

This simple serialization technique can handle lists and dictionaries, but serializing arbitrary class instance in JSON
requires a bit of extra effort. The reference for the json module contains an explanation of this.

See also: pickle - the pickle module

Contrary to JSON, pickle is a protocol which allows the serialization of arbitrarily complex Python objects. As such, it 
is specific to Python and can be used to communicate with applications written in other languages, it is also insecure 
by default: deserializing pickle data coming from an untrusted source can execute arbitrary code, if the data was 
crafted by a skilled attacker.

8. Errors and exceptions

Until now error messages haven't been more than mentioned, but if you have tried out the examples you have probably
seen some. There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

8.1. Syntax Errors

Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still 
learning Python:

The parser repeats the offending line and displays a little 'arrow' pointing at teh earliest point in the line where the 
error ws detected. The error is caused by (or at least detected at) the token preceding the arrow: in the example, the 
error is detected at the function print(), since a colon (':') is missing before it. File name and line number are 
printed so you know where to look in case the input came from a script.

8.2. Exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is mode to execute it. 
Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to 
handle the in Python programs. Most exceptions are not handled by programs, however, and result in error messages as 
shown here:

The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed 
as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string printed as 
the exception type is the name of the built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception and what caused it.

The preceding part of the error message shows the context where the exception happened, in the form of stack traceback.
In general it contains a stack traceback listing source lines; however, it will not display lines read from standard 
input.
Built-in Exceptions lists the built-in exceptions and their meanings.

8.3. Handling Exceptions

It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user 
for input until a valid integer has been entered, but allows teh user ti interrupt the program (using Control - C or 
whatever the operating system supports); note that a user-generated interruption is signalled by raising the 
KeyboardInterrupt Exception.
"""


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")


"""
The try statement works as follows. 
    - First, the try clause (the statement(s) between the try and except keywords) is executed.
    
    - if no exception occurs, the except clause is skipped and execution of the try statement is finished.
    
    - If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type 
    matches the exception named after the except keyword, the except clause is executed, and then execution continues 
    after the try statement.
    
    - If an exception occurs which does not match the exception named in the except clause, it is passed on to outer 
    try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown
    above.
    
A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler
will be executed. Handlers only handle exceptions tht occur in the corresponding try clause, not in other handlers of 
the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:

A class in an except Clause is compatible with an exception if it is the same class or base class thereof (but not the 
other way around - an except clause listing a derived class is not compatible with a base class). For example, the 
following code will print B, C, D in that order:
"""


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')


"""
Note that if the except clauses were reversed (with except B first), it would have printed B, B, B - the first matching
except clause is triggered.

The last except class may omit the exception names(s), to serve as a wildcard. Use this with extreme caution, since it 
is easy to mask a real programming error in this way! it can also be used to print an error message and then re-raise 
the exception (allowing a caller to handle the exception as well):
"""