from constants import Shape, Color
from game_object import GameObject
from dataclasses import dataclass

@dataclass
class BoundingBox:
    x_min: float
    y_min: float
    x_max: float
    y_max: float

class Car(GameObject):
    car_velocity: int = 5
    MOVE_INCREMENT: int = 10

    def __init__(self, x_pos: float, y_pos: float) -> None:
        super().__init__(Shape.SQUARE, Color.WHITE)
        self.height = 1
        self.width = 2
        self.shapesize(self.height, self.width)
        self._init_x_pos = x_pos
        self._init_y_pos = y_pos
        self.start_car()

    def start_car(self) -> None:
        self._start_object()

    def move(self) -> None:
        x, y = self.pos()
        self.goto(x-self.car_velocity, y)
    
    def get_bounding_box(self) -> BoundingBox:
        x, y = self.pos()
        x_offset = self.width // 2 * self.minimum_size
        y_offset = self.height // 2 * self.minimum_size
        return BoundingBox(x-x_offset, y-y_offset, x+x_offset, y+y_offset)
    
    def change_color(self, color: Color) -> None:
        self.color(color.value)

    @classmethod
    def increment_velocity(cls) -> None:
        cls.car_velocity += cls.MOVE_INCREMENT