import time
import sys
from turtle import Screen
from paddle_module import Paddle
from obstacle_drawer import ObjectsDrawer
from CONST import SCREEN_WIDTH, SCREEN_HEIGHT
from ball import Ball


screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("#333")
screen.title("80's BreakOut")
screen.tracer(0)

p = Paddle("l")
op = ObjectsDrawer()
my_ball = Ball()
screen.onkeypress(p.move_left, "f")
screen.onkeypress(p.move_right, "j")
p.on_mouse_move(screen, p.drag_handle)
screen.listen()


while True:
    screen.update()
    time.sleep(0.001)
    my_ball.move()
    if my_ball.ycor() >= p.ycor() - 10 and my_ball.ycor() <= p.ycor() + 10:
        if my_ball.xcor() > p.xcor() - p.width*20//2 and my_ball.xcor() < p.xcor():
            if my_ball.dir_x < 0:
                my_ball.bounce_for()
            else:
                my_ball.bounce_back()
        elif my_ball.xcor() < p.xcor() + p.width*20//2 and my_ball.xcor() > p.xcor():
            if my_ball.dir_x > 0:
                my_ball.bounce_for()
            else:
                my_ball.bounce_back()
    if op.turtles:
        for t in op.turtles:
            if abs(t.xcor() - my_ball.xcor()) < 30 and abs(t.ycor() - my_ball.ycor()) < 30:
                if my_ball.dir_x > 0:
                    my_ball.dir_x -= 0.02
                else:
                    my_ball.dir_x += 0.02

                if my_ball.dir_y > 0:
                    my_ball.dir_y -= 0.02
                else:
                    my_ball.dir_y += 0.02

                if abs(t.xcor() - my_ball.xcor()) > abs(t.ycor() - my_ball.ycor()):
                    my_ball.bounce_left()
                else:
                    my_ball.bounce_for()
                t.hideturtle()
                op.turtles.remove(t)
    else:
        op.level_up()
        my_ball.level_up()
