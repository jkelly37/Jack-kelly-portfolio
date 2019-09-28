
#  CSci 1133 HW 3
#  Jack Kelly
#  HW Problem 3D
import turtle
side = 50
#funtion 'drawTriangle' takes gets in one argument of type 'turtle' and draws a triangle
def drawTriangle(t2):
    global side
    t2.forward(side)
    t2.left(120)
    t2.forward(side)
    t2.left(120)
    t2.forward(side)
    t2.left(120)  
    
#funtion 'drawSquare' takes gets in one argument of type 'turtle' and draws a square    
def drawSquare(t2):
    global side
    t2.forward(side)
    t2.left(90)
    t2.forward(side)
    t2.left(90)
    t2.forward(side)
    t2.left(90)
    t2.forward(side)
    t2.left(90)
    
#funtion 'drawHex' takes gets in one argument of type 'turtle' and draws a hexagon    
def drawHex(t2):
    global side
    t2.forward(side)
    t2.left(60)
    t2.forward(side)
    t2.left(60)
    t2.forward(side)
    t2.left(60)
    t2.forward(side)
    t2.left(60)
    t2.forward(side)
    t2.left(60)
    t2.forward(side)
    t2.left(60)
#'triangleSequence' recives two values 'num' which is how many times the shape should be drawn and 't1' which is a turtle object

def triangleSequence(num,t1):
    turn = 360/num
    t1.pencolor("#0000FF")
    i = 0
    while i<num:
        drawTriangle(t1)
        t1.left(turn)
        i= i+1
    t1.hideturtle()
    
#'squareSequence' recives two values 'num' which is how many times the shape should be drawn and 't1' which is a turtle object
def squareSequence(num,t1):
    turn = 360/num
    t1.pencolor("#00FF00")
    i = 0
    while i<num:
        drawSquare(t1)
        t1.left(turn)
        i= i+1
    t1.hideturtle()
    
#'hexSequence' recives two values 'num' which is how many times the shape should be drawn and 't1' which is a turtle object       
def hexSequence(num,t1):
    turn = 360/num
    t1.pencolor("#FF0000")
    i = 0
    while i<num:
        drawHex(t1)
        t1.left(turn)
        i= i+1  
    t1.hideturtle()
    
# 'main' recives user imput for shapes to draw with and how many to draw and checks for error in input. then calls the respective procedures to draw the shape sequences   
def main():
    # extra credit funtions added in at line 102 to prevent turtle popup from blocking user input
    run = True
    while run== True:
        print("welcome to the program to draw shapes")
        shapeReal = False
        while shapeReal == False:
            shape = input("enter the shape used to draw the figure(Triangle, Square, hexagon): " ).lower()
            if shape=="triangle" or shape=="square" or shape=="hexagon":
                shapeReal = True
            else:
                print("Error: choice:", shape, "is not recognized, please enter a valid choice")
        NumIsPos = False
        while NumIsPos==False:
            number = int(input("Enter the number of shapes you would like to draw: "))
            if number<0:
                print("Error: number: ", number, "is not positive- please enter a positive number")
            else:
                NumIsPos=True
            
        world = turtle.Screen()    
        world.clear()
        t = turtle.Turtle()
        world.delay(0)
        t.speed(0)
        if shape=="triangle":    
            
            triangleSequence(number,t)
        if shape=="square":
            
            squareSequence(number,t)
        if shape=="hexagon":
            
            hexSequence(number,t)
         
        cont = input("Would you like to continue ('Y' or 'y'): ").lower()
        if cont!="y":
            run = False
                



    


    
    
    
    
if __name__ == '__main__':
    main()
    
    