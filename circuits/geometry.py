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


def get_nearest_point(p1: Vector2, p2: Vector2, p3: Vector2) -> Vector2:
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    dx, dy = x2 - x1, y2 - y1
    det = dx * dx + dy * dy
    a = (dy * (y3 - y1) + dx * (x3 - x1)) / det
    return Vector2(x1 + a * dx, y1 + a * dy)
