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
        self.segments: list[Turtle] = []
        self._init_segments()
    
    @property
    def head(self) -> Turtle:
        return self.segments[-1]

    def move(self) -> None:
        self._segment_propagation()
        self.head.forward(self._segment_size)

    def turn_up(self) -> None:
        if not self._is_valid_movement(current_direction=self.head.heading(),
                                        desired_direction=TurnDegrees.UP):
            return
        self.head.setheading(TurnDegrees.UP)

    def turn_down(self) -> None:
        if not self._is_valid_movement(current_direction=self.head.heading(),
                                        desired_direction=TurnDegrees.DOWN):
            return
        self.head.setheading(TurnDegrees.DOWN)

    def turn_left(self) -> None:
        if not self._is_valid_movement(current_direction=self.head.heading(),
                                        desired_direction=TurnDegrees.LEFT):
            return
        self.head.setheading(TurnDegrees.LEFT)

    def turn_right(self) -> None:
        if not self._is_valid_movement(current_direction=self.head.heading(),
                                        desired_direction=TurnDegrees.RIGHT):
            return
        self.head.setheading(TurnDegrees.RIGHT)

    def extend(self) -> None:
        self.head.forward(self._segment_size)
        head_position = self.head.pos()
        head_heading = self.head.heading()
        self.head.backward(self._segment_size)
        snake_segment = self._create_segment(seg_pos_x_pix=head_position[0],
                                                seg_pos_y_pix=head_position[1],
                                                direction=head_heading,
                                                segment_size_ratio=self._segment_size/20)
        self.segments.append(snake_segment)

    def _init_segments(self) -> None:
        INITIAL_SEGMENTS = 3
        seg_x_pix = (INITIAL_SEGMENTS - 1) * self._segment_size
        seg_y_pix = 0
        for _ in range(INITIAL_SEGMENTS):
            snake_segment = self._create_segment(seg_pos_x_pix=seg_x_pix,
                                                 seg_pos_y_pix=seg_y_pix,
                                                 direction=TurnDegrees.RIGHT,
                                                 segment_size_ratio=self._segment_size/20)
            self.segments.append(snake_segment)
            seg_x_pix += self._segment_size

    def _segment_propagation(self) -> None:
        for seg_idx in range(0, len(self.segments)-1):
            current_segment = self.segments[seg_idx]
            next_segment = self.segments[seg_idx+1]
            current_segment.goto(next_segment.pos())

    @staticmethod
    def _create_segment(seg_pos_x_pix: int, seg_pos_y_pix: int, direction: TurnDegrees, segment_size_ratio: int) -> Turtle:
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.setheading(direction)
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