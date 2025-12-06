from turtle import Turtle
from constants import Shape, Color, MINIMUM_SIZE_PIX, BoundingBox



class GameObject(Turtle):
    def __init__(self, shape: Shape, color: Color) -> None:
        super().__init__(shape=shape.value)
        self.minimum_size = MINIMUM_SIZE_PIX
        self.penup()
        self.color(color.value)
        self.height: int = 1
        self.width: int = 1
        self._init_x_pos: float
        self._init_y_pos: float

    def get_bounding_box(self) -> BoundingBox:
        x, y = self.pos()
        x_offset = (self.width / 2) * self.minimum_size
        y_offset = (self.height / 2) * self.minimum_size
        return BoundingBox(x-x_offset, y-y_offset, x+x_offset, y+y_offset)

    def _start_object(self) -> None:
        self.goto(self._init_x_pos, self._init_y_pos)
