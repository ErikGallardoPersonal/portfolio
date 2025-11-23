from turtle import Turtle

class Snake:
    def __init__(self) -> None:
        self._segments: list[Turtle] = []
        self._segment_size = 20
        self._init_segments()

    def _init_segments(self):
        segment_position = [0, 0]
        for _ in range(3):
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto(segment_position[0], segment_position[1])
            self._segments.append(snake_segment)
            segment_position[0] -= self._segment_size

    def _segment_propagation(self):
        for seg_idx in range(len(self._segments)-1, 0, -1):
            current_segment = self._segments[seg_idx]
            next_segment = self._segments[seg_idx-1]
            current_segment.goto(next_segment.pos())

    def move(self):
        self._segment_propagation()
        self._segments[0].forward(self._segment_size)