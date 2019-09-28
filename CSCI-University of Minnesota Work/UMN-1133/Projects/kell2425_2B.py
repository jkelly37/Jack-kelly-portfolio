#  CSci 1133 HW 2
#  Jack Kelly
#  HW Problem 2B

def get_r(b1, s1, z1):
        return b1*s1*z1
# funtion get_r takes values b1 s1 and z1  as floats and returns the product which is r as a float
#start program 

done = False
while not done:
    B = float(input('Enter the % likelihood of transmission (1 <= percentB <= 100): '))/100;
    pop = float(input('Enter the total population: (451 <= N <= 1384688986): '));
    S = float(input("Enter the % of population that is susceptible to infection (10 <= percentS <= 90): "))/100;
    Z = float(input("Enter the % of population that spontaneously turns into zombies (.25 <= percentZ <= 2): "))/100;
    if B > 1 or B<0.01 or S < 0.1 or S > .9 or pop < 451 or pop > 1384688986 or Z < 0.0025 or Z > 0.02:
        print("you entered an illegal input value")
    else: 
    
        print("b is:", B)
        print("s is:", S*pop)
        print("z is: ", pop*Z)
        print("The rate of zombie transmission is:", get_r(B, S*pop, pop*Z))
    goAgain = input("Continue?(Enter 'y' or 'Y'): ")
    if not ((goAgain == 'Y') or (goAgain == 'y')):
        done = True
        print("exiting program...")
