from .connection_point import ConnectionPoint
from .colours import DEAD_COLOUR, LIVE_COLOUR
from .geometry import get_nearest_point

from pygame import draw, Surface

from copy import deepcopy


class Wire:
    """
    This class represents a single wire which can be connected to multiple
    other components
    """

    def _entangle(self, cp: ConnectionPoint):
        self._connections.append(deepcopy(cp.high))
        cp.set_state_functor(self.high)

    def __init__(self, start: ConnectionPoint, end: ConnectionPoint):
        self._connections = []
        self._entangle(start)
        self._entangle(end)
        self.start = start
        self.end = end

    def high(self):
        return any((h() for h in self._connections))

    def draw(self, screen: Surface):
        colour = LIVE_COLOUR if self.high() else DEAD_COLOUR
        draw.line(screen, colour, self.start.location, self.end.location)

    def extend(self, end: ConnectionPoint) -> "Wire":
        nearest_point = get_nearest_point(
            self.start.location, self.end.location, end.location
        )
        self._entangle(end)
        return Wire(ConnectionPoint(nearest_point, lambda: self.high()), end)
