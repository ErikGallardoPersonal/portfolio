from game_object import GameObject, Color, Shape

class Player(GameObject):
    def __init__(self, screen_height: float) -> None:
        super().__init__(Shape.TURTLE, Color.BLACK)
        self.player_speed = 10
        half_height = screen_height // 2
        self.start_line_y = -half_height + self.minimum_size
        self.finish_line_y = half_height
        self.goto(0, self.start_line_y)
        self.setheading(90)
        
    def move_up(self):
        self.forward(self.player_speed)