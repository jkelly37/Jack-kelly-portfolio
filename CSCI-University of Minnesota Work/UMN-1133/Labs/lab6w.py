def shortestDist(list):
    shortestLeng = 12345654
    i = 0
    while i< len(list):
        x1 = list[i][0]
        y1 = list[i][1]
        j=0
        while j< len(list):
            x2 = list[j][0]
            y2 = list[j][1]
            if i!= j:
                dist = (((x1-x2)**2)+((y1-y2)**2))**0.5
                if dist< shortestLeng:
                    shortestLeng = dist
            j = j+1
        i = i+1
    return shortestLeng
    
l1 = [[45,-99],[24,83],[-48,-68],[-97,99],
[-8,-77],[-2,50],[44,41],[-48,-58],
[-1,53],[14,86],[31,94],[12,-91],
[33,50],[82,72],[83,-90],[10,78],
[7,-22],[90,-88],[-21,5],[6,23]]

def main():
    short = shortestDist(l1)
    print(short)
if __name__ == '__main__':
    main() 

    
    
    
             
        elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), leftAngle):
            print("elif")
            turtle.left(90)
            turtle.forward(1)
            
            
            
            
            
            
                    if moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), 270):
            turtle.right(turtle.heading())
            turtle.left(270)
            
            turtle.forward(1)
            
            print("turtle moved forward one space")
            #try left
   
            #try forward
        #turtle.left(90)
        
        elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), 0):
            turtle.right(turtle.heading())
            turtle.forward(1)
        elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), 90):
            turtle.right(turtle.heading())
            turtle.left(90)
            turtle.forward(1)
        elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), 180):
            turtle.right(turtle.heading())
            turtle.left(180)
            turtle.forward(1
                           
                           
                           
                           
                           
                           
                           
                           
#  CSci 1133 HW 4
#  Jack Kelly
#  HW Problem 4C
import turtle
turtle.setworldcoordinates(-1, -1, 10, 10)
dgrid = [[0,0,0,0,0,0,0,0,0,0],
     [0,1,1,1,1,0,1,1,1,0],
     [0,1,0,0,0,0,1,0,1,0],
     [0,1,1,1,1,1,1,1,1,0],
     [0,1,0,0,0,0,1,0,0,0],
     [0,1,1,1,1,1,1,1,1,0],
     [0,0,1,0,0,0,1,0,1,0],
     [0,0,1,0,0,0,0,0,0,0],
     [0,1,1,1,1,1,1,1,1,0],
     [0,0,0,0,0,0,0,0,0,0]]
#func move valid recives param. grid(list of lists), an x and y postion and a dirrection. using these it determines if the move would be valid if so it returns true if not it returns false
def moveValid(grid, xpos, ypos, direction):
    #print(direction)
    #print("recived XPos:", xpos)
    #print(" recived yPos:", ypos)
    #print("recived dir", direction)
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
    #else:
        #print("error: invalid direction")
        #return False
    
    import turtle
turtle.setworldcoordinates(-1, -1, 10, 10)
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

    
def drawSquare(x,y):
    turtle.penup()
    turtle.setx(x-0.5)
    turtle.sety(y-0.5)
    #turtle.pendown
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
def main():
    x = 1
    y = 1
    drawGrid(dgrid)
    turtle.setx(1)
    turtle.sety(1)
    turtle.pendown()
    #turtle.settiltangle((turtle.tiltangle()+90))
    
    

    
    while int(round(turtle.xcor()))!=8 or int(round(turtle.ycor()))!=8:
        print( turtle.xcor(), turtle.ycor())
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
        print("right", right, "left", left, "back", back, "forward", forward)
        if moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), right):
            turtle.setheading(right)
            turtle.forward(1)
            print("turtle right")
        elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), forward):
            turtle.setheading(forward)
            turtle.forward(1)
            print("turtle up")
        elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), left):
            turtle.setheading(left)
            
        elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), back):
            turtle.setheading(back)
            turtle.forward(1)
            print("turtle left")

            
            
            
    
            print("turtle down")
 
        #leftAng = currentAng + 180

        #try right
        #print("angle",turtle.heading(), "x:", int(turtle.xcor()),"y(rounded):", int(round(turtle.ycor())), "result:", moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), turtle.heading()))
        #try right
        #if moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), 0):
         #   turtle.right(turtle.heading())
            #turtle.forward(1)
            #print("turtle right")
        #elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), 90):
            #turtle.right(turtle.heading())
            #turtle.left(90)
            #turtle.forward(1)
            #print("turtle up")
        #elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), 180):
            #turtle.right(turtle.heading())
            #turtle.left(180)
            #turtle.forward(1)
            #print("turtle left")
        #elif moveValid(dgrid,int(round(turtle.xcor())),int(round(turtle.ycor())), 270):
         #   turtle.right(turtle.heading())
            #turtle.left(270)
            
            #turtle.forward(1)
            
            #print("turtle down")
            #try left
   
            #try forward
        #turtle.left(90)
        



        #else: 
            #turtle.right(180)
        #try forward
        #elif moveValid(dgrid,round(int(turtle.xcor())),round(int(turtle.ycor())), turtle.heading()) == True:
            #print("forward ran")
            #turtle.left(turtle.heading())
            #turtle.forward(1)
        #try right
        #elif moveValid(dgrid,round(int(turtle.xcor())),round(int(turtle.ycor())), turtle.heading()-180) == True:
            #print("left ran")
            #turtle.left(180)
            #turtle.forward(1)
        
            
        #if moveValid(dgrid,round(int(turtle.xcor())),round(int(turtle.ycor())), round(int(turtle.heading()))) == False:
            #print("bish im false, turning 90 deg")
            
            #turtle.right(90)
            #print(turtle.heading(), "is tilt angle")
           

if __name__ == '__main__':
    main()   
          
                               