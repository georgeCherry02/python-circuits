from .connection_point import ConnectionPoint
from .colours import DEAD_COLOUR, LIVE_COLOUR

from pygame import draw, Surface


class Transistor:
    """
    This class represents a transistor component
    """

    def __init__(self, input: ConnectionPoint, signal: ConnectionPoint):
        self.location = input.location + (5, 0)
        if input.location + (5, 5) != signal.location:
            print("Oh no...")
            raise Exception("Passed invalid connection points, two far apart!")
        self.input = input
        self.signal = signal
        self.output = ConnectionPoint(input.location + (5, 10), self._output)

    def _output(self):
        return self.input.high() and self.signal.high()

    def draw(self, screen: Surface):
        input_high = self.input.high()
        signal_high = self.signal.high()
        output_high = self.output.high()
        draw.circle(screen, DEAD_COLOUR, self.location, 5, width=1)
