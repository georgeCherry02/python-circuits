from .connection_point import ConnectionPoint
from .wire import Wire

from typing import Optional


class Transistor:
    """
    This class represents a transistor component
    """

    def __init__(self, input: ConnectionPoint):
        self.input  = input
        self.signal = ConnectionPoint(input.location + (5, 5))
        self.output = ConnectionPoint(input.location + (5, 10), self.out)

    def out(self):
        return self.input.high() and self.signal.high()
