from turtle import Turtle
STARTING_POSITIONS= [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for turtle_index in STARTING_POSITIONS:
            self.add_turtle(turtle_index)

    def add_turtle(self,turtle_index):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(turtle_index)
        self.turtles.append(new_turtle)

    def reset(self):
        for tur in self.turtles:
            tur.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]


    def extend(self):
        #add a new segment to the snake
        self.add_turtle(self.turtles[-1].position())


    def move(self):
        for tur_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[tur_num - 1].xcor()
            new_y = self.turtles[tur_num - 1].ycor()
            self.turtles[tur_num].goto(new_x, new_y)
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
