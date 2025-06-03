# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# TODO - create your player character
s1 = create_sprite("cat2", -200, -200)
s2 = create_sprite("baseball",50 ,50)
s3 = create_sprite("rectangle", -250, -295)
s4 = create_sprite("rectangle", -100, -295)
s5 = create_sprite("rectangle", 0, -295)
s6 = create_sprite("rectangle", 100, -295)
s6 = create_sprite("rectangle" , 0, -190)
# TODO - set your background
set_background("castle")
# TODO - set the starting value for your variable

# Section 3: Controls
# TODO - define your controls
def jump():
	s1.setheading(90)
	s1.forward(70)
	window.update()
	time.sleep(0.1)
	s1.forward(50)
	window.update()
	time.sleep(0.1)
	s1.forward(10)

def right():
	s1.setheading(0)
	s1.forward(20)
	
def left():	
	s1.setheading(180)
	s1.forward(20)


# TODO - pick keys for each control
window.onkeypress(jump, "w")
window.onkeypress(right, "d")
window.onkeypress(left, "a")



# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.01)
	timer += 1  
	 
    
 	# TODO - code for automatic actions


		
	
	# if you are above the block
	if s1.xcor()> -100 and s1.xcor()< 100 and s1.ycor()> -80 and s1.ycor()< -79:
		# do nothing
		pass
	# else, 
	else:

		s1.setheading(270)
		s1.forward(5)

	#### Josh Gravity

	# fall down
	
	# if at the bottom
	# if s1.ycor() < -229:
	# 	s1.goto(s1.xcor(), -240)





	window.update()

	# if :
	# 	break
	

print("Game Over")
