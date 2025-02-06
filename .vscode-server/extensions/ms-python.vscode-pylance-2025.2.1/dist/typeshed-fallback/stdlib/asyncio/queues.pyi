import sys
from asyncio.events import AbstractEventLoop
from typing import Any, Generic, TypeVar

if sys.version_info >= (3, 9):
    from types import GenericAlias

if sys.version_info >= (3, 10):
    from .mixins import _LoopBoundMixin
else:
    _LoopBoundMixin = object

class QueueEmpty(Exception): ...
class QueueFull(Exception): ...

# Keep asyncio.__all__ updated with any changes to __all__ here
if sys.version_info >= (3, 13):
    __all__ = ("Queue", "PriorityQueue", "LifoQueue", "QueueFull", "QueueEmpty", "QueueShutDown")

else:
    __all__ = ("Queue", "PriorityQueue", "LifoQueue", "QueueFull", "QueueEmpty")

_T = TypeVar("_T")

if sys.version_info >= (3, 13):
    class QueueShutDown(Exception): ...

# If Generic[_T] is last and _LoopBoundMixin is object, pyright is unhappy.
# We can remove the noqa pragma when dropping 3.9 support.
class Queue(Generic[_T], _LoopBoundMixin):  # noqa: Y059
    if sys.version_info >= (3, 10):
        def __init__(self, maxsize: int = 0) -> None: ...
    else:
        def __init__(self, maxsize: int = 0, *, loop: AbstractEventLoop | None = None) -> None: ...

    def _init(self, maxsize: int) -> None: ...
    def _get(self) -> _T: ...
    def _put(self, item: _T) -> None: ...
    def _format(self) -> str: ...
    def qsize(self) -> int: ...
    @property
    def maxsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    async def put(self, item: _T) -> None: ...
    def put_nowait(self, item: _T) -> None: ...
    async def get(self) -> _T: ...
    def get_nowait(self) -> _T: ...
    async def join(self) -> None: ...
    def task_done(self) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, type: Any, /) -> GenericAlias: ...
    if sys.version_info >= (3, 13):
        def shutdown(self, immediate: bool = False) -> None: ...

class PriorityQueue(Queue[_T]): ...
class LifoQueue(Queue[_T]): ...
