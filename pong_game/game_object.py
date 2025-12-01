from turtle import Turtle
from enum import Enum

class Shapes(Enum):
    SQUARE = "square"
    circle = "circle"

class GameObject(Turtle):
    def __init__(self, minimum_size_pix: int, shape: Shapes, x_pos_pix: int, y_pos_pix: int = 0) -> None:
        super().__init__(shape=shape.value)
        self.minimum_size = minimum_size_pix
        self.penup()
        self.color("white")
        self.shapesize(1, 1)
        self.goto(x_pos_pix, y_pos_pix)
