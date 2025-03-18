###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("underwater")

q4 = codesters.Square(100, 100, 200, 'black')
q1 = codesters.TriangleRight(100, 100 , 200, 200,  'DeepPink')
q2 = codesters.Square(-100, 100 , 200,  'black')
q3 = codesters.Square(-100, -100 , 200,  'teal')
q5 = codesters.TriangleRight(-100, -100, 200, 200, 'black')
q4 = codesters.Square(100, -100, 200, 'black')

s1 = codesters.Sprite("cat3", 100, 100)
s1.set_size(0.2)
s2 = codesters.Sprite("draw", 98, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("sushi", -100, 100)
s4 = codesters.Sprite("image", -100, -100)
s4.set_size(0.3)

message1 = codesters.Text("Lionel", 0, 220,"black")
message2 = codesters.Text("Last time i did that before again", 0, -220,"black")