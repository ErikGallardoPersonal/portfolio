from enum import Enum
from turtle import Turtle

class Shapes(Enum):
    SQUARE = "square"
    circle = "circle"

class GameObject(Turtle):
    def __init__(self, minimum_size_pix: int, shape: Shapes) -> None:
        super().__init__(shape=shape.value)
        self.minimum_size = minimum_size_pix
        self.penup()
        self.color("white")
        self.shapesize(1, 1)
        self._init_x_pos: int

    def _start_object(self) -> None:
        self.goto(self._init_x_pos, 0)
