from random import randint
from game_object import GameObject, Shapes
from paddle import Paddle

class Ball(GameObject):
    def __init__(self, minimum_size_pix: int, wall_limit: int):
        super().__init__(minimum_size_pix=minimum_size_pix, shape=Shapes.circle, x_pos_pix=0, y_pos_pix=0)
        velocity = 10
        self.x_velocity = velocity
        self.y_velocity = randint(1, velocity)
        self.wall_limit = wall_limit

    def move(self):
        x, y = self.pos()
        x += self.x_velocity
        y += self.y_velocity 
        self.goto(x, y)

    def collision_with_paddle(self, paddle: Paddle):
        if self.distance(paddle) > self.minimum_size * 5 / 2:
            return
        original_paddle_x = paddle.xcor()
        original_sign = 1 if original_paddle_x >= 0 else -1
        paddle_x_limit = abs(original_paddle_x)
        paddle_width = paddle.minimum_size // 2
        ball_x = abs(self.xcor())
        x_limit = paddle_x_limit - 2 * paddle_width
        if ball_x >= x_limit:
            self._bounce_x(x_limit * original_sign)


    def collision_with_wall(self):
        y_cor = self.ycor()
        ball_radius = self.minimum_size // 2
        y_limit = self.wall_limit - ball_radius
        if y_cor >= y_limit:
            self._bounce_y(y_limit)
        y_limit = -self.wall_limit + ball_radius
        if y_cor <= y_limit:
            self._bounce_y(y_limit)

    def has_scored(self):
        ...

    def _bounce_x(self, x_pos: float):
        self.setx(x_pos)
        self.x_velocity *= -1

    def _bounce_y(self, y_pos: float):
        self.sety(y_pos)
        self.y_velocity *= -1