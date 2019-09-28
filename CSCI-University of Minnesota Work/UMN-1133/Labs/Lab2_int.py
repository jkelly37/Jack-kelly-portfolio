full = float(input('Enter a 4 digit integer'));
di1 = full//1000
di2 = (full - (di1*1000))//100
di3 = ((full - (di1*1000)) - ((di2*100)//10))
print(di1)
print(di2)
print(di3)