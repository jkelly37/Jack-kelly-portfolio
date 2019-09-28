#  CSci 1133 HW 5
#  Jack Kelly
#  HW Problem 5D
#funtion doubleStringList is passed one parameter of type list and returns the list but with every letter in each element duplicated
def doubleStringList(sList):
    if type(sList)== list and len(sList)!=0: 
        return [doubleLetterInString(sList[0])] + doubleStringList(sList[1:])
    
    else:
        return []
#funtion 'doubleLetterInString' accepts one paramater 'L' which is a word and duplicates every letter in it and returns the word
def doubleLetterInString(L):
    if len(L)==0:
        return ""
    if len(L) == 1:
        return L+L
    if len(L)>1:
        return L[0]+L[0] + doubleLetterInString(L[1:])

    
    
    
    
