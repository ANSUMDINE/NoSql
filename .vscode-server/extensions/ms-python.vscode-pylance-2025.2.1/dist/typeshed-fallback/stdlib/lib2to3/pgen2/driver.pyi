from _typeshed import StrPath
from collections.abc import Iterable
from logging import Logger
from typing import IO

from ..pytree import _NL
from . import _Convert
from .grammar import Grammar

__all__ = ["Driver", "load_grammar"]

class Driver:
    grammar: Grammar
    logger: Logger
    convert: _Convert
    def __init__(self, grammar: Grammar, convert: _Convert | None = None, logger: Logger | None = None) -> None: ...
    def parse_tokens(
        self, tokens: Iterable[tuple[int, str, tuple[int, int], tuple[int, int], str]], debug: bool = False
    ) -> _NL: ...
    def parse_stream_raw(self, stream: IO[str], debug: bool = False) -> _NL: ...
    def parse_stream(self, stream: IO[str], debug: bool = False) -> _NL: ...
    def parse_file(self, filename: StrPath, encoding: str | None = None, debug: bool = False) -> _NL: ...
    def parse_string(self, text: str, debug: bool = False) -> _NL: ...

def load_grammar(
    gt: str = "Grammar.txt", gp: str | None = None, save: bool = True, force: bool = False, logger: Logger | None = None
) -> Grammar: ...
