def maxValue(nList):
    if nlist == sorted(nlist, Reverse == True):
        return nList
    else
        nli
        
        
        
        def deepSquare(list1):
    global Glist
    print("deepSquare called with list" ,list1)
    
    if type(list1) == int:
        print("if ran", list1)
        e = list1**2
        return e 
        
    if type(list1) == list:
        i = 0
        while i < len(list1):
            print("list is actaully a list")
            temp  = list1[0]
            del list1[0]
            
            Glist.append(deepSquare(temp))
    
            


        
    
    

        
print(deepSquare([[-1,[2],[3],[[[-4,5]]],[],[]]]))
print(Glist)
def SameStuff(l1,l2):
    
    list1 = copy.copy(l1)
    print(len(l1), len(l2))
    print("this l1",l1)
    if len(list1) == 1:
        if list1[0] in l2:
            return True
    if len(list1) > 1: 
        return SameStuff(list1[1:],l2)