from game_object import GameObject, Shapes

class Ball(GameObject):
    def __init__(self, minimum_size_pix: int):
        super().__init__(minimum_size_pix=minimum_size_pix, shape=Shapes.circle, x_pos_pix=0, y_pos_pix=0)
        velocity = 10
        self.x_velocity = velocity
        self.y_velocity = velocity

    def move(self):
        x, y = self.pos()
        x += self.x_velocity
        y += self.y_velocity 
        self.goto(x, y)

    def bounce_paddle(self):
        ...

    def bounce_wall(self, wall_limit: int):
        y_cor = self.ycor()
        condition: int = wall_limit - self.minimum_size // 2
        if y_cor >= condition:
            self._y_pos = condition
            self.y_velocity *= -1
        condition = -wall_limit + self.minimum_size // 2
        if y_cor <= condition:
            self._y_pos = condition
            self.y_velocity *= -1

    def has_scored(self):
        ...