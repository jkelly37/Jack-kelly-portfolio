def main():
    
    intstring = input("enter list of integers with spaces inbetween:").replace(" ","")
    intList = [0] * len(intstring)
    p = 0
    while p<len(intstring):
        intList[p] = int(intstring[p])
        p = p+1
    for i in range(len(intstring)):
        min = i
        for j in range(i+1, len(intList)):
            if int(intList[min])>int(intList[j]):
                min = j
                #intList[i] = min
                intList[i], intList[min] = intList[min], intList[i]
    
    print(intList)
                
    

        
    


    
        
    

              
if __name__ == '__main__':
    main()