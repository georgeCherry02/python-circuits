from circuits.new_wire import Wire
from circuits.colours import DEAD_COLOUR

from geometry import DIRECTION, get_dir_vec, get_clockwise_dir, get_anticlockwise_dir

from pygame import draw, Surface


class NotGate:
    """
    This class represents a NOT gate which inverts the incoming signal
    The reason this isn't implemented with transistors is NOT gates are
    reliant on the existence of resistance which this simple model of
    circuits doesn't include
    """

    def __init__(self, input: Wire.ConnectionPoint, direction: DIRECTION = "RIGHT"):
        self.direction: DIRECTION = direction
        self.input = input
        output_location = input.location + get_dir_vec(direction) * 10
        self.output = Wire.ConnectionPoint(
            output_location, lambda: not self.input.high()
        )

    def draw(self, screen: Surface):
        left_point = self.input.location + (
            get_dir_vec(get_clockwise_dir(self.direction)) * 4
        )
        right_point = self.input.location + (
            get_dir_vec(get_anticlockwise_dir(self.direction)) * 4
        )
        tip = self.output.location + (-4, 0)
        circle_loc = self.output.location + (-2, 0)
        draw.polygon(screen, DEAD_COLOUR, (left_point, right_point, tip), width=1)
        draw.circle(screen, DEAD_COLOUR, circle_loc, 2, width=1)
