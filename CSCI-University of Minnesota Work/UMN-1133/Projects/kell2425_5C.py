#  CSci 1133 HW 5
#  Jack Kelly
#  HW Problem 5C
import copy 
#function 'SameStuff' recives two lists and returns true if they share any of the same values and have the same length. if they dont share vaules or have diffenent lengths it returns false  
def SameStuff(l1,l2):
    list1 = copy.copy(l1)
    list2 = copy.copy(l2)
    if len(list1) == 0 and len(list2) == 0:
        return True
    elif len(list1) == len(list2):
        if list1[0] in list2:
            i = list2.index(list1[0])
            del list2[i]
            del list1[0]
            return SameStuff(list1,list2)
        else:
            return False
    elif len(list1) != len(list2):
        return False

    