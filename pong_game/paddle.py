from enum import IntEnum
from turtle import Turtle

class MoveDirection(IntEnum):
    DOWN = -1
    UP = 1

class Paddle:
    def __init__(self, x_pos_pix: int) -> None:
        self._x_pos = x_pos_pix
        self._y_pos = 0
        self._number_of_elements = 5
        self._width = 20
        self._paddle_elements: list[Turtle] = []

    def move_up(self) -> None:
        ...

    def move_down(self) -> None:
        ...

    def get_bbox(self):
        ...

    def _create_paddle_elements(self):
        Y_OFFSET = self._number_of_elements // 2
        y_pos_pix = self._y_pos - (Y_OFFSET * self._width)
        for _ in self._number_of_elements:
            paddle_element = self._create_element(ele_pos_x_pix=self._x_pos,
                                                 ele_pos_y_pix=y_pos_pix)
            self._paddle_elements.append(paddle_element)

    def _move(self, move_dir: MoveDirection) -> None:
        if not self._is_valid_movement():
            return
        self._move_elements()

    def _is_valid_movement(self, current_tip: Turtle):
        ...

    def _move_elements(self, move_dir: MoveDirection):
        ...

    @staticmethod
    def _create_element(ele_pos_x_pix: int, ele_pos_y_pix: int) -> Turtle:
        paddle_element = Turtle(shape="square")
        paddle_element.penup()
        paddle_element.color("white")
        paddle_element.shapesize(
            stretch_len=1.0, stretch_wid=1.0)
        paddle_element.goto(ele_pos_x_pix, ele_pos_y_pix)
        return paddle_element