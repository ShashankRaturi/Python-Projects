import turtle as t
import random 
from color import random_color

t.colormode(255)

tur = t.Turtle()
tur.shape('turtle')
################# different shapes   ###########




def shape(num_of_sides):
    angle = 360 / num_of_sides

    for i in range(num_of_sides):
        tur.forward(100)
        tur.right(angle)


for i in range(3 , 11):
    tur.color(random_color())
    shape(i)



screen = t.Screen()
screen.exitonclick()
