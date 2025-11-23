from turtle import Turtle
from enum import IntEnum
from constants import SNAKE_SEGMENT_SIZE_PIX

class TurnDegrees(IntEnum):
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

class Snake:
    def __init__(self, segment_size: int = SNAKE_SEGMENT_SIZE_PIX) -> None:
        self._segment_size = segment_size
        self._segments: list[Turtle] = []
        self._init_segments()
        self.head = self._segments[0]

    def move(self):
        self._segment_propagation()
        self.head.forward(self._segment_size)

    def turn_up(self):
        if self.head.heading() == TurnDegrees.DOWN:
            return
        self.head.setheading(TurnDegrees.UP)
        self.move()

    def turn_down(self):
        if self.head.heading() == TurnDegrees.UP:
            return
        self.head.setheading(TurnDegrees.DOWN)
        self.move()

    def turn_left(self):
        if self.head.heading() == TurnDegrees.RIGHT:
            return
        self.head.setheading(TurnDegrees.LEFT)
        self.move()

    def turn_right(self):
        if self.head.heading() == TurnDegrees.LEFT:
            return
        self.head.setheading(TurnDegrees.RIGHT)
        self.move()

    def _init_segments(self):
        segment_position = [0, 0]
        for _ in range(3):
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            segment_size = SNAKE_SEGMENT_SIZE_PIX/20
            snake_segment.shapesize(stretch_len=segment_size, stretch_wid=segment_size)
            snake_segment.goto(segment_position[0], segment_position[1])
            self._segments.append(snake_segment)
            segment_position[0] -= self._segment_size

    def _segment_propagation(self):
        for seg_idx in range(len(self._segments)-1, 0, -1):
            current_segment = self._segments[seg_idx]
            next_segment = self._segments[seg_idx-1]
            current_segment.goto(next_segment.pos())