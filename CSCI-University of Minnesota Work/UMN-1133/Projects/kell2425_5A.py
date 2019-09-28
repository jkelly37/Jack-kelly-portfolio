#  CSci 1133 HW 5
#  Jack Kelly
#  HW Problem 5A
import math
#function estimate accepts one paramater 'epsilon' and computes an apporximation until the error is less then epsilon and prints the terms, the estimation and how many terms were needed
def estimate(epsilon):
    approxfirst = ((12)**0.5)*(((-3)**0)/((1)))
    print("zeroth term: ", approxfirst)
    approxsecond = ((12)**0.5)*(((-3)**(-1))/((3)))
    print("first term", approxsecond+ approxfirst)
    sum1 = approxfirst + approxsecond
    k = 2 
    while math.fabs((sum1-math.pi)) > epsilon:
        
        approxsecond = ((12)**0.5)*(((-3)**(-k))/(((2*k)+1)))
        
        sum1 = sum1+approxsecond
        print("term ", k, "Value: ", sum1)
        k = k+1
        
    print(k-1, "terms used to PI value ", sum1, "with epsilon value: ", epsilon)

    