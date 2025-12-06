from constants import Shape, Color
from game_object import GameObject

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
    
    def change_color(self, color: Color) -> None:
        self.color(color.value)

    @classmethod
    def increment_velocity(cls) -> None:
        cls.car_velocity += cls.MOVE_INCREMENT