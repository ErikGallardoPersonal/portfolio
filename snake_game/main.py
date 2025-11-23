from turtle import Turtle, Screen

WINDOW_WIDTH_PIX = 600
WINDOW_HEIGHT_PIX = WINDOW_WIDTH_PIX
TURTLE_WIDTH_PIX = 20
TURTLE_HEIGHT_PIX = 20


def main():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH_PIX, height=WINDOW_HEIGHT_PIX)
    screen.bgcolor("black")
    screen.title("Ouroboros")

    segment_position = [0, 0]
    for _ in range(3):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.goto(segment_position[0], segment_position[1])
        segment_position[0] -= TURTLE_WIDTH_PIX

    screen.exitonclick()

if __name__ == "__main__":
    main()