# ##################################################
# ### SETUP ###
import turtle
turtle.bgcolor("black")
# ##################################################

t = turtle.Turtle()
t.penup()
t.goto(-100, 50)
t.color("maroon")
t.speed(10)
t.pendown()

#repeating movement
for i in range(10000):
    t.forward(400)
    t.left(210 + 1)
    t.speed(10)


t.forward(300)


# ##################################################
# ### ENDING ###
turtle.exitonclick()
# ##################################################