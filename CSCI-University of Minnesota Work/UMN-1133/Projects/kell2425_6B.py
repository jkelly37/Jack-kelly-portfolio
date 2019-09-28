def main():
    
    cont = True
    while cont == True:
        valid = False
        while valid != True:
            choice = input("Enter Encrypt or Decrypt (Enter e or d): ")
            if choice.lower() == 'e':
                valid = True
                valid1 = False
                shift = 0
                while valid1 == False:
                    shift = int(input("Enter a shift number n, where 1 <= n <= 13:"))

                    if shift > 0 and shift <= 13:
                        valid1 = True

                    else:
                        print("Invalid number: ", shift, "Try again")

                fileIn = input("Enter input file name: ")
                fileOut = input("Enter output file name:")
                infile = open(fileIn, 'r')
                inFileText = infile.read().lower()
                infile.close()
                contents = encrypt(inFileText, shift)
                newFile = open(fileOut, 'w')
                data = str(shift) + contents
                newFile.write(data)
                newFile.close()
            elif choice.lower() == 'd':
                valid = True
                fileIn = input("Enter input file name: ")

                infile = open(fileIn, 'r')
                shift = infile.readline()
                inFileText = infile.read().lower()
                infile.close()
                contents = decrypt(inFileText, shift)
                print("Decrypted Contents of the file: ", fileIn,":")
                print(contents)


            else:
                print("Invalid choice:", choice, "try again")
            
        go = input("Continue: (Enter Y or y)):").lower()
        if go !='y':
            cont = False
        else:
            print()


def encrypt(astr, shiftNum):
    lineSplit = astr.split("\n")
    for i in range(len(lineSplit)):
        lineSplit[i] = lineSplit[i].split(" ")
    
    shiftDict = getShiftDicte(shiftNum)
    para = ''
    sentence = ""
    for lines in lineSplit:
        newSentence = ''
        for words in lines:
            newSentence = newSentence + doShiftForWord(shiftDict, words) + " "
        para = para +'\n' + newSentence.rstrip() 
    
    return para

    print(para)
def decrypt(astr, shiftNum):
    lineSplit = astr.split("\n")
    for i in range(len(lineSplit)):
        lineSplit[i] = lineSplit[i].split(" ")
    
    shiftDict = getShiftDictd(shiftNum)
    para = ""
    sentence = ""
    for lines in lineSplit:
        newSentence = ''
        for words in lines:
            newSentence = newSentence + doShiftForWord(shiftDict, words) + " "
        para = para + newSentence.rstrip() + '\n'
    

    
    return para.rstrip()



def getShiftDicte(shift):
    num_shift = {'1':1 ,'2':2, '3':3, '4':4, '5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'11':11,'12':12,'13':13,'14':14,'15':15,'16':16,'17':17,'18':18,'19':19,'20':20,'21':21,'22':22,'23':23,'24':24,'25':25,'26':26}
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for index in num_shift:
        num_shift[index] = int(num_shift[index]) + shift
        if num_shift[index] > 26:
            num_shift[index] = int(num_shift[index]) - 26

    return num_shift

def getShiftDictd(shift):
    num_shift = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 11,
                     '12': 12, '13': 13, '14': 14, '15': 15, '16': 16, '17': 17, '18': 18, '19': 19, '20': 20, '21': 21,
                     '22': 22, '23': 23, '24': 24, '25': 25, '26': 26}

    for index in num_shift:
        num_shift[index] = int(num_shift[index]) - int(shift)

        if num_shift[index] < 0:
            num_shift[index] = int(num_shift[index]) + 26


    return num_shift
def doShiftForWord(shift, word):
    newword = ""
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for ch in word:
        if ch in alpha:
            index1 = alpha.index(ch)+1

            newIndex = shift[str(index1)]
            letter = alpha[newIndex-1]
            newword = newword + letter
        else:
            newword = newword + str(ch)
    return newword

if __name__ == '__main__':
    main()