#  Jack Kelly
# Lab 2

print('Welcome to the the windchill calculator!')
#prints welcome statement
print();
#creates blank line
wind = float(input('Enter the wind speed in miles/hour: '));
temp = float(input('Enter the temp in fahrenheit '));
if temp>=-58 and temp<41:
        ans = 35.74+(0.6215*temp)-(35.75*(wind**0.16))+(0.4275*temp*(wind**0.16))
        print(ans);
else:
    print("Invalid temp")
