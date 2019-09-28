#  CSci 1133 HW 3
#  Jack Kelly
#  HW Problem 3c
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
 
 #function 'escape' takes one artument 'moveList' which is a list of strings that indicates the dirrection of a move. the function contains a loop that calls the funtion 'process loop' in order to return a boolean value of weather the player escaped
def escape(ls = []):
    escapeDist = 3
    didEscape = False
    i = 0
    for i in range(0,(len(ls))):
        escapeDist = escapeDist + processMove(ls[i])
        i = i+1
        if escapeDist<= 0:
            didEscape = True
            return didEscape
       
    if didEscape == False:
        return False
    else: 
        return True
    
        