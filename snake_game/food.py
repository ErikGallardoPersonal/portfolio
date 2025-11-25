from turtle import Turtle
from random import randint
from constants import WINDOW_WIDTH_PIX, WINDOW_HEIGHT_PIX, SNAKE_SEGMENT_SIZE_PIX, FOOD_SIZE_PIX

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.penup()
        food_size = FOOD_SIZE_PIX/SNAKE_SEGMENT_SIZE_PIX
        self.shapesize(stretch_len=food_size, stretch_wid=food_size)
        self.color("red")
        self.speed(0)
        self.reposition()

    def reposition(self) -> None:
        x_limit_norm = (WINDOW_WIDTH_PIX // 2) // SNAKE_SEGMENT_SIZE_PIX
        y_limit_norm = (WINDOW_HEIGHT_PIX // 2) // SNAKE_SEGMENT_SIZE_PIX
        x_position = randint(-x_limit_norm + 1, x_limit_norm - 1) * SNAKE_SEGMENT_SIZE_PIX
        y_position = randint(-y_limit_norm + 1, y_limit_norm - 2) * SNAKE_SEGMENT_SIZE_PIX
        self.goto(x_position, y_position)