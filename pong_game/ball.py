from game_object import GameObject, Shapes

class Ball(GameObject):
    def __init__(self, minimum_size_pix: int):
        super().__init__(minimum_size_pix=minimum_size_pix, shape=Shapes.circle, x_pos_pix=0)

    def move(self):
        self.forward(self.minimum_size)

    def has_collided_with_paddle(self):
        ...

    def has_collided_with_wall(self):
        ...
    
    def has_scored(self):
        ...