from circuits.colours import DEAD_COLOUR, LIVE_COLOUR
from geometry import NoOrthogonalConnection, get_nearest_point

from pygame import draw, Surface, Vector2

from math import inf
from typing import Callable, List, Optional, Tuple


def find_nearest_point_across_segments(
    segments: List[Tuple[Vector2, Vector2]], target: Vector2
) -> Vector2:
    current_nearest = None
    current_nearest_distance = inf
    for start, end in segments:
        try:
            nearest_point_on_segment = get_nearest_point(start, end, target)
        except NoOrthogonalConnection:
            continue
        distance = nearest_point_on_segment.distance_to(target)
        if distance < current_nearest_distance:
            current_nearest_distance = distance
            current_nearest = nearest_point_on_segment

    return current_nearest  # type: ignore


class Wire:
    """
    This class is meant to represent a wire made up of multiple individual
    stretches
    """

    class ConnectionPoint:
        """
        This class represents a connection point to a wire, or on a Component
        @member location: Vector2
        @member _state_functor: Callable[[]bool]
        """

        def __init__(
            self, location: Vector2, state_functor: Callable[[], bool] = lambda: True
        ):
            self.connected_wires = []
            self.location = location
            self._state_functor = state_functor

        def set_state_functor(self, functor: Callable[[], bool]):
            self._state_functor = functor

        def connect_wire(self, wire: "Wire"):
            self.connected_wires.append(wire)

        def high(self, /, from_wire: Optional["Wire"] = None) -> bool:
            return self._state_functor() or any(
                (wire.high() for wire in self.connected_wires if wire != from_wire)
            )

    def __init__(self, id: str, first_point: ConnectionPoint):
        self.id = id
        self.connections = [first_point]
        self.segments = []

    def __eq__(self, other) -> bool:
        if isinstance(other, Wire):
            return self.id == other.id
        elif isinstance(other, str):
            return self.id == other
        else:
            return False

    def __repr__(self) -> str:
        return (
            f"[id={self.id}, segments={self.segments}, connections={self.connections}]"
        )

    def add_connection(self, point: ConnectionPoint):
        point.connect_wire(self)
        self.connections.append(point)
        self.add_stretch(point.location)

    def add_stretch(self, target: Vector2, /, debug: bool = False):
        if debug:
            print(f"Extending wire to target={target}")
            print(f"Current segments: {self.segments}")
        nearest_point = (
            self.connections[0].location
            if not self.segments
            else find_nearest_point_across_segments(self.segments, target)
        )
        self.segments.append((nearest_point, target))

    def high(self) -> bool:
        return any((con.high(from_wire=self) for con in self.connections))

    def draw(self, screen: Surface):
        colour = LIVE_COLOUR if self.high() else DEAD_COLOUR
        for start, end in self.segments:
            draw.line(screen, colour, start, end)
