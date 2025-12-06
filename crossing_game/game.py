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
        self._player = Player(self._screen_height)
        self._bind_keys()
        self.car_manager = CarManager()
        self._scoreboard = Scoreboard(self._screen_width, self._screen_height)
        self.car_manager.set_street(self._screen_width, self._screen_height, self._player.minimum_size)
        self.update_interval: float = 1 / 60
        self._is_running: bool = False
        self._is_paused: bool = False
        self._quit_game: bool = False

    def run(self) -> None:
        self._start_game()
        while not self._quit_game:
            last_update = 0
            while self._is_running:
                if self._quit_game:
                    break
                now = time()
                delta = now - last_update
                if delta >= self.update_interval and not self._is_paused:
                    self._update()
                    last_update = now
                self._render()
                sleep(0.001)
            sleep(0.1)
            self._render()
        self._window._screen.bye()

    def _bind_keys(self) -> None:
        self._window._screen.listen()
        self._window._screen.onkey(self._start_game, "r")
        self._window._screen.onkey(self._move_player, "Up")
        self._window._screen.onkey(self._toggle_pause, "p")
        self._window._screen.onkey(self._toggle_quit, "q")

    def _render(self) -> None:
        self._window._screen.update()

    def _update(self) -> None:
        self.car_manager.move_cars()
        player_bbox = self._player.get_bounding_box()
        if self.car_manager.check_crashes(player_bbox):
            self._is_running = False
            self._scoreboard.game_over()
            self._scoreboard.show_input_message()
            return
        if self._player.finished():
            self.car_manager.increment_car_velocities()
            self._scoreboard.player_finished()
            self._scoreboard.update_score()
        self.car_manager.check_cars_finished()

    def _toggle_pause(self) -> None:
        if not self._is_running:
            return
        self._is_paused = not self._is_paused

    def _toggle_quit(self) -> None:
        self._quit_game = not self._quit_game

    def _start_game(self) -> None:
        if self._is_running:
            return
        self._is_running = True
        self._is_paused = False
        self._player.move_to_start()
        self.car_manager.reposition_all_cars()
        self.car_manager.restart_car_velocities()
        self._scoreboard.restart_player_score()
        self._scoreboard.update_score()

    def _move_player(self) -> None:
        if not self._is_running:
            return
        self._player.move_up()