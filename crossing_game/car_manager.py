from random import choice, randint
from constants import Color, MINIMUM_SIZE_PIX
from car import Car, BoundingBox

class CarManager:
    def __init__(self) -> None:
        self._cars: list[Car] = []
        self._number_of_cars = 50
        self._cache_colors = self._get_colors_list()
        self._lanes: int = 30
        self._columns: int = 120
        self._create_all_cars()

    def move_cars(self) -> None:
        for car in self._cars:
            car.move()        

    def check_crashes(self, player_bbox: BoundingBox) -> bool:
        for car in self._cars:
            car_bbox = car.get_bounding_box()
            if  (player_bbox.x_max >= car_bbox.x_min and\
                player_bbox.x_min <= car_bbox.x_max) or\
                (player_bbox.y_max >= car_bbox.y_min and\
                player_bbox.y_min <= car_bbox.y_max):
                return True
        return False
    
    def check_car_ended(self) -> None:
        for car in self._cars:
            car_bbox = car.get_bounding_box()
    
    def _create_all_cars(self):
        for _ in range(self._number_of_cars):
            x_pos, y_pos = self._get_random_car_coor(self._columns, self._lanes)
            car = Car(x_pos * 5, y_pos * MINIMUM_SIZE_PIX)
            self._change_car_color(car)
            self._cars.append(car)
    
    def _change_car_color(self, car: Car) -> None:
        car.color(self._get_random_color(self._cache_colors).value)

    @staticmethod
    def increment_car_velocities() -> None:
        Car.increment_velocity()

    @staticmethod
    def _get_random_color(colors: list[Color]) -> Color:
        return choice(colors)
    
    @staticmethod
    def _get_random_car_coor(max_columns: int, max_lanes: int) -> tuple[float, float]:
        column = randint(0, max_columns)
        lane = randint(0, max_lanes)
        return column, lane

    @staticmethod
    def _get_colors_list() -> list[Color]:
        return [color for color in Color if color != Color.WHITE or color != Color.BLACK]



    