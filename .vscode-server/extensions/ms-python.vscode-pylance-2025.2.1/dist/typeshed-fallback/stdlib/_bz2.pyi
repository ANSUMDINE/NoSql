import sys
from _typeshed import ReadableBuffer
from typing import final
from typing_extensions import Self

@final
class BZ2Compressor:
    if sys.version_info >= (3, 12):
        def __new__(cls, compresslevel: int = 9, /) -> Self: ...
    else:
        def __init__(self, compresslevel: int = 9, /) -> None: ...

    def compress(self, data: ReadableBuffer, /) -> bytes: ...
    def flush(self) -> bytes: ...

@final
class BZ2Decompressor:
    def decompress(self, data: ReadableBuffer, max_length: int = -1) -> bytes: ...
    @property
    def eof(self) -> bool: ...
    @property
    def needs_input(self) -> bool: ...
    @property
    def unused_data(self) -> bytes: ...
