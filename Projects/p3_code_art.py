# ##################################################
# ### SETUP ###
import turtle
turtle.bgcolor("black")
# ##################################################

t = turtle.Turtle()
t.penup()
t.goto(-200, 80)
t.color("maroon")
t.speed(10)
t.pendown()

#repeating movement
for i in range(2000):
    t.forward(500)
    t.left(210 + 1)
    t.speed(10)


t.forward(300)


# ##################################################
# ### ENDING ###
turtle.exitonclick()
# ##################################################