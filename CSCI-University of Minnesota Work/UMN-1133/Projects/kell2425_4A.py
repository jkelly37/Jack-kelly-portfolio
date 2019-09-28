#  CSci 1133 HW 4
#  Jack Kelly
#  HW Problem 4A

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
    
    