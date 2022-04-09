from turtle import Screen
from snake import Snakes
import time
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("my snack game")
screen.bgcolor("black")
# here we are skip the animation of the moving blocks one by one
screen.tracer(0)

# creating object from class.
snake = Snakes()
food = Food()
score_board = ScoreBoard()

# for giving the direction to snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    # and now we refresh (in other words skip animation and see full  done graphics
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detection of collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.refresh_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()

    # detect collision with his tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()

