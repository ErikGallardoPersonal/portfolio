from window import Window
from ball import Ball
from paddle import Paddle
class Game:
    def __init__(self) -> None:
        self._window = Window()
        self._ball = Ball()
        self._player1 = Paddle()
        self._player2 = Paddle()

    def run(self) -> None:
        ...

    def _render(self):
        ...

    def _update(self):
        ...