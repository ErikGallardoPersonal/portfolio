from turtle import Screen
from time import sleep
from snake import Snake
WINDOW_WIDTH_PIX = 600
WINDOW_HEIGHT_PIX = WINDOW_WIDTH_PIX

def main():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH_PIX, height=WINDOW_HEIGHT_PIX)
    screen.bgcolor("black")
    screen.title("Ouroboros")
    screen.tracer(0)

    snake = Snake()
    is_game_running = True
    while is_game_running:
        screen.update()
        sleep(0.1)
        snake.move()

    screen.exitonclick()

if __name__ == "__main__":
    main()