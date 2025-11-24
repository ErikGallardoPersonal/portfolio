from turtle import Turtle
from constants import WINDOW_WIDTH_PIX, WINDOW_HEIGHT_PIX
class Grid(Turtle):
    def __init__(self) -> None:
        super().__init__(visible = False)
        self.speed(0)
        self._top_right_corner = (WINDOW_WIDTH_PIX//2, WINDOW_HEIGHT_PIX//2)
        self._draw_contour()
        self._show_score()

    def _show_score(self):
        self.penup()
        self.color("black")
        self.pensize(17)
        self.goto(-WINDOW_WIDTH_PIX // 4, WINDOW_HEIGHT_PIX//2)
        self.pendown()
        self.forward(WINDOW_WIDTH_PIX // 2)
    
    def _draw_contour(self):
        self.penup()
        self.color("white")
        self.pensize(17)
        self.goto(self._top_right_corner)
        self.pendown()
        for _ in range(2):
            for idx in range(len(self._top_right_corner)-1, -1, -1):
                self.setheading(self.heading() - 90)
                self.forward(self._top_right_corner[idx]*2)