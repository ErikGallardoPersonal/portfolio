from random import choice, randint
from constants import Color, BoundingBox
from car import Car

class CarManager:
    def __init__(self) -> None:
        self._cache_colors = self._get_colors_list()
        self._number_of_cars = 50
        self._cars: list[Car] = []
        self._lanes: int
        self._columns: int
        self._step_col: float
        self._lane_heigth: float
        self._finish_line: float

    def set_street(self, screen_width: float, screen_heigth: float, lane_heigth: float, step_col: float = 5.0):
        self._step_col = step_col
        self._lane_heigth = lane_heigth
        self._columns = int(screen_width / step_col)
        self._lanes = int(screen_heigth / lane_heigth)
        self._finish_line = -screen_width // 2

    def create_all_cars(self):
        for _ in range(self._number_of_cars):
            column, lane = self._get_random_car_coor()
            car = Car(column, lane)
            self._change_car_color(car)
            self._cars.append(car)

    def move_cars(self) -> None:
        for car in self._cars:
            car.move()        

    def check_crashes(self, player_bbox: BoundingBox) -> bool:
        def check_x_collision():
            return (player_bbox.x_max >= car_bbox.x_min and\
                    player_bbox.x_max <= car_bbox.x_max) or\
                    (player_bbox.x_min >= car_bbox.x_min and\
                    player_bbox.x_min <= car_bbox.x_max)
        def check_y_collision():
            return (player_bbox.y_max > car_bbox.y_min and\
                    player_bbox.y_max <= car_bbox.y_max) or\
                    (player_bbox.y_min >= car_bbox.y_min and\
                    player_bbox.y_min < car_bbox.y_max)
        for car in self._cars:
            car_bbox = car.get_bounding_box()
            if check_x_collision() and check_y_collision():
                return True
        return False
    
    def check_car_finished(self) -> None:
        for car in self._cars:
            car_bbox = car.get_bounding_box()
            is_finished = car_bbox.x_max <= self._finish_line
            if not is_finished:
                continue
            _, lane = self._get_random_car_coor()
            car.goto(self._finish_line * -1, lane)
    
    def _change_car_color(self, car: Car) -> None:
        car.color(self._get_random_color(self._cache_colors).value)

    def _get_random_car_coor(self) -> tuple[float, float]:
        screen_columns = self._columns // 2
        screen_lanes = self._lanes // 2
        safe_zone_start_offset = 2
        column = randint(-screen_columns, screen_columns)
        lane = randint(-screen_lanes+safe_zone_start_offset, screen_lanes)
        return column*self._step_col, lane*self._lane_heigth
    
    @staticmethod
    def increment_car_velocities() -> None:
        Car.increment_velocity()

    @staticmethod
    def _get_random_color(colors: list[Color]) -> Color:
        return choice(colors)
    
    @staticmethod
    def _get_colors_list() -> list[Color]:
        return [color for color in Color if color != Color.WHITE and color != Color.BLACK]



    