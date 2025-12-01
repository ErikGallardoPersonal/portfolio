from encodings.punycode import T
from enum import IntEnum
from game_object import GameObject, Shapes

class MoveDirection(IntEnum):
    DOWN = -1
    UP = 1

class Paddle(GameObject):
    def __init__(self, minimum_size_pix: int, x_pos_pix: int) -> None:
        super().__init__(minimum_size_pix=minimum_size_pix, shape=Shapes.SQUARE, x_pos_pix=x_pos_pix)
        self.shapesize(5, 1)
        self._direction: MoveDirection = MoveDirection.UP

    def move_up(self) -> None:
        self._direction = MoveDirection.UP
        self._move()

    def move_down(self) -> None:
        self._direction = MoveDirection.DOWN
        self._move()

    def get_bbox(self):
        ...

    def _move(self) -> None:
        if not self._is_valid_movement():
            return
        x, y = self.pos()
        self.goto(x, y + (self._direction * self.minimum_size))

    def _is_valid_movement(self):
        return True
