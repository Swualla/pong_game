from turtle import Turtle
PADDLE_SIZE = 6
UP = 90
DOWN = 270
MOVE_DISTANCE = 20
NET_START_POS = (0, 280)
NET_END_POS = (0, -280)


class Paddle:

    def __init__(self, paddle_position):
        self.paddle = []
        self.make_paddle(paddle_position)
        self.top = self.paddle[0]
        self.bottom = self.paddle[PADDLE_SIZE - 1]

    def make_paddle(self, position):
        y_start = position[1]
        for _ in range(PADDLE_SIZE):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position[0], y_start)
            segment.setheading(90)
            self.paddle.append(segment)
            y_start -= 20

    def move(self):
        for segment in range(len(self.paddle)):
            self.paddle[segment].forward(MOVE_DISTANCE)

    def up(self):
        if self.top.ycor() != 280:
            for segment in range(len(self.paddle)):
                self.paddle[segment].setheading(UP)
            self.move()

    def down(self):
        if self.bottom.ycor() != -280:
            for segment in range(len(self.paddle)):
                self.paddle[segment].setheading(DOWN)
            self.move()

    def make_net_section(self, net_start):
        self.make_paddle(NET_START_POS)


