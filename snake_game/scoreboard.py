from constants import WINDOW_HEIGHT_PIX, SNAKE_SEGMENT_SIZE_PIX, ALIGNMENT, FONT
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.current_score = -1
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, WINDOW_HEIGHT_PIX//2 - SNAKE_SEGMENT_SIZE_PIX)
        self.update_score()
    
    def update_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score = {self.current_score}", align=ALIGNMENT, font=FONT)