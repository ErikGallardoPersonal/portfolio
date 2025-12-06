from turtle import Screen
class Window:
    def __init__(self) -> None:
        self._screen = Screen()
        self._screen.clearscreen()
        self._screen.setup(
            width=600,
            height=600
        )
        # self._screen.cv._rootwindow.resizable(False, False)
        self._screen.bgcolor("white")
        self._screen.title("Crossing the street")
        self._screen.tracer(0)

    def screensize(self) -> tuple[int, int]:
        return self._screen.window_width(), self._screen.window_height()