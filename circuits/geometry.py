from math import sqrt
from typing import Literal

from pygame import Vector2

DIRECTION = Literal["UP", "DOWN", "RIGHT", "LEFT"]


def get_dir_vec(dir: DIRECTION) -> Vector2:
    match dir:
        case "UP":
            return Vector2(0, -1)
        case "DOWN":
            return Vector2(0, 1)
        case "RIGHT":
            return Vector2(1, 0)
        case "LEFT":
            return Vector2(-1, 0)


def get_clockwise_dir(dir: DIRECTION) -> DIRECTION:
    match dir:
        case "UP":
            return "RIGHT"
        case "RIGHT":
            return "DOWN"
        case "DOWN":
            return "LEFT"
        case "LEFT":
            return "UP"


def get_anticlockwise_dir(dir: DIRECTION) -> DIRECTION:
    match dir:
        case "UP":
            return "LEFT"
        case "LEFT":
            return "DOWN"
        case "DOWN":
            return "RIGHT"
        case "RIGHT":
            return "UP"


def get_nearest_end_to_p3(p1: Vector2, p2: Vector2, p3: Vector2) -> Vector2:
    p1_closer = p3.distance_to(p1) < p3.distance_to(p2)
    return p1 if p1_closer else p2


def get_nearest_point_p3_off_line(p1: Vector2, p2: Vector2, p3: Vector2) -> Vector2:
    """
    This function makes the assumption that p3 is not present on the infinite
    line which p1 and p2 are both on
    """
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    dx, dy = x2 - x1, y2 - y1
    det = dx * dx + dy * dy
    a = (dy * (y3 - y1) + dx * (x3 - x1)) / det
    return Vector2(x1 + a * dx, y1 + a * dy)


def get_nearest_point(p1: Vector2, p2: Vector2, p3: Vector2) -> Vector2:
    segment = (p2 - p1).normalize()
    end_to_p3 = (p3 - p2).normalize()
    on_line = abs(segment.dot(end_to_p3)) == 1.0
    return (
        get_nearest_end_to_p3(p1, p2, p3)
        if on_line
        else get_nearest_point_p3_off_line(p1, p2, p3)
    )
