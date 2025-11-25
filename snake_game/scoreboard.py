from constants import ALIGNMENT, FONT
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.current_score = -1
        self.penup()
        self.color("white")
        self.speed(0)

    def position_score(self, y_pos_pix: int, grid_size: int) -> None:
        self.goto(0, y_pos_pix - grid_size)
        self.update_score()
    
    def update_score(self) -> None:
        self.current_score += 1
        self.clear()
        self.write(f"Score = {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(f"GAME OVER!!!", align=ALIGNMENT, font=FONT)