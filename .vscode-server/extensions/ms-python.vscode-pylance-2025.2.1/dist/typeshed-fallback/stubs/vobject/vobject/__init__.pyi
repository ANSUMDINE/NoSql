from .base import VERSION as VERSION, Component

__version__ = VERSION

def iCalendar() -> Component: ...
def vCard() -> Component: ...
