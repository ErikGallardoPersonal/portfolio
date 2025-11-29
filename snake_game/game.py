from time import time, sleep
from turtle import Screen
from constants import WINDOW_WIDTH_PIX, WINDOW_HEIGHT_PIX, GRID_SIZE_PIX
from snake import Snake
from food import Food
from grid import Grid
from scoreboard import Scoreboard


class Game:
    def __init__(self) -> None:
        self._grid_size = GRID_SIZE_PIX
        self.grid_positions: list[tuple[int, int]] = []
        self._setup_screen()
        self._create_elements()
        self._draw_frame()
        self._bind_keys()
        self._is_running = True
        self._is_paused = False
        self.update_interval: float = 1 / 5

    def _render(self):
        self._screen.update()

    def _update(self):
        self._snake.move()
        self.check_food_collision()
        self.check_wall_collision()
        self.check_tail_collision()

    def run(self) -> None:
        self._scoreboard.position_score(
            self._screen.window_height() // 2,  self._grid_size)
        self._food.reposition(self.grid_positions, self._snake.segments)
        last_update = time()
        while self._is_running:
            now = time()
            delta = now - last_update
            if delta >= self.update_interval:
                if not self._is_paused:
                    self._update()
                    last_update = now
            self._render()
            sleep(0.001)
        self._screen.exitonclick()

    def _setup_screen(self) -> None:
        self._screen = Screen()
        self._screen.clearscreen()
        self._screen.setup(
            width=WINDOW_WIDTH_PIX + self._grid_size,
            height=WINDOW_HEIGHT_PIX + self._grid_size
        )
        self._screen.cv._rootwindow.resizable(False, False)
        self._screen.bgcolor("black")
        self._screen.title("Ouroboros")
        self._screen.tracer(0)

    def _draw_frame(self) -> None:
        grid = Grid((WINDOW_WIDTH_PIX//2, WINDOW_HEIGHT_PIX//2))
        grid.frame_scene()
        del grid
        # Generate all grid coordinates
        for x in range(-self._screen.window_width()//2 + self._grid_size // 2,
                       self._screen.window_width()//2 - self._grid_size,
                       self._grid_size):
            for y in range(-self._screen.window_height()//2 + self._grid_size // 2,
                           self._screen.window_height()//2 - self._grid_size,
                           self._grid_size):
                self.grid_positions.append((x, y))

    def _create_elements(self) -> None:
        self._snake = Snake()
        self._food = Food()
        self._scoreboard = Scoreboard()

    def toggle_pause(self) -> None:
        self._is_paused = not self._is_paused

    def _bind_keys(self) -> None:
        self._screen.listen()
        self._screen.onkey(self._snake.turn_up, "Up")
        self._screen.onkey(self._snake.turn_down, "Down")
        self._screen.onkey(self._snake.turn_left, "Left")
        self._screen.onkey(self._snake.turn_right, "Right")
        self._screen.onkey(self.toggle_pause, "p")

    # --- collision methods ---
    def check_food_collision(self) -> None:
        if not self._snake.ate(self._food):
            return
        self._food.reposition(self.grid_positions, self._snake.segments)
        self._scoreboard.update_score()
        self._snake.extend()
        self.update_interval = max(0.055, self.update_interval * 0.95)

    def check_wall_collision(self):
        if not self._snake.collided_with_wall(self._screen.window_width()//2, self._screen.window_height()//2):
            return
        self._scoreboard.game_over()
        self._is_running = False

    def check_tail_collision(self):
        if not self._snake.collided_with_tail():
            return
        self._scoreboard.game_over()
        self._is_running = False
