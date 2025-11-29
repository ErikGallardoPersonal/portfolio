from random import choice
from turtle import Turtle

class Ball(Turtle):
    def __init__(self, ):
        super().__init__(shape = "square")

    def move(self):
        ...

    def has_collided_with_paddle(self):
        ...

    def has_collided_with_wall(self):
        ...
    
    def has_scored(self):
        ...