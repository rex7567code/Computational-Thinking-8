# ##################################################
# ### SETUP ###
import turtle
turtle.bgcolor("black")
# ##################################################

t = turtle.Turtle()
t.penup()
t.goto(-200, -80)
t.color("blue")
t.speed(10)
t.pendown()

#repeating movement
    

for i in range(500):
    t.forward(500)
    t.left(83 + 6)
    t.speed(10)
#new circle
t.penup()
t.goto(-250, -250)
t.color("yellow")
t.pendown()
t.left(130)

for i in range(500):
    t.forward(500)
    t.left(83 + 6)
    t.speed(10)
#another circle
t.penup()
t.goto(0, 50)
t.color("magenta")
t.pendown()
t.left(100)


for i in range(500):
    t.forward(500)
    t.left(83 + 6)
    t.speed(10)
# ##################################################
# ### ENDING ###
turtle.exitonclick()
# ##################################################