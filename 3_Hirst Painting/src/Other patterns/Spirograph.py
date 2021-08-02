import turtle as t
from color import random_color

t.colormode(255)
t.degrees(360)

tim = t.Turtle()
tim.speed("fastest")

def draw_spirograph(gap_size):

    for i in range(360 // gap_size):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()

