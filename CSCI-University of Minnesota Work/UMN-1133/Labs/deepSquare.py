Glist = []
def deepSquare(list1):
    print(list1)
    for i in range(len(list1)):
        if type(list1[i])== int:
            list1[i] = list1[i] **2
        else:
            deepSquare(list1[i])
    return list1
            


        
    
    

        

def flatDeepSquare(list1):
    if type(list1) == int:
        return list1**2
    else:
        if len(list1) ==0:
            return[]
        elif len(list1) == 1:
            return flatDeepSquare(list1[0])
        else:
            return flatDeepSquare(list1[0]) + flatDeepSquare(list1[1:])
        
def GDC(a,b):
    if b== 0:
        return a
    r = a%b
    return GDC(r,b)
    
    
    
    
    
flatDeepSquare([[-1,[2],[3],[[[-4,5]]],[],[]]])   
print(Glist)



