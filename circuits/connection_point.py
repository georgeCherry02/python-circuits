from typing import Callable

from pygame import Vector2


class ConnectionPoint:
    """
    This class represents a connection point on a component
    """

    def __init__(
        self, location: Vector2, state_functor: Callable[[], bool] = lambda: True
    ):
        self.location = location
        self._state_functor = state_functor

    def set_state_functor(self, functor: Callable[[], bool]):
        self._state_functor = functor

    def high(self) -> bool:
        return self._state_functor()
