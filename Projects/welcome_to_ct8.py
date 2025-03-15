###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("moon")
mySprite = codesters.Sprite("kitten" , 4 , 5)
mySprite.say("i rule the wold!!!!!!")
mySprite2 = codesters.Sprite("soccerball" , 100 , -180)
mySprite3 = codesters.Sprite("spaceship" , -170 , 110)
mySprite3.set_size(0.03)
mySprite2.set_size(0.7)
mySprite4 = codesters.Sprite("flower" , -150 , -180)
mySprite4.set_size(2)