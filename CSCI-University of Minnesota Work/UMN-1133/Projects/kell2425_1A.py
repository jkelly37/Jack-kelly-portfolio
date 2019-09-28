#  CSci 1133 HW 1
#  Jack Kelly
#  HW Problem 1A

print("Welcome to the Simple Interest Calculator!");
#prints welcome statement
print()
#creates blank line
principal = float(input('Enter the loan amount: '));
interest = float(input('Enter the interest rate: '));
time = float(input('Enter the time to repay loan (in years): ')) / 100 ;
#captures three variables from user input and casts them as floats
print();
print("Interest is: ", "{:.2f}".format(principal*interest*time))
#uses the variables captured to calculate and print the total interest