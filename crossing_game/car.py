from tkinter import NO
from constants import Shape, Color
from game_object import GameObject

class Car(GameObject):
    START_CAR_SPEED: float = 5
    car_velocity: float = START_CAR_SPEED
    MOVE_INCREMENT: float = 1.05

    def __init__(self) -> None:
        super().__init__(Shape.SQUARE, Color.WHITE)
        self.height = 1
        self.width = 2
        self.shapesize(self.height, self.width)
        self._init_x_pos: float
        self._init_y_pos: float

    def start_car(self) -> None:
        self._start_object()

    def reposition(self, column: float, lane: float) -> None:
        self.goto(column, lane)

    def move(self) -> None:
        x, y = self.pos()
        self.goto(x-self.car_velocity, y)

    def has_finished(self, finish_line: float) -> bool:
        return self.get_bounding_box().x_max <= finish_line
    
    def change_color(self, color: Color) -> None:
        self.color(color.value)

    @classmethod
    def increment_velocity(cls) -> None:
        cls.car_velocity *= cls.MOVE_INCREMENT

    @classmethod
    def restart_speed(cls) -> None:
        cls.car_velocity = cls.START_CAR_SPEED