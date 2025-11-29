from turtle import Turtle
from random import choice


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)

    def reposition(self, grid_positions: list[int], snake_segments: list[Turtle]) -> None:
        snake_positions = {(seg.xcor(), seg.ycor()) for seg in snake_segments}
        free_positions = [
            pos for pos in grid_positions if pos not in snake_positions]
        if not free_positions:
            return
        x, y = choice(free_positions)
        self.goto(x, y)
