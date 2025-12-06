from game_object import GameObject, Color, Shape
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(GameObject):
    def __init__(self) -> None:
        super().__init__(Shape.TURTLE, Color.BLACK)
        self.player_speed = 10
        self.setheading(90)
        
    def move_up(self):
        self.forward(self.player_speed)