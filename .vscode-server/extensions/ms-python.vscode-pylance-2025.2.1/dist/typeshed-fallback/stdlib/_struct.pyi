from _typeshed import ReadableBuffer, WriteableBuffer
from collections.abc import Iterator
from typing import Any

def pack(fmt: str | bytes, /, *v: Any) -> bytes: ...
def pack_into(fmt: str | bytes, buffer: WriteableBuffer, offset: int, /, *v: Any) -> None: ...
def unpack(format: str | bytes, buffer: ReadableBuffer, /) -> tuple[Any, ...]: ...
def unpack_from(format: str | bytes, /, buffer: ReadableBuffer, offset: int = 0) -> tuple[Any, ...]: ...
def iter_unpack(format: str | bytes, buffer: ReadableBuffer, /) -> Iterator[tuple[Any, ...]]: ...
def calcsize(format: str | bytes, /) -> int: ...

class Struct:
    @property
    def format(self) -> str: ...
    @property
    def size(self) -> int: ...
    def __init__(self, format: str | bytes) -> None: ...
    def pack(self, *v: Any) -> bytes: ...
    def pack_into(self, buffer: WriteableBuffer, offset: int, *v: Any) -> None: ...
    def unpack(self, buffer: ReadableBuffer, /) -> tuple[Any, ...]: ...
    def unpack_from(self, buffer: ReadableBuffer, offset: int = 0) -> tuple[Any, ...]: ...
    def iter_unpack(self, buffer: ReadableBuffer, /) -> Iterator[tuple[Any, ...]]: ...
