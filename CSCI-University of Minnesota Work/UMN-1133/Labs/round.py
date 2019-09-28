def roundit(num):
    if num>= 0:
        num=num+0.5
        num//num
    else:
        num=num-0.5
    return(int(num))
num1 = float(input('Enter a number '));
print(roundit(num1))
    