#  CSci 1133 HW 3
#  Jack Kelly
#  HW Problem 3B

# funtion processMove takes value 'move' which is a string that indicates dirrection and then determines how much farther that made the player from the exit

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

    
# the funtion 'main' runs a loop asking the user for moves and then calls the funtion 'processMove' to see how the move affectd the players distance from the exit. the loop runs until the variable 'toExit' = 0
def main():
    done = False
    toExit = 3
    while done!=True:
         print("you are", toExit, "squares away from the exit")
         if toExit == 0:
            done = True
            print("You escaped the forest!")
         else:    
            direction = input("You are lost in the woods. Enter N/S/E/W: ")
            toExit = toExit + (processMove(direction))


            
if __name__ == '__main__':
    main()
    