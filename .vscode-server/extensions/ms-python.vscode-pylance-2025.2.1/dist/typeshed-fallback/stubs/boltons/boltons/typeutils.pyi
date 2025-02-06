from typing import Any, Literal, Protocol
from typing_extensions import Self

class _Sentinel(Protocol):
    def __bool__(self) -> Literal[False]: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, _memo) -> Self: ...

def make_sentinel(name: str = "_MISSING", var_name: str | None = None) -> _Sentinel: ...
def issubclass(subclass: type, baseclass: type) -> bool: ...
def get_all_subclasses(cls: type) -> list[type]: ...

class classproperty:
    fn: Any
    def __init__(self, fn) -> None: ...
    def __get__(self, instance, cls): ...
