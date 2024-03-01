from turtle import Turtle
FONT = ("Arial", 50, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 200)
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.clear()
        self.write(f"{self.score1}    {self.score2}", align="center", font=FONT)

    def point(self, x_cord):
        if x_cord < -289:
            self.score1 += 1
            self.draw_scoreboard()
        elif x_cord > 289:
            self.score2 += 1
            self.draw_scoreboard()



