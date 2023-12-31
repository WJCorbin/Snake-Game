import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_piece(position)

    def add_piece(self, position):
        new_turtle = t.Turtle("square")
        new_turtle.color("green")
        new_turtle.penup()
        new_turtle.goto(position)
        self.body.append(new_turtle)

    def extend(self):
        self.add_piece(self.body[-1].position())

    def reset_snake(self):
        for piece in self.body:
            piece.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def move(self):
        for piece in range(len(self.body) - 1, 0, -1):
            new_x = self.body[piece - 1].xcor()
            new_y = self.body[piece - 1].ycor()
            self.body[piece].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
