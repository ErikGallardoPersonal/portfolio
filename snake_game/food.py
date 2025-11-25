from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)

    def reposition(self, x_limit_pix: int, y_limit_pix: int, grid_size: int) -> None:
        self.goto(self._get_random_pos(x_limit_pix, y_limit_pix, grid_size))

    @staticmethod
    def _get_random_pos(x_limit_pix: int, y_limit_pix: int, grid_size: int) -> tuple[int]:
        x_limit_norm = (x_limit_pix // 2) // grid_size
        y_limit_norm = (y_limit_pix // 2) // grid_size
        x_position = randint(-x_limit_norm + 1, x_limit_norm - 1) * grid_size
        y_position = randint(-y_limit_norm + 1, y_limit_norm - 2) * grid_size
        return (x_position, y_position)