"""
816. Ambiguous Coordinates

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and
spaces, and ended up with the string S. Return a list of strings representing all possibilities for what our original
coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00",
"1.0", "001", or any other number that can be represented with less digits. Also, a decimal point within a number
occurs without at least one digit occurring before it, so we never started with numbers like '.1'.

The final answer list can be returned in any order. Also note that all coordinates in the final answer have exactly one
space between them (occurring after the comma.)

Example 1:

input: "(123)"
output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

example 2:

Input: "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation:
0.0, 00, 0001 or 00.01 are not allowed.

example 3:

Input: "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

Example 4:

Input: "(100)"
Output: [(10, 0)]
Explanation:
1.0 is not allowed.
"""
import itertools


class Solution:
    def ambiguous_coordinates(self, S):
        def make(frag):
            N = len(frag)
            for d in range(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if (not left.startswith('0') or left == '0') and not right.endswith('0'):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]
        return ["{}, {}".format(*cand) for i in range(1, len(S))
                for cand in itertools.product(make(S[:i], make(S[i:])))]


"""
4.7. test sequence type - str

textual data in python is handled with str objects, or strings. Strings are immutable sequences of Unicode code point.
String literals are written in a variety of ways:

- Single quotes:
- Double quotes:
- Triple quoted:

Triple quoted string may span multiple lines - all associated whitespace will be included in the string literal.

String literals that are part of single expression and have only whitespace between them will be implicitly converted 
to a string literal. That is, ("span" "eggs") == "span eggs".

See String and Bytes literals for more about the various forms of string literal, including supported escape sequences,
and the r("raw") prefix that disables most escape sequence processing.

String may also be created from other objects using the str constructor.

Since there is no separate "character" type, indexing a string produces strings of length 1. That is, for a non-empty 
string s, s[0] == s[0:1]

There is also no mutable string type, but str.join() or io.StringIO can be used to efficiently construct strings from 
multiple fragments.

Changed in version 3.3: For backwards compatibility with Python 2 series, the u prefix is once again permitted on 
string literals. It has no effect on the meaning of string literals and cannot be combined with the r prefix.

class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
    Return a string version of object, if object is not provided, return the empty string. Otherwise, the behavior of 
    str() depends on whether encoding or errors is given, as follows.
    
    If neither encoding nor errors is given, str(object) returns object.__str__(), which is the "informal" or nicely 
    printable string representation of objects, this is the string itself. If object does not have a __str__() method,
    then str() falls back to returning repr(object).
    
    If at least one of encoding or errors is given, object should be a bytes-like object (e.g. bytes or bytearray). In
    this case, if object is a bytes (or bytearray) object, then str(bytes, encoding, errors) is equivalent to 
    bytes.decode(encoding, errors). Otherwise, the bytes object underlying the bugger object is obtained before calling 
    bytes.decode(). See Binary sequences types - bytes, bytearray, memoryview and buffer protocol for information on 
    buffer objects.
    
    Passing a bytes object to str() without the encoding or errors arguments falls under the first case of returning
    the informal string representation (see also the -b command-line option to Python).
    
4.7.1. String Methods

Strings implement all of the common sequence operations. along with the additional methods described below.

Strings also support two styles of string formatting, one providing a large degree of flexibility and customization
(see str.format(), Format String Syntax and Custom string formatting) and the other based on C printf style formatting
that handles a narrower range of types and is slightly harder to use correctly, but it often faster for the cases it
can handle (print-style string formatting).

The text processing service section of the standard library covers a number of other modules provide various text 
related utilities (including regular expression support in the re module).

str.capitalize()
    Return a copy of the string with its first character capitalized and the rest lower-cased.
    
str.casefold()
    Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
    
    Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in 
    a string. For example, the German lowercase letter 'ß' is equivalent to 'ss'. Since it is already lowercase, 
    lower() would do nothing to 'ß'; caosefold() coverts it to 'ss'.
    
    The casefolding algorithm is described in sectoin 3.13 of Unicode Standard.
    
str.center(width[, fillcar])
    Return centered in a string of length with, Padding in done using the specified fillchar (default is an ASCII 
    space). The original string is returned if width is less than or equal to len(s).
    
    
str.count(sub[, start[, end]])
    Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments 
    start and end are interpreted as in slice notation.
    
str.encode(encoding = 'utf-8', errors='strict')
    Return an encoded version of the string as bytes object. Default encodings is 'utf-8'. errors may be given to set 
    a different error handling schema. The default for errors is 'strict', meaning that encoding errors raise a 
    UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any other 
    name registered via codecs.register_error(), see section Error Handlers. For a list of possible encodings, see
    section standard encodings.
    
str.endswith(suffix[, start[, end]])
    Return True if the string ends with the specified suffix, otherwise return False. suffix can also be tuple of 
    suffixes to look for. With optional start, test beginning at the position, with optional end, stop comparing at 
    that position.
    
str.expandtabs(tabsize=8)
    Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current
    column and the given tab size. Tab positions occur every tabsize characters (default is 8, giving tab positions
    at columns 0, 8, 16 and so on).  to expand the string, the current columns is set to zero and the string is 
    examined character by character. If the character is a tab(\t), one of more spaces characters are inserted in the 
    result until the current columns is equal to the next tab position. (The tab character itself is not copied.) If 
    the character is newline (\n) or return (\r), it is copied and the current column is reset to zero. Any other 
    characters is copied unchanged and the current columns is incremented by one regardless of how the character is 
    represented when printed.
"""
