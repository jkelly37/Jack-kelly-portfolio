print("welcom to odd number sum")
num = int(input("please enter a number n:"))
i =0
sum = 0
for i in range(0,num):
    print("i:",i)
    if i%2 == 0:
        print("even")
    else:
        sum = sum + i
    i = i+1
    print(sum)
        
        
