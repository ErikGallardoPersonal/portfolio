from turtle import Turtle
from enum import IntEnum
from constants import SNAKE_SEGMENT_SIZE_PIX

class TurnDegrees(IntEnum):
    RIGHT = 0
    UP = 90
    LEFT = 180
    DOWN = 270
    FULL = 360

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
        if not self._is_valid_movement(current_direction=self.head.heading(),
                                        desired_direction=TurnDegrees.UP):
            return
        self.head.setheading(TurnDegrees.UP)

    def turn_down(self):
        if not self._is_valid_movement(current_direction=self.head.heading(),
                                        desired_direction=TurnDegrees.DOWN):
            return
        self.head.setheading(TurnDegrees.DOWN)

    def turn_left(self):
        if not self._is_valid_movement(current_direction=self.head.heading(),
                                        desired_direction=TurnDegrees.LEFT):
            return
        self.head.setheading(TurnDegrees.LEFT)

    def turn_right(self):
        if not self._is_valid_movement(current_direction=self.head.heading(),
                                        desired_direction=TurnDegrees.RIGHT):
            return
        self.head.setheading(TurnDegrees.RIGHT)

    def _init_segments(self):
        segment_position = [0, 0]
        segment_size = SNAKE_SEGMENT_SIZE_PIX/20
        for _ in range(3):
            snake_segment = self._create_segment(seg_pos_x_pix=segment_position[0],
                                                 seg_pos_y_pix=segment_position[1],
                                                 segment_size_ratio=segment_size)
            self._segments.append(snake_segment)
            segment_position[0] -= self._segment_size

    def _segment_propagation(self):
        for seg_idx in range(len(self._segments)-1, 0, -1):
            current_segment = self._segments[seg_idx]
            next_segment = self._segments[seg_idx-1]
            current_segment.goto(next_segment.pos())

    @staticmethod
    def _create_segment(seg_pos_x_pix: int, seg_pos_y_pix: int, segment_size_ratio: int):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.shapesize(stretch_len=segment_size_ratio, stretch_wid=segment_size_ratio)
        snake_segment.goto(seg_pos_x_pix, seg_pos_y_pix)
        return snake_segment
    
    @staticmethod
    def _is_valid_movement(current_direction: TurnDegrees, desired_direction: TurnDegrees) -> bool:
        contrary_direction = Snake._get_contrary_direction(current_direction)
        return not(desired_direction == current_direction or desired_direction == contrary_direction)
        
    @staticmethod
    def _get_contrary_direction(direction: TurnDegrees) -> int:
        inverse_direction = direction + TurnDegrees.FULL // 2
        if inverse_direction >= TurnDegrees.FULL: # limit direction to positive values between 0 and 270
            inverse_direction -= TurnDegrees.FULL
        return inverse_direction