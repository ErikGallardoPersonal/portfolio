from enum import Enum

FONT = ("Courier", 24, "normal")

class Shape(Enum):
    SQUARE = "square"
    TURTLE = "turtle"

class Color(Enum):
    WHITE = "white"
    BLACK = "black"
    RED = "red"
    ORANGE = "orange"
    YELLWO = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"

MINIMUM_SIZE_PIX = 20