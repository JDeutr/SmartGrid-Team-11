# import package and making objects
import turtle
import numpy as np
 
sc=turtle.Screen()
trtl=turtle.Turtle()
 
# method to draw y-axis lines
def drawy(val):
     
    # line
    trtl.up()
    trtl.setpos(-250 + val, -250)

    trtl.down()
    trtl.forward(500)
    
def drawx(val):
     
    # line
    trtl.up()
    trtl.setpos(-250, -250 + val)

    trtl.down()
    trtl.forward(500)
     

# Main Section
# set screen
sc.setup(600,600)   
 
# set turtle features
trtl.speed(100)
trtl.left(90) 
trtl.color('lightgreen')
 
# y lines
for i in range(51):
    drawy(10*(i))
    
trtl.right(90)

for i in range(51):   
    drawx(10*(i))

trtl.hideturtle()

def lab():
    
    trtl.color('green')

    # set position
    trtl.penup()
    trtl.setpos(-200, -270)

    for value in range(5, 51, 5): 

        trtl.pendown()
        
        # write value
        trtl.write(value,font=("Verdana", 8))
        trtl.penup()

        trtl.forward(50)

    trtl.left(90)
    trtl.setpos(-270, -205)

    for value in range(5, 51, 5): 

        trtl.pendown()
        
        # write value
        trtl.write(value,font=("Verdana", 8))
        trtl.penup()

        trtl.forward(50)

    # set position for x axis
    trtl.right(90)
    trtl.up()
    trtl.setpos(-250,-250)
    trtl.down()
 
    # x-axis
    trtl.forward(500)
 
    # set position for y axis
    trtl.left(90)
    trtl.up()
    trtl.setpos(-250,-250)
    trtl.down()
 
    # y-axis
    trtl.forward(500)

lab()

turtle.done()

zero = np.zeros((5,2))