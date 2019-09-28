#  CSci 1133 HW 4
#  Jack Kelly
#  HW Problem 4C
import turtle
turtle.setworldcoordinates(-1, -1, 10, 10)

#func move valid recives param. grid(list of lists), an x and y postion and a dirrection. using these it determines if the move would be valid if so it returns true if not it returns false
def moveValid(grid, xpos, ypos, direction):
    if direction == 90:
        if grid[ypos+1][xpos]== 0:
            return False
        else:
            return True
        
    elif direction == 180:
        if grid[ypos][xpos-1]== 0:
            return False
        else:
            return True
    elif direction == 0:
        if grid[ypos][xpos+1]== 0:
            return False
        else:
            return True
    elif direction == 270:
        if grid[ypos-1][xpos]== 0:
            return False
        else:
            return True
    else:
        print("error: invalid direction")
        return False
    

#function drawGrid recives one param of a list of lists. the function then parses through the values in the nested lists and draws a black square to its respected location in the turtle window if the value is equal to 0  
def drawGrid(grid):
    turtle.delay(0)
    turtle.speed(0)

    turtle.showturtle()
    i = 0
    while i<len(grid):
        j = 0
        while j<len(grid):
            if grid[j][i] ==0:
                drawSquare(i,j)
            j = j+1
        i = i+1

#funtion 'drawSquare' takes 2 parameters x and y which are the center coordinates of the square and it draws a square around it     
def drawSquare(x,y):
    turtle.penup()
    turtle.setx(x-0.5)
    turtle.sety(y-0.5)
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
#function 'rightWall' receives a 2d list and navagates a turtle object to the pt(8,8)
def rightWall(grid):

    drawGrid(grid)
    turtle.setx(1)
    turtle.sety(1)
    turtle.pencolor("blue")
    turtle.pendown()
    while int(round(turtle.xcor()))!=8 or int(round(turtle.ycor()))!=8:
        angle = turtle.heading()
        right = angle-90
        left = angle+90
        back = angle+180
        forward = angle
        if back == 360:
            back = 0
        if back == 450:
            back = 90
        if left ==360:
            left = 0
        if right == -90:
            right = 270
        
        if moveValid(grid,int(round(turtle.xcor())),int(round(turtle.ycor())), right):
            turtle.setheading(right)
            turtle.forward(1)
            
        elif moveValid(grid,int(round(turtle.xcor())),int(round(turtle.ycor())), forward):
            turtle.setheading(forward)
            turtle.forward(1)
            
        elif moveValid(grid,int(round(turtle.xcor())),int(round(turtle.ycor())), left):
            turtle.setheading(left)
            
        elif moveValid(grid,int(round(turtle.xcor())),int(round(turtle.ycor())), back):
            turtle.setheading(back)
            turtle.forward(1)

          
    