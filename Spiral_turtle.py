import turtle
MAX_LENGTH = 250
INCREMENT = 10

def spiral_by_turle(a_turtle,line_length):
    if line_length > MAX_LENGTH:
        return
    a_turtle.forward(line_length)
    a_turtle.right(90)
    spiral_by_turle(a_turtle,line_length + INCREMENT)

my_turtle = turtle.Turtle(shape="turtle")
my_turtle.pensize(5)
my_turtle.color("black")
spiral_by_turle(my_turtle,10)
turtle.done()