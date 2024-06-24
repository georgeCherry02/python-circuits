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


class NoOrthogonalConnection(Exception):
    """
    This exception will be raised when an orthogonal connection is requested
    to a point which does not sit orthogonal to the line
    """


def get_nearest_point(p1: Vector2, p2: Vector2, p3: Vector2) -> Vector2:
    horizontal = p1.y == p2.y
    between_p1_p2_x = ((p1.x <= p3.x) and (p3.x <= p2.x)) or (
        (p2.x <= p3.x) and (p3.x <= p1.x)
    )
    between_p1_p2_y = ((p1.y <= p3.y) and (p3.y <= p2.y)) or (
        (p2.y <= p3.y) and (p3.y <= p1.y)
    )
    if horizontal and between_p1_p2_x:
        return Vector2(p3.x, p1.y)
    elif between_p1_p2_y:
        return Vector2(p1.x, p3.y)
    else:
        raise NoOrthogonalConnection(
            f"Failed to find an orthogonal connection to p3={p3} from the line connecting p1={p1} to p2={p2}"
        )
