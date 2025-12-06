from game_object import GameObject, Color, Shape

class Player(GameObject):
    def __init__(self, screen_height: float) -> None:
        super().__init__(Shape.TURTLE, Color.BLACK)
        self.player_speed = 10
        half_height = screen_height // 2
        self.start_line_y = -half_height + self.minimum_size
        self.finish_line_y = half_height
        self.setheading(90)
        self._move_to_start()

    def _move_to_start(self) -> None:
        self.goto(0, self.start_line_y)

    def move_up(self):
        self.forward(self.player_speed)

    def finished(self) -> bool:
        player_bbox = self.get_bounding_box()
        is_finished = player_bbox.y_min >= self.finish_line_y
        if is_finished:
            self._move_to_start()
        return is_finished