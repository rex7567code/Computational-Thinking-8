# Beginning: create variables
g_points = 0
b_points = 0

# Middle: ask questions
answer = input("if you are flying through the desert and your boat gets a flat tire what should you have in your back pocket? A) C4, or B) 8 grains of water")
if answer.lower() == "a":
    g_points += 1
elif answer.lower() == "b":
    b_points += 1

answer = input("would you rather, A) cary a cumbersome cucumber through cambodia, or B) gain 1 scoliosis?")
if answer.lower() == "a":
    g_points += 1
elif answer.lower() == "b":
    b_points += 1

answer = input("does cy8mxioecym98 9v7373?, A) y8yx8of, or B) 22222222222222222222222")
if answer.lower() == "a":
    g_points += 1
elif answer.lower() == "b":
    b_points += 1

answer = input("cause of death, A) hit by supersonic green whale, or B) fell of of a bottle of sunscreen")
if answer.lower() == "a":
    g_points += 1
elif answer.lower() == "b":
    b_points += 1

answer = input("Mong Mango cheese, hello, good nutrition on your back and man, everyone greeted. A) hand mirror, or B) cowboy hat")
if answer.lower() == "a":
    g_points += 1
elif answer.lower() == "b":
    b_points += 1

answer = input("what does your grandpa call you? A) little munchkin, or B) nothing, he just tries to eat you")
if answer.lower() == "a":
    g_points += 1
elif answer.lower() == "b":
    b_points += 1

answer = input("He wondered if she would appreciate his toenail collection. A) oh no, B) gasp")
if answer.lower() == "a":
    g_points += 1
elif answer.lower() == "b":
    b_points += 1

#End: determine results
if g_points > b_points:
    print("5 nanoseconds after you turn -36, you will lead an army of 3 year old businessmen to colonize russia")
elif b_points > g_points:
    print("freakbob no-pants will break into your house on march 86th and dropkick you into the sun")
elif g_points == b_points:
    print("The old rusted farm equipment surrounded the house predicting its demise.")