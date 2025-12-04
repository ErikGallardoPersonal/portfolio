from dataclasses import dataclass
from turtle import Turtle

@dataclass
class PaddleScore:
    score: int
    x_cor: int

class Scoreboard(Turtle):
    def __init__(self, y_cor: int, x_ofset: int) -> None:
        super().__init__(visible=False)
        self.current_score = -1
        self.penup()
        self.color("white")
        self.speed(0)
        self.y_pos_pix = y_cor
        self.left_score = PaddleScore(0, -x_ofset)
        self.right_score = PaddleScore(0, x_ofset)
        self._scores: list[PaddleScore] = [self.left_score, self.right_score]
        self.update_scores()
    
    def left_scored(self) -> None:
        self.left_score.score += 1

    def right_scored(self) -> None:
        self.right_score.score += 1

    def update_scores(self) -> None:
        self.clear()
        for score in self._scores:
            self.goto(score.x_cor, self.y_pos_pix)
            self.write(score.score, align="center", font=('Courier', 30, 'normal'))

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(f"GAME OVER!!!", align="center", font=('Courier', 30, 'normal'))