from _typeshed import IdentityFunction, Unused
from collections.abc import Callable, Iterator, MutableMapping, Sequence
from contextlib import AbstractContextManager
from typing import Any, TypeVar, overload
from typing_extensions import deprecated

__all__ = ("Cache", "FIFOCache", "LFUCache", "LRUCache", "MRUCache", "RRCache", "TLRUCache", "TTLCache", "cached", "cachedmethod")
__version__: str

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")

class Cache(MutableMapping[_KT, _VT]):
    @overload
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float]) -> None: ...
    @overload
    def __init__(self, maxsize: float, getsizeof: None = None) -> None: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    def __missing__(self, key: _KT) -> _VT: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __len__(self) -> int: ...
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _VT | _T) -> _VT | _T: ...
    def setdefault(self, key: _KT, default: _VT | None = None) -> _VT: ...
    @property
    def maxsize(self) -> float: ...
    @property
    def currsize(self) -> float: ...
    @staticmethod
    def getsizeof(value: _VT) -> float: ...

class FIFOCache(Cache[_KT, _VT]): ...
class LFUCache(Cache[_KT, _VT]): ...
class LRUCache(Cache[_KT, _VT]): ...

@deprecated("@mru_cache is deprecated")
class MRUCache(Cache[_KT, _VT]): ...

class RRCache(Cache[_KT, _VT]):
    @overload
    def __init__(self, maxsize: float, choice: None = None, getsizeof: None = None) -> None: ...
    @overload
    def __init__(self, maxsize: float, *, getsizeof: Callable[[_VT], float]) -> None: ...
    @overload
    def __init__(self, maxsize: float, choice: None, getsizeof: Callable[[_VT], float]) -> None: ...
    @overload
    def __init__(self, maxsize: float, choice: Callable[[Sequence[_KT]], _KT], getsizeof: None = None) -> None: ...
    @overload
    def __init__(self, maxsize: float, choice: Callable[[Sequence[_KT]], _KT], getsizeof: Callable[[_VT], float]) -> None: ...
    @property
    def choice(self) -> Callable[[Sequence[_KT]], _KT]: ...

class _TimedCache(Cache[_KT, _VT]):
    @overload
    def __init__(self, maxsize: float, timer: Callable[[], float] = ..., getsizeof: None = None) -> None: ...
    @overload
    def __init__(self, maxsize: float, timer: Callable[[], float], getsizeof: Callable[[_VT], float]) -> None: ...
    @overload
    def __init__(self, maxsize: float, timer: Callable[[], float] = ..., *, getsizeof: Callable[[_VT], float]) -> None: ...
    @property
    def currsize(self) -> float: ...

    class _Timer:
        def __init__(self, timer: Callable[[], float]) -> None: ...
        def __call__(self) -> float: ...
        def __enter__(self) -> float: ...
        def __exit__(self, *exc: Unused) -> None: ...

    @property
    def timer(self) -> _Timer: ...

class TTLCache(_TimedCache[_KT, _VT]):
    @overload
    def __init__(self, maxsize: float, ttl: float, timer: Callable[[], float] = ..., getsizeof: None = None) -> None: ...
    @overload
    def __init__(self, maxsize: float, ttl: float, timer: Callable[[], float], getsizeof: Callable[[_VT], float]) -> None: ...
    @overload
    def __init__(
        self, maxsize: float, ttl: float, timer: Callable[[], float] = ..., *, getsizeof: Callable[[_VT], float]
    ) -> None: ...
    @property
    def ttl(self) -> float: ...
    def expire(self, time: float | None = None) -> list[tuple[_KT, _VT]]: ...

class TLRUCache(_TimedCache[_KT, _VT]):
    def __init__(
        self,
        maxsize: float,
        ttu: Callable[[_KT, _VT, float], float],
        timer: Callable[[], float] = ...,
        getsizeof: Callable[[_VT], float] | None = None,
    ) -> None: ...
    @property
    def ttu(self) -> Callable[[_KT, _VT, float], float]: ...
    def expire(self, time: float | None = None) -> list[tuple[_KT, _VT]]: ...

def cached(
    cache: MutableMapping[_KT, Any] | None,
    key: Callable[..., _KT] = ...,
    lock: AbstractContextManager[Any] | None = None,
    info: bool = False,
) -> IdentityFunction: ...
def cachedmethod(
    cache: Callable[[Any], MutableMapping[_KT, Any] | None],
    key: Callable[..., _KT] = ...,
    lock: Callable[[Any], AbstractContextManager[Any]] | None = None,
) -> IdentityFunction: ...
