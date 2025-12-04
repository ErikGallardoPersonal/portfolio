from time import time, sleep
from window import Window
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

class Game:
    def __init__(self) -> None:
        self._minimum_element_size_pix = 20
        self._window = Window()
        self._screen_width, self._screen_height = self._window.screensize()
        self._ball = Ball(self._minimum_element_size_pix, wall_limit=self._screen_height//2)
        self._initialize_ball_movement()
        self._player1: Paddle
        self._player2: Paddle
        self._create_players()
        self._scoreboard = Scoreboard(self._screen_height // 2 - 50, 100)
        self._bind_keys()
        self._is_running: bool = True
        self.update_interval: float = 1 / 60
        self._is_paused = False

    def run(self) -> None:
        last_update = 0
        while self._is_running:
            now = time()
            delta = now - last_update
            if delta >= self.update_interval:
                if not self._is_paused:
                    self._update()
                    last_update = now
            self._render()
            sleep(0.001)
        self._window._screen.exitonclick()

    def _initialize_ball_movement(self) -> None:
        new_heading = self._ball.towards(self._screen_width//2, self._screen_height//2)
        self._ball.setheading(new_heading)

    def _create_players(self) -> None:
        half_width = self._screen_width // 2
        self._player1 = Paddle(self._minimum_element_size_pix, -half_width + self._minimum_element_size_pix)
        self._player2 = Paddle(self._minimum_element_size_pix, half_width - self._minimum_element_size_pix)

    def _bind_keys(self) -> None:
        self._window._screen.listen()
        self._window._screen.onkey(self._player1.move_up, "w")
        self._window._screen.onkey(self._player1.move_down, "s")
        self._window._screen.onkey(self._player2.move_up, "Up")
        self._window._screen.onkey(self._player2.move_down, "Down")
        self._window._screen.onkey(self.toggle_pause, "p")

    def _render(self) -> None:
        self._window._screen.update()

    def _update(self) -> None:
        players = [self._player1, self._player2]
        self._ball.has_collision_with_wall()
        for player in players:
            has_collision_paddle = self._ball.has_collision_with_paddle(player.pos())
            if has_collision_paddle:
                continue
            has_scored = self._ball.has_scored(player.xcor())
            if not has_scored:
                continue
            self._scoreboard.left_scored() if player is self._player2 else self._scoreboard.right_scored()
            self._scoreboard.update_scores()
            self._ball.start_ball()
            for p in players:
                p.start_paddle()
            break
        self._ball.move()

    def toggle_pause(self) -> None:
        self._is_paused = not self._is_paused