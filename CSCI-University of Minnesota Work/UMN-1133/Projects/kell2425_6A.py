
def main():
    go = True
    while go != False:
        location = input("Enter name of input file: ").replace(" ", "")
        handle = open(location, encoding = 'utf-8', errors = 'ignore')

        data = sortByVal(handle)

        save = input("Write list to output file:(enter 'Y' or 'y')?").lower()
        if save == 'y':
            name = input("Enter name of output file:") + ".txt"
            saveData(data,name)
        cont = input("Continue: (enter 'Y' or 'y')?").lower()
        if cont != 'y':
            go = False
def saveData(data, filename):
    newfile = open(filename, 'w')
    head1 = '\t' + 'Year' + '\t' + 'Name' + '\t' + 'Country' + '\t' + '\t' + 'Language' + '\n'
    datastr = ""
    for lines in data:
        datastr = datastr + str(lines) + '\n'
    newfile.write(head1 + datastr)
    newfile.close()

def sortByVal(hand):
    valid = False
    extra = hand.readline()
    unit = hand.read().rstrip().split("\n")
    hand.close()
    twoD = []
    for i in range(0, len(unit)):
        twoD.append(unit[i].split(","))
        twoD[i][0] = int(twoD[i][0])
        twoD[i][1] = twoD[i][1].split(" ")
    while valid!= True:

        print("Enter direction on how to sort and display data: ")
        val = input("((y)ear, (f)irst, (l)ast, (c)ountry, (s)poken language(s)): ")



        if val == "y":
            valid = True
            twoD.sort(key = yearKeyFunction)
        elif val == 'f':
            valid = True
            twoD.sort(key = firstKeyFunction)
        elif val == "l":
            valid = True
            twoD.sort(key = lastKeyFunction)
        elif val == 'c':
            valid = True
            twoD.sort(key = countryKeyFunction)
        elif val == 's':
            valid = True
            twoD.sort(key=languageKeyFunction)
        else:
            print("ERROR: Choice: ", val, "not recognized")
            print("")
    print('\t' + 'Year' + '\t' + 'Name' + '\t' + 'Country' + '\t' + '\t' + 'Language' + '\n')
    for e in twoD:
        print(e)
    return twoD

def yearKeyFunction(listElement):
    return listElement[0]
def firstKeyFunction(listElement):
    return listElement[1][0]
def lastKeyFunction(listElement):
    return listElement[1][1]
def countryKeyFunction(listElement):
    return listElement[2]
def languageKeyFunction(listElement):
    if type(listElement[3]) == list:
        return listElement[3][0]
    else:
        return listElement[3]



if __name__ == "__main__":
    main()
