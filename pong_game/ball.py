from math import sqrt
from random import randint, choice
from game_object import GameObject, Shapes

class Ball(GameObject):
    def __init__(self, minimum_size_pix: int, wall_limit: int) -> None:
        super().__init__(minimum_size_pix=minimum_size_pix, shape=Shapes.circle)
        self.wall_limit = wall_limit
        self._init_x_pos = 0
        self.start_ball()

    def start_ball(self) -> None:
        self._start_object()
        signs = [1, -1]
        velocity: float = 10
        self.x_velocity = choice(signs) * velocity
        self.y_velocity = choice(signs) * randint(1, velocity)

    def increase_speed(self):
        self.x_velocity *= 1.05
        self.y_velocity *= 1.05

    def move(self):
        x, y = self.pos()
        x += self.x_velocity
        y += self.y_velocity 
        self.goto(x, y)

    def has_collision_with_paddle(self, paddle_cor: tuple[float, float]) -> bool:
        if self.distance(paddle_cor) > self.minimum_size * 5 / 2:
            return False
        paddle_x, _ = paddle_cor
        original_sign = 1 if paddle_x >= 0 else -1
        paddle_x_limit = abs(paddle_x)
        paddle_width = self.minimum_size // 2
        ball_x = abs(self.xcor())
        x_limit = paddle_x_limit - 2 * paddle_width
        if ball_x >= x_limit:
            self._bounce_x(x_limit * original_sign)
            return True
        return False

    def has_collision_with_wall(self) -> bool:
        y_cor = self.ycor()
        ball_radius = self.minimum_size // 2
        y_limit = self.wall_limit - ball_radius
        if y_cor >= y_limit:
            self._bounce_y(y_limit)
            return True
        y_limit = -self.wall_limit + ball_radius
        if y_cor <= y_limit:
            self._bounce_y(y_limit)
            return True
        return False

    def has_scored(self, paddle_x: float) -> bool:
        if self.x_velocity == 0:
            return False
        is_left_paddle: bool = True if paddle_x <= 0 else False
        is_ball_going_left: bool = True if self.x_velocity <= 0 else False
        if is_left_paddle ^ is_ball_going_left: # Ignore far away paddle 
            return False
        ball_x = self.xcor()
        return abs(ball_x) >= abs(paddle_x) + self.minimum_size // 2
    
    def _bounce_x(self, x_pos: float) -> None:
        self.setx(x_pos)
        self.x_velocity *= -1

    def _bounce_y(self, y_pos: float) -> None:
        self.sety(y_pos)
        self.y_velocity *= -1
