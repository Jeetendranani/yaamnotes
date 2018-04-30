"""
6. Text Processing Services

The modules described in this chapter provide a wide range of string manipulation operations and other test processing
services.

The codecs module described under binary data services is also highly relevant to text processing. In addition, see
the documentation for python's built-in string in Text Sequence Type - str.

6.1 string - common string operations

6.1.1 string constants

string.ascii_letters
    The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale
    dependent.

string.ascii_lowercase
    the lowercase letters 'abcdefghijklmnopqrstuvwxyz'. this values is not locale dependent and will not cange

string.ascii_uppercase

string.digits

string.hexdigits

string.octdigits

string.punctuation

string.whitespace

6.1.2 custom string formatting

The build-in string class provides the ability to do complex variable substitutions and value formatting via the
format() method described in PEP 3101. The Formatter class in the string module allows you to create and customize your
own string formatting behaviors using the same implementation as the built-in format() method.

class string.Formatter
The Formatter class has the following public methods;

    format()

    vformat()

    parse()

    get_field()

    get_value()

    check_unused_args()

    format_field()

    convert_field()

6.1.3 Format string syntax


6.2 re regular expression


6.3 difflib - Helpers for computing deltas

This module provides classes and functions for comparing sequences. It can be used for example, for comparing files,
and can produce difference information in various formats, including HTML and context and unified diffs. For comparing
directories and files, see also, the filecmp module.

class difflib.SequenceMatcher

class difflib.Differ

class difflib.HtmlDiff

difflib.context_diff

difflib.get_close_matches

difflib-ndiff

difflib.restore

difflib.unified_diff

difflib.diff_bytes

difflib.IS_LINE_JNK

difflib.IS_CHARACTER_JUNK
"""