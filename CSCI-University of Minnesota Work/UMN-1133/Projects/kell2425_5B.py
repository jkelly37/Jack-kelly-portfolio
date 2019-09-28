#  CSci 1133 HW 5
#  Jack Kelly
#  HW Problem 5B
#function 'FibAny' takes one paramter number and returns the fib number of that int 
def FibAny(num):
    if num== 0:
        return 0
    if num==1:
        return 1
    elif num>0:
        return(FibAny(num-1) + FibAny(num-2))
    elif num<0:
        return(((-1)**((-num)+1))*FibAny(-num))
    