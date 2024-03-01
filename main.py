import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

PLAYER_1_POS = (-370, 20)
PLAYER_2_POS = (370, 20)
BALL_START_SPEED = 10

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)

paddle1 = Paddle(PLAYER_1_POS)
paddle2 = Paddle(PLAYER_2_POS)
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkeypress(fun=paddle1.up, key="w")
screen.onkeypress(fun=paddle1.down, key="s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.movement(BALL_START_SPEED)
    paddle2.move()

    # Move computer paddle
    if paddle2.top.ycor() > 280:
        paddle2.down()
    elif paddle2.bottom.ycor() < -280:
        paddle2.up()

    # Check collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_collision()

    # Check if goal.
    if ball.xcor() > 390 or ball.xcor() < -390:
        scoreboard.point(ball.xcor())
        ball.kick_off()

    # Check paddle1 collision.
    for segment in paddle1.paddle:
        if ball.distance(segment) < 19:
            ball.paddle_collision()

    # Check paddle2 collision.
    for segment in paddle2.paddle:
        if ball.distance(segment) < 19:
            ball.paddle_collision()
















screen.exitonclick()
