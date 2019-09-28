import random
i = 0 
diceList = [0,0,0,0,0,0,0,0,0,0,0,0,]
while i<10000:
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    sum = num1 + num2
    diceList[sum-2] = (diceList[sum-2]+1)
    i = i+1
print(diceList)