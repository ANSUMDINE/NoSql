from _typeshed import Incomplete
from collections.abc import Iterator, MutableMapping
from typing import Any, NamedTuple

def base64url_encode(payload: str | bytes) -> str: ...
def base64url_decode(payload: str) -> bytes: ...
def json_encode(string: str | bytes) -> str: ...

# The function returns json.loads which returns Any
def json_decode(string: str | bytes) -> Any: ...

class JWException(Exception): ...

class InvalidJWAAlgorithm(JWException):
    def __init__(self, message: str | None = None) -> None: ...

class InvalidCEKeyLength(JWException):
    def __init__(self, expected: int, obtained: int) -> None: ...

class InvalidJWEOperation(JWException):
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class InvalidJWEKeyType(JWException):
    def __init__(self, expected: int, obtained: int) -> None: ...

class InvalidJWEKeyLength(JWException):
    def __init__(self, expected: int, obtained: int) -> None: ...

class InvalidJWSERegOperation(JWException):
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class JWKeyNotFound(JWException):
    def __init__(self, message: str | None = None) -> None: ...

class JWSEHeaderParameter(NamedTuple):
    description: str
    mustprotect: bool
    supported: bool
    check_fn: Incomplete | None

class JWSEHeaderRegistry(MutableMapping[str, JWSEHeaderParameter]):
    def __init__(self, init_registry: Incomplete | None = None) -> None: ...
    def check_header(self, h: str, value) -> bool: ...
    def __getitem__(self, key: str) -> JWSEHeaderParameter: ...
    def __iter__(self) -> Iterator[str]: ...
    def __delitem__(self, key: str) -> None: ...
    def __setitem__(self, h: str, jwse_header_param: JWSEHeaderParameter) -> None: ...
    def __len__(self) -> int: ...
