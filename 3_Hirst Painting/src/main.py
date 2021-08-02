import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.hideturtle()
tim.speed('fastest')

rgb_colors = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (194, 38, 81), 
			(237, 161, 50), (234, 215, 86), (226, 237, 229), (223, 137, 176), (143, 108, 57), (102, 197, 219), 
			(205, 166, 30), (21, 57, 132), (214, 74, 91), (238, 89, 49), (119, 192, 140), (142, 208, 227), (4, 185, 176), 
			(106, 108, 198), (138, 29, 72), (5, 161, 86), (98, 51, 36), (23, 156, 209), (229, 167, 185), (173, 185, 222), 
			(29, 90, 95), (233, 172, 162), (155, 212, 190), (88, 46, 33), (244, 207, 5), (35, 47, 85), (31, 93, 92), (101, 24, 56)]




for i in range(10):
	for j in range(10):
		
		tim.dot(20 , random.choice(rgb_colors))
		if j != 9:
			tim.penup()
			tim.forward(30)
			tim.pendown()

	if i % 2 == 0:
		tim.left(90)
		tim.penup()
		tim.forward(30)
		tim.pendown()
		tim.left(90)
	
	else:
		tim.right(90)
		tim.penup()
		tim.forward(40)
		tim.pendown()
		tim.right(90)



screen = t.Screen()
screen.exitonclick()