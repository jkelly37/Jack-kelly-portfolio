#  CSci 1133 HW 2
#  Jack Kelly
#  HW Problem 2C
import turtle

def drawTriangle(side, color):
        turtle.pencolor(color)
        turtle.pendown()
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(120)    
        turtle.penup()
#function 'drawTriangle' accepts 2 arguments, color and side. color is used to set the color of the pen. and size determines the size of the triangle
    
    
def drawRectanglePattern(side1):
    turtle.hideturtle()
    clr = "#e82020"
    
    turtle.penup()
    turtle.setx(200)
    turtle.sety(-150)
    drawTriangle(side1, clr)
    turtle.penup()
    turtle.sety(250)
    #turtle.left(90)
    drawTriangle(side1, clr)
    turtle.penup()
    turtle.setx(-200-side1)
    #turtle.right(180)
    drawTriangle(side1, clr)
    turtle.penup()
    turtle.setx(-200-side1)
    turtle.sety(-150)
    
    drawTriangle(side1, clr)
    
# function 'drawRectanglePattern'accepts one argument, side1 which is then passed to drawtriangle. this function traces a rectangle and at each corner draws a triangle    
    
def drawStarPattern(side2):
    turtle.hideturtle()
    clr = "#1656bc"
    turtle.penup()
    turtle.setx(50)
    turtle.sety(-100)
    turtle.pendown()
    drawTriangle(side2, clr)
    
    turtle.sety(50)
    turtle.setx(125)
    drawTriangle(side2,clr)
    
    turtle.setx(-side2/2)
    turtle.sety(150)
    drawTriangle(side2, clr)
    turtle.right(180)
    turtle.setx(-(125+side2))
    turtle.sety(50)
    turtle.right(180)
    drawTriangle(side2, clr)

    turtle.setx(-(50+side2))
    turtle.sety(-100)
    drawTriangle(side2, clr)
    turtle.hideturtle()
    turtle.setx(0)
    turtle.sety(0)
# function 'drawTrianglePattern'accepts one argument, side2 which is then passed to drawtriangle. this function traces a star and calls function 'drawTriangle' to draw triangles at each vertices

#program start

sideLength = float(input("Enter length of side: "))
if sideLength>50 or sideLength<25:
    print("Error: ", sideLength,"is less than 25 or greater than 50, using default value of 25")
    sideLength = 25
shape = input("Enter drawing pattern: r or R for rectangle, s or S for star, b or B for both: ")

if shape == "r" or shape == "R":
    drawRectanglePattern(sideLength)
elif shape == "s" or shape == "S":
    drawStarPattern(sideLength) 
elif shape == "b" or shape == "B":
    drawStarPattern(sideLength)
    drawRectanglePattern(sideLength)
else:
    print("Error: pattern: ", shape, "not recognized!")
        
#these if statments determine what functions to call        

    

