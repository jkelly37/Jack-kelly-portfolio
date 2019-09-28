#funtion 'getInput' recives and validates input from user and returns a string of the input
def getInput():
    valid = False
    while valid == False:
        text = input("Enter a telephone number: ").lower()
        for ch in ' .#-()':
            text = text.replace(ch, '')
        if len(text) == 7 or len(text) == 10:
            return text

        elif len(text) > 0:
            print("Error: Invalid number")
            print()
        else:
            valid = True
            return ""




def main():
    isNull = False
    while isNull == False:
        num = getInput()
        if num !='':
            print("Numeric telephone number is:", convertNum(num))
            print()
        else:
            isNull = True

#function 'convertNum recives string 'num' as a string and converts it to a properly formated number and returns it as a string
def convertNum(num):
    digits = '1234567890'
    alpha = {'abc': 2, 'def': 3, 'ghi': 4, 'jkl': 5, 'mno': 6, 'pqrs': 7, 'tuv': 8, 'wxyz': 9}
    numAsStr = ""
    for i in num:
        if i in digits:

            numAsStr = numAsStr + str(i)
        else:
            for keys in alpha:
                for l in keys:
                    if i == l:

                        numAsStr = numAsStr + str(alpha[keys])

    if len(numAsStr) == 10:
        numAsStr = numAsStr[:3] + "-" + numAsStr[3:6] + "-" + numAsStr[6:]

    if len(numAsStr) == 7:
        numAsStr = numAsStr[:3] + "-" + numAsStr[3:]
    return numAsStr

if __name__ == '__main__':
    main()



    
    """http://127.0.0.1:8231?accountId=accountIS68UIRQ9G"""
    '''http://localhost:8231?accountId=accountBVGNR0W4TM'''