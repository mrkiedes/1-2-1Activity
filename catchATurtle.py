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
xMin = 0
xMax = 112
yMin = 0
yMax = 324

color = "red"
shape = "triangle"
size = 2

#-----initialize turtle-----
t = trtl.Turtle()
t.shape(shape)
t.turtlesize(size)
t.fillcolor(color)

#-----game functions--------
def spot_clicked(x, y):
    t.goto(rand.randint(xMin,xMax), rand.randint(yMin,yMax))


#-----events----------------
t.onclick(spot_clicked)



wn = trtl.Screen()
wn.mainloop()