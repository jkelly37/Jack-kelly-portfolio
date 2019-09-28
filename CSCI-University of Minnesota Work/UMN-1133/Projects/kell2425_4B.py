
#  CSci 1133 HW 4
#  Jack Kelly
#  HW Problem 4B
import turtle
turtle.setworldcoordinates(-1, -1, 10, 10)
#function drawGrid recives one param of a list of lists. the function then parses through the values in the nested lists and draws a black square to its respected location in the turtle window if the value is equal to 0  
def drawGrid(grid):
    turtle.delay(0)
    turtle.speed(0)
    turtle.setx(-0.5)
    turtle.sety(-0.5)
    turtle.hideturtle()
    i = 0
    while i<len(grid):
        j = 0
        while j<len(grid):
            if grid[j][i] ==0:
                drawSquare(i,j)
            j = j+1
        i = i+1
    
def drawSquare(x,y):
    turtle.penup()
    turtle.setx(x-0.5)
    turtle.sety(y-0.5)
    turtle.pencolor("#000000")
    turtle.fillcolor("#000000")
    turtle.begin_fill()
    turtle.forward(1)
    turtle.left(90)
    turtle.forward(1)
    turtle.left(90)
    turtle.forward(1)
    turtle.left(90)
    turtle.forward(1)
    turtle.left(90)
    turtle.end_fill()

    
          
    