from .connection_point import ConnectionPoint
from .colours import DEAD_COLOUR, LIVE_COLOUR

from pygame import draw, Surface

TRANSISTOR_SIZE = 7


class Transistor:
    """
    This class represents a transistor component
    """

    def __init__(self, input: ConnectionPoint, signal: ConnectionPoint):
        self.location = input.location + (TRANSISTOR_SIZE, 0)
        if input.location + (TRANSISTOR_SIZE, TRANSISTOR_SIZE) != signal.location:
            print("Oh no...")
            raise Exception("Passed invalid connection points, two far apart!")
        self.input = input
        self.signal = signal
        self.output = ConnectionPoint(input.location + (2 * TRANSISTOR_SIZE - 1, 0), self._output)

    def _output(self):
        return self.input.high() and self.signal.high()

    def draw(self, screen: Surface):
        input_high = self.input.high()
        signal_high = self.signal.high()
        output_high = self.output.high()
        draw.circle(screen, DEAD_COLOUR, self.location, TRANSISTOR_SIZE, width=1)
        # Yes this is all dependent on transistor size
        # I'm not changing that yet...
        ik_start = self.input.location + (2, 0)
        ik_end = self.input.location + (5, 3)
        ok_start = self.input.location + (8, 3)
        ok_end = self.input.location + (11, 0)
        draw.line(screen, DEAD_COLOUR, self.input.location, ik_start)
        draw.line(screen, DEAD_COLOUR, ik_start, ik_end)
        draw.line(screen, DEAD_COLOUR, ik_end, ok_start)
        draw.line(screen, DEAD_COLOUR, ok_start, ok_end)
        draw.line(screen, DEAD_COLOUR, ok_end, self.output.location)
        sig_mid = self.location + (0, 3)
        draw.line(screen, DEAD_COLOUR, sig_mid, self.signal.location)

