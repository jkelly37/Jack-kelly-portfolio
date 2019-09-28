import turtle
import random
def move():
    print("moveXtimes called")
    i=0
    x = (random.randint(20,40))
    stepsCounter = 0
    while i<x:
        steps = random.randint(15,25)
        turtle.forward(steps)
        turtle.right(turn())
        i=i+1
        stepsCounter = stepsCounter + steps
    turtle.penup()    
    turtle.setx(0)
    turtle.sety(300)
    turtle.write( ("total steps taken: ",stepsCounter), True, align="center",font=("Arial", 25, "normal"))
    
    
def turn():
    num = random.randint(1,5)
    print(num)
    if num==1:
        return 90
    if num==2:
        return 0
    if num==3:
        return 180
    if num==4:
        return 270
    if num==5:
        return 360
    
    
    
def main():
    print("main ran")
    turtle.left(90)
   
    move()
    

    
if __name__ == '__main__':
         main()