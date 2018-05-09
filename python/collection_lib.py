__all__ = ['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList',
           'UserString', 'Counter', 'OrderedDict', 'ChainMap']


from _collections_abc import *
import _collections_abc

__all__ += _collections_abc.__all__


from operator import itemgetter as _itermegetter, eq as _eq
from keyword import iskeyword as _iskeyword
import sys as _sys
import heapq as _heapq
from _weakref import proxy as _proxy
from itertools import repeat as _repeat, chain as _chain, starmap as _starmap
from reprlib import recursive_repr as _recursive_repr

try:
    from _collections import deque
except ImportError:
    pass
else:
    MutableSequence.register(deque)

try:
    from _collections import defaultdict
except ImportError:
    pass


