from circuits.wire import Wire
from circuits.colours import DEAD_COLOUR, LIVE_COLOUR

from pygame import draw, Surface

TRANSISTOR_SIZE = 7


class Transistor:
    """
    This class represents a transistor component
    """

    def __init__(self, input: Wire.ConnectionPoint, signal: Wire.ConnectionPoint):
        self.location = input.location + (TRANSISTOR_SIZE, 0)
        if input.location + (TRANSISTOR_SIZE, TRANSISTOR_SIZE) != signal.location:
            raise Exception("Passed invalid connection points, two far apart!")
        self.input = input
        self.signal = signal
        self.output = Wire.ConnectionPoint(input.location + (2 * TRANSISTOR_SIZE - 1, 0), self._output)

    def _output(self):
        return self.input.high() and self.signal.high()

    def draw(self, screen: Surface):
        input_colour = LIVE_COLOUR if self.input.high() else DEAD_COLOUR
        signal_colour = LIVE_COLOUR if self.signal.high() else DEAD_COLOUR
        output_colour = LIVE_COLOUR if self.output.high() else DEAD_COLOUR
        draw.circle(screen, DEAD_COLOUR, self.location, TRANSISTOR_SIZE, width=1)
        # Yes this is all dependent on transistor size
        # I'm not changing that yet...
        ik_start = self.input.location + (2, 0)
        ik_end = self.input.location + (5, 3)
        ok_start = self.input.location + (8, 3)
        ok_end = self.input.location + (11, 0)
        draw.line(screen, input_colour, self.input.location, ik_start)
        draw.line(screen, input_colour, ik_start, ik_end)
        draw.line(screen, input_colour, ik_end, ok_start)
        draw.line(screen, output_colour, ok_start, ok_end)
        draw.line(screen, output_colour, ok_end, self.output.location)
        sig_mid = self.location + (0, 3)
        draw.line(screen, signal_colour, sig_mid, self.signal.location)

