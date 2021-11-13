from turtle import Turtle
from CONST import SCREEN_WIDTH, SCREEN_HEIGHT


MOVE_PACE = 40
START_POS = (0, -250)
# SCREEN_WIDTH = 630
# SCREEN_HEIGHT = 630


class Paddle(Turtle):
    def __init__(self, size: str) -> None:
        super().__init__()
        self.penup()
        self.size = size.lower()
        self.__set_paddle_width()
        self.draw_paddle()

    def draw_paddle(self):
        self = self
        self.shape("square")
        self.speed(0)
        self.penup()
        self.color("#f7f7f7")
        self.shapesize(0.1, self.width, outline=6)

        self.setx(0)
        self.sety(-250)

    def move_right(self):
        x = self.xcor()
        y = self.ycor()
        if (x + (self.width * 20) // 2) + MOVE_PACE < SCREEN_WIDTH//2 - 8:
            self.goto(x+MOVE_PACE, y)
        else:
            self.goto((SCREEN_WIDTH//2 - (self.width * 20) // 2), y)

    def move_left(self):
        x = self.xcor()
        y = self.ycor()
        if (x - (self.width * 20) // 2) - MOVE_PACE > -SCREEN_WIDTH//2:
            self.goto(x-MOVE_PACE, y)
        else:
            self.goto((-SCREEN_WIDTH//2 + (self.width * 20) // 2), y)

    def on_mouse_move(self, screen, func, add=None):
        def event_func(event):
            func(screen.cv.canvasx(event.x) / screen.xscale, -
                 screen.cv.canvasy(event.y) / screen.yscale)
        screen.cv.bind('<Motion>', event_func, add)

    def drag_handle(self, x, y):
        self.ondrag(None)
        if x - (self.width*20) // 2 > -SCREEN_WIDTH // 2 and x + (self.width*20) // 2 < SCREEN_WIDTH//2:
            self.goto(x, self.ycor())
        self.ondrag(self.drag_handle)

    def __set_paddle_width(self):
        assert self.size in [
            "s", "m", "l"], "Bad value for size must be s, m or l"
        if self.size == "s":
            self.width = 2
        elif self.size == "m":
            self.width = 4
        elif self.size == "l":
            self.width = 6
