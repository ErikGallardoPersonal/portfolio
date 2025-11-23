from turtle import Turtle, Screen
from time import sleep
WINDOW_WIDTH_PIX = 600
WINDOW_HEIGHT_PIX = WINDOW_WIDTH_PIX
TURTLE_WIDTH_PIX = 20
TURTLE_HEIGHT_PIX = 20


def main():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH_PIX, height=WINDOW_HEIGHT_PIX)
    screen.bgcolor("black")
    screen.title("Ouroboros")
    screen.tracer(0)

    snake_segments: list[Turtle] = []
    segment_position = [0, 0]
    for _ in range(3):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(segment_position[0], segment_position[1])
        snake_segments.append(snake_segment)
        segment_position[0] -= TURTLE_WIDTH_PIX

    is_game_running = True
    while is_game_running:
        screen.update()
        sleep(0.1)
        snake_size = len(snake_segments)
        next_segment_pos_pix = [0, 0]
        for seg_idx in range(snake_size-1, 0, -1):
            current_segment = snake_segments[seg_idx]
            next_segment = snake_segments[seg_idx-1]
            next_segment_pos_pix = [*next_segment.pos()]
            current_segment.goto(next_segment_pos_pix[0], next_segment_pos_pix[1])
        snake_segments[0].forward(TURTLE_WIDTH_PIX)

    screen.exitonclick()

if __name__ == "__main__":
    main()