import turtle
import random
turtle.speed(100000000000)
def addPoint():
    dotsIn = 0    
    i=0
    darts = 100
    while i<darts:
        turtle.penup()
        ptX = random.randint(-150,150)
        ptY = random.randint(-150,150)

        i = i+1
        
        if (ptX**2 + ptY**2)**0.5<150:
            turtle.sety(ptY)
            turtle.setx(ptX)
            turtle.dot(5, "green")
        else:
            turtle.sety(ptY)
            turtle.setx(ptX)
            turtle.dot(5, "red")
            dotsIn= dotsIn+1
    pi = 4*(dotsIn/darts) 
    print("the estimate of pi is ", pi)
        
        
            
    
def drawCircle():
    turtle.penup()
    turtle.sety(-150)
    turtle.pendown()
    turtle.circle(150)
    
    
def drawSquare():
    print("draw")
    turtle.penup()
    turtle.setx(-150)
    turtle.sety(-150)
    turtle.pendown()
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.left(30)
    
        
    
def main():
    print("main ran")
    drawCircle()
    addPoint()
    drawSquare()
    
    

    
if __name__ == '__main__':
        main()
    