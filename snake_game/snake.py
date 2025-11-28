from turtle import Turtle
from enum import IntEnum
from constants import GRID_SIZE_PIX


class TurnDegrees(IntEnum):
    RIGHT = 0
    UP = 90
    LEFT = 180
    DOWN = 270
    FULL = 360


class Snake:
    def __init__(self) -> None:
        self.segment_size_pix = GRID_SIZE_PIX
        self._collision_margin = 2
        self.segments: list[Turtle] = []
        self._init_segments()
        self.can_turn = True

    @property
    def head(self) -> Turtle:
        return self.segments[-1]

    def move(self) -> None:
        self._segment_propagation()
        self.head.forward(self.segment_size_pix)
        self.can_turn = True

    def _turn(self, desired_direction: TurnDegrees):
        if not self.can_turn:
            return
        if not self._is_valid_movement(current_direction=self.head.heading(),
                                       desired_direction=desired_direction):
            return
        self.head.setheading(desired_direction)
        self.can_turn = False

    def turn_up(self) -> None:
        self._turn(TurnDegrees.UP)

    def turn_down(self) -> None:
        self._turn(TurnDegrees.DOWN)

    def turn_left(self) -> None:
        self._turn(TurnDegrees.LEFT)

    def turn_right(self) -> None:
        self._turn(TurnDegrees.RIGHT)

    def ate(self, food: Turtle) -> bool:
        return self.head.distance(food) < self.segment_size_pix//2 + GRID_SIZE_PIX//2 - self._collision_margin

    def collided_with_wall(self, x_limit_pix: int, y_limit_pix: int) -> bool:
        margin = self.segment_size_pix // 2 + self._collision_margin
        return (self.head.xcor() < -x_limit_pix + margin or self.head.xcor() > x_limit_pix - margin) or\
            (self.head.ycor() < -y_limit_pix +
             margin or self.head.ycor() > y_limit_pix - margin)

    def collided_with_tail(self) -> bool:
        for current_segment in self.segments[:-1]:
            if self.head.distance(current_segment) < self.segment_size_pix - self._collision_margin:
                return True
        return False

    def extend(self) -> None:
        self.head.forward(self.segment_size_pix)
        head_position = self.head.pos()
        head_heading = self.head.heading()
        self.head.backward(self.segment_size_pix)
        snake_segment = self._create_segment(seg_pos_x_pix=head_position[0],
                                             seg_pos_y_pix=head_position[1],
                                             direction=head_heading,
                                             segment_size_ratio=self.segment_size_pix/20)
        self.segments.append(snake_segment)

    def _init_segments(self) -> None:
        INITIAL_SEGMENTS = 3
        OFFSET = 3
        seg_x_pix = (INITIAL_SEGMENTS - OFFSET - 1) * self.segment_size_pix
        seg_y_pix = 0
        for _ in range(INITIAL_SEGMENTS):
            snake_segment = self._create_segment(seg_pos_x_pix=seg_x_pix,
                                                 seg_pos_y_pix=seg_y_pix,
                                                 direction=TurnDegrees.RIGHT,
                                                 segment_size_ratio=self.segment_size_pix/20)
            self.segments.append(snake_segment)
            seg_x_pix += self.segment_size_pix

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
        snake_segment.shapesize(
            stretch_len=segment_size_ratio, stretch_wid=segment_size_ratio)
        snake_segment.goto(seg_pos_x_pix, seg_pos_y_pix)
        return snake_segment

    @staticmethod
    def _is_valid_movement(current_direction: TurnDegrees, desired_direction: TurnDegrees) -> bool:
        contrary_direction = Snake._get_contrary_direction(current_direction)
        return not (desired_direction == current_direction or desired_direction == contrary_direction)

    @staticmethod
    def _get_contrary_direction(direction: TurnDegrees) -> int:
        inverse_direction = direction + TurnDegrees.FULL // 2
        if inverse_direction >= TurnDegrees.FULL:  # limit direction to positive values between 0 and 270
            inverse_direction -= TurnDegrees.FULL
        return inverse_direction
