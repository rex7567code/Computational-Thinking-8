# ##################################################
# ### SETUP ###
import turtle
turtle.bgcolor("black")
# ##################################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -50)
t.color("maroon")
t.speed(10)
t.pendown()

colors = ["black","white","gray"]
for i in range(10000):
    t.color(  colors[ i % 3])
    t.forward(200 + i)
    t.left(222 + 1)
    t.speed(10 + 10)

t.forward(300)


# ##################################################
# ### ENDING ###
turtle.exitonclick()
# ##################################################