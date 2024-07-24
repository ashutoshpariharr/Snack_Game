import time
from food import Food
from snack_game import Snack
from score_board import Scoreboard
from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()
snack = Snack()
food = Food()
score = Scoreboard()


turtle.write("Home = ", True, align="center")
screen.title("Welcome over Snack Game")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(650, 650)
screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")
screen.onkey(snack.down, "Down")

is_over = True
while is_over:
    screen.update()
    time.sleep(0.1)
    snack.move()
    # Detect the food
    if snack.head.distance(food) < 15:
        food.refresh()
        snack.extend()
        score.increase_score()

    # When snack hit the wall game over
    if snack.head.xcor() > 280 or snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280:
        score.reset()
        snack.reset()

    for segment in snack.segment[1:]:
        if snack.head.distance(segment) < 10:
            score.reset()
            snack.reset()

screen.exitonclick()