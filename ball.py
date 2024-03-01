from turtle import Turtle
import random
START_HEADING = [45, 135, 225, 315]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.8, 0.8)
        self.color("white")
        self.penup()
        self.tiltangle(45)
        self.setposition(0, random.randint(-280, 280))
        self.setheading(random.choice(START_HEADING))
        self.move_speed = 0.1

    def movement(self, speed):
        self.forward(speed)

    def wall_collision(self):
        if self.heading() == 45:
            self.setheading(315)
        elif self.heading() == 315:
            self.setheading(45)
        elif self.heading() == 135:
            self.setheading(225)
        elif self.heading() == 225:
            self.setheading(135)

    def paddle_collision(self):
        if self.heading() == 45:
            self.setheading(135)
        elif self.heading() == 315:
            self.setheading(225)
        elif self.heading() == 135:
            self.setheading(45)
        elif self.heading() == 225:
            self.setheading(315)
        self.move_speed *= 0.9

    def kick_off(self):
        self.setposition(0, random.randint(-280, 280))
        self.setheading(random.choice(START_HEADING))
        self.move_speed = 0.1



