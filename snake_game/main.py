from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from constants import WINDOW_WIDTH_PIX, WINDOW_HEIGHT_PIX, FOOD_SIZE_PIX, SNAKE_SEGMENT_SIZE_PIX
from time import sleep

def main():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH_PIX, height=WINDOW_HEIGHT_PIX)
    screen.bgcolor("black")
    screen.title("Ouroboros")
    screen.tracer(0)

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
        
    screen.exitonclick()

if __name__ == "__main__":
    main()