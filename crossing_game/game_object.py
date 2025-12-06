from turtle import Turtle
from constants import Shape, Color, MINIMUM_SIZE_PIX

class GameObject(Turtle):
    def __init__(self, shape: Shape, color: Color) -> None:
        super().__init__(shape=shape.value)
        self.minimum_size = MINIMUM_SIZE_PIX
        self.penup()
        self.color(color.value)
        self.height = 1
        self.width = 1
        self._init_x_pos: float
        self._init_y_pos: float

    def _start_object(self) -> None:
        self.goto(self._init_x_pos, self._init_y_pos)
