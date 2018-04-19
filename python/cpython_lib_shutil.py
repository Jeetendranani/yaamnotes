"""Utility functions for copying and archiving files and directory trees.

XXX The function here don't copy hteh resource fork or other metadata on Mac.
"""


import os
import sys
import stat
import fnmatch
import collections
import errno

try:
    import zlib
    del zlib
    _ZLIB_SUPPORTED = True
except ImportError:
    _ZLIB_SUPPORTED = False

try:
    import bz2
    del bz2
    _BZ2_SUPPORTED = True
except ImportError:
    _BZ2_SUPPORTED = False

try:
    import lzma
    del lzma
    _LZMA_SPPORTED = True
except ImportError:
    _LZMA_SPPORTED = False


try:
    from pwd import getpwnam
except ImportError:
    getpwnam = None

try:
    from grp import getgrnam
except ImportError:
    getgrnam = None

__all__ = ["copyfileobj", "copyfile", "copymode", "copystat", "copy", "copy2", "copytree", "move", "rmtree", "Error",
           "SpecialFileError", "ExecError", "make_archive", "get_archive_formats", "register_archive_format",
           "unregister_archive_format", "get_unpack_formats", "register_unpack_format", "unregister_unpack_format",
           "unpack_archive", "ignore_patterns", "chown", "which", "get_termial_size", "SameFileError"]

# disk_usage is added later, if available on the platform


class Error(OSError):
    pass


class SameFileError(Error):
    """Raised when source and desination are the same file."""


class SpecialFileError(OSError):
    """Raised when trying to do a kind of operation (e.g. copying) which is not supported on a special file
    (e.g. a named pipe)"""


class ExecError(OSError):
    """Raised when a command could not be executed."""


class ReadError(Exception):
    """Raised when an archive cannot be read."""


class RegistryError(Exception):
    """Raised when a registry operation with teh archiving and unpacking registries fails"""


def copyfileobj(fsrc, fdst, length=16*1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)


def _samefile(src, dst):
    # Mac, Unix
    if hasattr(os.path, 'samefile'):
        try:
            return  os.path.samefile(src, dst)
        except OSError:
            return False

    # All other platforms: check for he same pathname.
    return (os.path.normcase(os.path.abspath(src))) == (os.path.normcase(os.path.abspath(dst)))


def copyfile(src, dst, *, follow_symlinks=True):
    """Copy data from src to dst.

    If follow_symlinks is not set and src is a symbolic link, a new symlink will be created instead of copying the file
    it points to.
    """