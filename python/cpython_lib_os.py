r"""Os routines for NT and posix depending on what system we're on.

This exports:
    - all functions from posix or nt, e.g. unlink, stat, etc.
    - os.path is either posixpath or ntpath
    - os.name is either 'posix' or 'nt'
    - os.curdir is a string representing the current directory (always '.')
    - os.pardir is a string representing the parent directory (always '..')
    - os.sep is the (or a most common) pathname separator ('/' or '\\')
    - os.extsep is the extension separator (always '.')
    - os.altsep is the alternate pathname separator (None or '/')
    - os.pathsep is the component separator used in $PATH etc
    - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
    - os.defpath is the default search path for executables
    - os.devnull is the file path of the null device ('/dev/null', etc)

Programs that import and use 'os' stand a better change of being portable between different platforms. Of course, they
must then only use functions that are defined by all platforms (e.g. unlink and opendir), and leave all pathname
manipulation to os.path (e.g., split and join).
"""

#
import abc
import sys
import stat as st

_names = sys.builtin_module_names

# Note: more names are added to __all__ later.
__all__ = ["altsep", "curdir", "pardir", "sep", "pathsep", "linesep", "defpath", "name", "devnull", "SEEK_SET",
           "SEEK_CUR", "SEEK_END", "fsencode", "fsdecode", "get_exec_path", "fdopen", "popen", "extsep"]


def _exists(name):
    return name in globals()


def _get_exports_list(module):
    try:
        return list(module.__all__)
    except AttributeError:
        return [n for n in dir(module) if n[0] != '_']


# Any new dependencies of the os module and / or changes in path separator requires updating importlib as well.
if 'posix' in _names:
    name = 'posix'
    linesep = '\n'
    from posix import *
    try:
        from posix import _exit
        __all__.append('__exit')
    except ImportError:
        pass
    import posixpath as path

    try:
        from posix import _have_functions
    except ImportError:
        pass

    import posix
    __all__.extend(_get_exports_list(posix))
    del posix

elif 'nt' in _names:
    name = 'nt'
    linesep = '\r\n'
    from nt import *
    try:
        from nt import _exit
        __all__.append('_exit')
    except ImportError:
        pass
    import ntpath as path

    import nt
    __all__.extend(_get_exports_list(nt))
    del nt

    try:
        from nt import _have_functions
    except ImportError:
        pass

else:
    raise ImportError('no os specific module found')

sys.modules['os.path'] = path
from os.path import (curdir, pardir, sep, pathsep, defpath, extsep, altsep, devnull)

del _names


if _exists("_have_functions"):
    _globals = globals()
    def _add(str, fn):
        if (fn in _globals) and (str in _have_functions):
            _set.add(_globals[fn])

    _set = set()
    _add("HAVE_FACCESSAT", "access")
    _add("HAVE_FCHMODAT", "chmod")
    _add("HAVE_FCHOWNAT", "chown")
    _add("HAVE_FSTATAT", "stat")
    _add("HAVE_FUTIMESAT", "utime")
    _add("HAVE_LINKAT", "link")
    _add("HAVE_MKDIRAT", "mkdir")
    _add("HAVE_MKFIFOAT", "mkfifo")
    _add("HAVE_MKNODAT", "mknod")
    _add("HAVE_OPENAT", "open")
    _add("HAVE_READLINKAT", "readlink")
    _add("HAVE_RENAMEAT", "rename")
    _add("HAVE_SYMLINKAT", "symlink")
    _add("HAVE_UNLINKAT", "unlink")
    _add("HAVE_UNLINKAT", "rmdir")
    _add("HAVE_UTIMENSAT", "utime")
    supports_dir_fd = _set

    _set = set()
    _add("HAVE_FACCESSAT", "access")
    supports_effective_ids = _set

    _set = set()
    _add("HAVE_FCHDIR", "chdir")
    _add("HAVE_FCHMOD", "chmod")
    _add("HAVE_FCHOWN", "chown")
    _add("HAVE_FDOPENDIR", "listdir")
    _add("HAVE_FDOPENDIR", "scandir")
    _add("HAVE_FEXECVE", "execve")
    _set.add(stat)  # fstat always works
    _add("HAVE_FTRUNCATE", "truncate")
    _add("HAVE_FUTIMENS", "utime")
    _add("HAVE_FUTIMES", "utime")
    _add("HAVE_FPATHCONF", "pathconf")
    if _exists("statvfs") and _exists("fstatvfs"): # mac os x10.3
        _add("HAVE_FSTATVFS", "statvfs")
    supports_fd = _set

    _set = set()
    _add("HAVE_FACCESSAT", "access")
    # Some platforms don't support lchmod().  Often the function exists
    # anyway, as a stub that always returns ENOSUP or perhaps EOPNOTSUPP.
    # (No, I don't know why that's a good design.)  ./configure will detect
    # this and reject it--so HAVE_LCHMOD still won't be defined on such
    # platforms.  This is Very Helpful.
    #
    # However, sometimes platforms without a working lchmod() *do* have
    # fchmodat().  (Examples: Linux kernel 3.2 with glibc 2.15,
    # OpenIndiana 3.x.)  And fchmodat() has a flag that theoretically makes
    # it behave like lchmod().  So in theory it would be a suitable
    # replacement for lchmod().  But when lchmod() doesn't work, fchmodat()'s
    # flag doesn't work *either*.  Sadly ./configure isn't sophisticated
    # enough to detect this condition--it only determines whether or not
    # fchmodat() minimally works.
    #
    # Therefore we simply ignore fchmodat() when deciding whether or not
    # os.chmod supports follow_symlinks.  Just checking lchmod() is
    # sufficient.  After all--if you have a working fchmodat(), your
    # lchmod() almost certainly works too.
    #
    # _add("HAVE_FCHMODAT",   "chmod")
    _add("HAVE_FCHOWNAT", "chown")
    _add("HAVE_FSTATAT", "stat")
    _add("HAVE_LCHFLAGS", "chflags")
    _add("HAVE_LCHMOD", "chmod")
    if _exists("lchown"):  # mac os x10.3
        _add("HAVE_LCHOWN", "chown")
    _add("HAVE_LINKAT", "link")
    _add("HAVE_LUTIMES", "utime")
    _add("HAVE_LSTAT", "stat")
    _add("HAVE_FSTATAT", "stat")
    _add("HAVE_UTIMENSAT", "utime")
    _add("MS_WINDOWS", "stat")
    supports_follow_symlinks = _set

    del _set
    del _have_functions
    del _globals
    del _add

    # Python uses fixed values for the SEEK_ constants; they are mapped to native constants if necessary in
    # posixmodule.c. Other possible SEEK values are directly imported from posixmodule.c

    SEEK_SET = 0
    SEEK_CUR = 1
    SEEK_END = 2

    # Super directory utilities.
    # (Inspired by Eric Raymond; the doc strings are mostly his)

