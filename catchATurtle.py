'''
Random appearance of the shape on different parts of the screen
The event of a shape being clicked
The score updating
The timer updating
'''
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
xMin = -300
xMax = 300
yMin = -300
yMax = 300
score = 0

timer = 30
timerUp = False
counterInterval = 1000
color = "red"
shape = "triangle"
size = 2

fontSetup = ("Arial", 20, "normal")


#-----initialize turtle-----
t = trtl.Turtle()
t.shape(shape)
t.turtlesize(size)
t.fillcolor(color)
t.penup()

scoreWriter = trtl.Turtle()
scoreWriter.penup()
scoreWriter.goto(300,-300)

counter = trtl.Turtle()
counter.penup()
counter.goto(-300, -300)

#-----game functions--------
def spot_clicked(x, y):

    t.goto(rand.randint(xMin,xMax), rand.randint(yMin,yMax))

    scoreChange()

def scoreChange():
    global score
    score += 1
    #print(score)
    scoreWriter.clear()
    scoreWriter.write(score, font=fontSetup)

def countdown():
    global timer, timerUp
    counter.clear()
    if timer <=0:
        counter.write("Time's Up", font=fontSetup)
        timerUp = True
    else:
        counter.write("Timer: " + str(timer), font=fontSetup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counterInterval)



#-----events----------------
t.onclick(spot_clicked)
wn = trtl.Screen()

wn.ontimer(countdown, counterInterval)
wn.mainloop()