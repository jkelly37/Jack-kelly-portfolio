#  CSci 1133 HW 1
#  Jack Kelly
#  HW Problem 1B

print('Welcome to the Program to compute compound interest on an investment!')
print();
#creates blank lines
p = float(input('Enter the initial investment amount: '));
r = float(input('Enter the interest rate: '))/100;
n = float(input('Enter number of times per year interst is compounded: '));
t = float(input('Length of time the money will be invested (in years): '));
#captures 4 variables from user input necessary to compute compound intrest and casts them as floats
print();
print('Interest earned is: ', "{:.2f}".format(p*((1+(r/n))**(n*t))-p));
#calculates and prints interest earned and rounds to two decimal places