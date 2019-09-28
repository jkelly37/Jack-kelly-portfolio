import turtle

def drawSquare(size):
    print("drawstart")
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
def main():
    turtle.speed(9)
    turtle.setworldcoordinates(-400,-400,400,400)
    squareSize = 100
    width = 400
    height = 400
    
    print(turtle.window_width())
    turtle.penup()
    turtle.setx(-width)
    turtle.sety(height)
    j = 1
    while j<=8:
        i=1
        print("loop start")
        while i<=8:
            print("test")
            if (i+j)%2 == 0:
                turtle.fillcolor("#000000")
            else:
                turtle.fillcolor("red")
            i = i +1    
            #turtle.fillcolor(1,0,0)
            turtle.penup()
            turtle.begin_fill()
            #turtle.goto(-width + squareSize,height - squaresize)
            #turtle.goto(-width,0)
            #turtle.left(90)
            drawSquare(squareSize)
            turtle.end_fill()
        turtle.sety(turtle.ycor()-squareSize)
        turtle.setx(-400) 
        j = j+1
    sum = 0
    a = 2
    while 7>=1:
        sum = sum + a
    
    
    
    
    
    
if __name__ == '__main__':
    main()    
    

    
          
    