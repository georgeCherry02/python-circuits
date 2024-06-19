from .connection_point import ConnectionPoint

from pygame import draw, Surface

from copy import deepcopy

DEAD_COLOUR = (0, 0, 0)
LIVE_COLOUR = (250, 221, 56)


def get_nearest_point(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    dx, dy = x2 - x1, y2 - y1
    det = dx * dx + dy * dy
    a = (dy * (y3 - y1) + dx * (x3 - x1)) / det
    return x1 + a * dx, y1 + a * dy


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
