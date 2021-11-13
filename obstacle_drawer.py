from turtle import Turtle
from CONST import SCREEN_HEIGHT, SCREEN_WIDTH
import random


START_X = -SCREEN_WIDTH//2 + 30
START_Y = SCREEN_HEIGHT//2 - 150
MAX_ROWS = 4

COLORS = ["orange", "blue", "green", "red", "purple", "yellow", "brown"]


class ObjectsDrawer:
    def __init__(self) -> None:
        self.rows = 2
        self.draw()

    def draw(self):
        self.turtles = []
        move_x, move_y = 0, 0
        color_ind = 0
        random.shuffle(COLORS)
        current_row = 0
        while current_row < self.rows:
            t = Turtle("square")
            t_width = 3
            t.speed(0)
            t.setheading(90)
            t.penup()
            t.color(COLORS[color_ind])
            t.shapesize(stretch_len=2, stretch_wid=t_width, outline=0)
            t.goto(START_X + move_x, START_Y + move_y)
            step = (t_width * 20) + 3
            if t.xcor() + step > SCREEN_WIDTH // 2:
                move_x = 0
                move_y -= 45
                current_row += 1
                color_ind += 1
            else:
                move_x += step
            self.turtles.append(t)

    def level_up(self):
        if self.rows < MAX_ROWS:
            self.rows += 1
        self.draw()
