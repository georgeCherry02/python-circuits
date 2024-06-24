from circuits.connection_point import ConnectionPoint
from circuits.colours import DEAD_COLOUR, LIVE_COLOUR
from .geometry import get_nearest_point

from pygame import draw, Surface, Vector2

from math import inf
from typing import List, Tuple


def find_nearest_point_across_seq(
    segments: List[Tuple[Vector2, Vector2]], target: Vector2
) -> Vector2:
    current_nearest = None
    current_nearest_distance = inf
    for start, end in segments:
        nearest_point_on_segment = get_nearest_point(start, end, target)
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

    def __init__(self, first_point: ConnectionPoint, label=""):
        self.connections = [first_point]
        self.segments = []
        self.label = label

    def __repr__(self) -> str:
        return f"[label={self.label}, segments={self.segments}, connections={self.connections}]"

    def add_connection(self, point: ConnectionPoint):
        self.connections.append(point)
        self.add_stretch(point.location)

    def add_stretch(self, target: Vector2):
        nearest_point = (
            self.connections[0].location
            if not self.segments
            else find_nearest_point_across_seq(self.segments, target)
        )
        self.segments.append((nearest_point, target))

    def high(self) -> bool:
        return any((con.high() for con in self.connections))

    def draw(self, screen: Surface):
        colour = LIVE_COLOUR if self.high() else DEAD_COLOUR
        for start, end in self.segments:
            draw.line(screen, colour, start, end)
