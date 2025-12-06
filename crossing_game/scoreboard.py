from turtle import Turtle
from constants import FONT

class Scoreboard(Turtle):
    def __init__(self, screen_width: float, screen_height: float) -> None:
        super().__init__(visible=False)
        self.current_score = -1
        self.penup()
        self.color("black")
        self.speed(0)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player_score: int

    def restart_player_score(self) -> None:
        self.player_score = 0
    
    def player_finished(self) -> None:
        self.player_score += 1

    def update_score(self) -> None:
        self.clear()
        self.goto(-self.screen_width // 2, -self.screen_height // 2)
        self.write(f"Level: {self.player_score}", align="left", font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(f"GAME OVER!!!", align="center", font=FONT)

    def show_input_message(self):
        self.goto(self.screen_width // 2, -self.screen_height // 2)
        self.write(f"R - Restart, Q - Quit", align="right", font=FONT)
