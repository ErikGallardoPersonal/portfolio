from time import time, sleep
from window import Window
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

class Game:
    def __init__(self) -> None:
        self._minimum_element_size_pix = 20
        self._window = Window()
        self._screen_width, self._screen_height = self._window.screensize()
        self._scoreboard = Scoreboard(self._screen_height // 2 - 50, 100)
        self._player = Player()
        self.car_manager = CarManager()
        self._bind_keys()
        self._is_running: bool = True
        self.update_interval: float = 1 / 60
        self._is_paused = False

    def run(self) -> None:
        last_update = 0
        while self._is_running:
            now = time()
            delta = now - last_update
            if delta >= self.update_interval and not self._is_paused:
                self._update()
                last_update = now
            self._render()
            sleep(0.001)
        self._window._screen.exitonclick()

    def _bind_keys(self) -> None:
        self._window._screen.listen()
        self._window._screen.onkey(self._player.move_up, "Up")
        self._window._screen.onkey(self.toggle_pause, "p")

    def _render(self) -> None:
        self._window._screen.update()

    def _update(self) -> None:
        ...

    def toggle_pause(self) -> None:
        self._is_paused = not self._is_paused