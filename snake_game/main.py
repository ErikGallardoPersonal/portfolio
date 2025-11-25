from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from grid import Grid
from constants import WINDOW_WIDTH_PIX, WINDOW_HEIGHT_PIX, FOOD_SIZE_PIX, SNAKE_SEGMENT_SIZE_PIX
from time import sleep

def main():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH_PIX+SNAKE_SEGMENT_SIZE_PIX, height=WINDOW_HEIGHT_PIX+SNAKE_SEGMENT_SIZE_PIX)
    screen.cv._rootwindow.resizable(False, False) # Disable Window Resize
    screen.bgcolor("black")
    screen.title("Ouroboros")
    screen.tracer(0)

    grid = Grid()
    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(fun= snake.turn_up, key="Up")
    screen.onkey(fun=snake.turn_down, key="Down")
    screen.onkey(fun= snake.turn_left, key="Left")
    screen.onkey(fun=snake.turn_right , key="Right")

    is_game_running = True
    while is_game_running:
        screen.update()
        sleep(0.1)
        snake.move()
    
        # Detect collision with food
        if snake.head.distance(food) < SNAKE_SEGMENT_SIZE_PIX//2 + FOOD_SIZE_PIX//2:
            food.reposition()
            score.update_score()
            snake.extend()
            
        # Detect collision with frame
        if  (snake.head.xcor() < -WINDOW_WIDTH_PIX//2 + SNAKE_SEGMENT_SIZE_PIX //2) or\
            (snake.head.xcor() > WINDOW_WIDTH_PIX//2 - SNAKE_SEGMENT_SIZE_PIX //2) or\
            (snake.head.ycor() < -WINDOW_HEIGHT_PIX//2 + SNAKE_SEGMENT_SIZE_PIX //2) or\
            (snake.head.ycor() > WINDOW_HEIGHT_PIX//2 - SNAKE_SEGMENT_SIZE_PIX //2):
            is_game_running = False
            score.game_over()
    screen.exitonclick()

if __name__ == "__main__":
    main()