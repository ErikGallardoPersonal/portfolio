from turtle import Turtle

class Grid(Turtle):
    def __init__(self, top_right_corner: tuple) -> None:
        super().__init__(visible = False)
        self.speed(0)
        self._top_right_corner = top_right_corner

    def frame_scene(self):
        self._draw_contour()
        self._show_score()

    def _show_score(self) -> None:
        self.penup()
        self.color("black")
        self.pensize(17)
        self.goto(-self._top_right_corner[0] // 2, self._top_right_corner[1])
        self.pendown()
        self.forward(self._top_right_corner[0])
    
    def _draw_contour(self) -> None:
        self.penup()
        self.color("white")
        self.pensize(17)
        self.goto(self._top_right_corner)
        self.pendown()
        for _ in range(2):
            for idx in range(len(self._top_right_corner)-1, -1, -1):
                self.setheading(self.heading() - 90)
                self.forward(self._top_right_corner[idx]*2)