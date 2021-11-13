from turtle import Turtle
from CONST import SCREEN_HEIGHT, SCREEN_WIDTH


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#666")
        self.speed(0)
        self.goto(0, -SCREEN_HEIGHT//2 + 200)
        self.dir_x = 1
        self.dir_y = 1

    def move(self):
        if self.xcor() > SCREEN_WIDTH//2 - 10 or self.xcor() < -SCREEN_WIDTH//2 + 10:
            self.dir_x *= -1
        if self.ycor() > SCREEN_HEIGHT//2 - 10 or self.ycor() < -SCREEN_HEIGHT//2 + 10:
            self.dir_y *= -1

        if not self.ycor() < -250 - 20:
            self.setx(self.xcor() + self.dir_x)
            self.sety(self.ycor() + self.dir_y)
        else:
            self.goto(0, -SCREEN_HEIGHT//2 + 200)

    def bounce_back(self):
        self.dir_y *= -1
        self.dir_x *= -1

    def bounce_for(self):
        self.dir_y *= -1

    def bounce_left(self):
        self.dir_x *= -1

    def level_up(self):
        self.dir_x = 1
        self.dir_y = 1
        self.dir_x += 1
        self.dir_y += 1

        self.goto(0, -SCREEN_HEIGHT//2 + 200)
