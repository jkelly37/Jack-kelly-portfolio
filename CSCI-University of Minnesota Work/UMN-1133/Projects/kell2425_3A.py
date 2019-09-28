#  CSci 1133 HW 3
#  Jack Kelly
#  HW Problem 3A
# funtion processMove takes value 'move' which is a string that indicates dirrection and then determines how much farther that made the player from the exit and returns that value
 
def processMove(move):
    if move != "S" and move != "N" and move != "E" and move!= "W":
        print("Invalid move")
        return 0
    elif move == "N":
        return -1
    elif move == "S":
        return 1
    elif move == "E" or "W":
        return 0
