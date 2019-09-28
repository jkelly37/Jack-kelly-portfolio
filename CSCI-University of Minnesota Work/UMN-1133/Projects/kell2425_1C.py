#  CSci 1133 HW 1
#  Jack Kelly
#  HW Problem 1C
def RuleOf72(rate):
    #defines function 'RuleOf72'
    time = 72.00/rate
    return time 
    
#Start of program
print('Welcome to the Program of Rule Of 72!')
#prints welcome statement
print();
#creates blank line
r = float(input('Enter the interest rate: '));
#creates variable r(Interest rate) from user input
print();
print("Your investment will require","{:.2f}".format(RuleOf72(r)), "years to double:" )
#call to function 'RuleOf72' passing the variable r that was previously captured