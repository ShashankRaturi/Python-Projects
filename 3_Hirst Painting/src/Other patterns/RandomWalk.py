import turtle as t
import random 
from color import random_color

t.colormode(255)
turte = t.Turtle()

event = [1 , -1]

turte.pensize(15)
turte.speed("fastest")


for i in range(200):
    result = random.choice(event)

    if result == 1:
        turte.right(90)
    else :
        turte.left(90)
    
    turte.color(random_color())
    turte.forward(30)




screen = t.Screen()
screen.exitonclick()


