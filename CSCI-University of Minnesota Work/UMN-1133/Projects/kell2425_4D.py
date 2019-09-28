
#  CSci 1133 HW 4
#  Jack Kelly
#  HW Problem 4D
#Funtion 'getInput' prompts the user for a sentence and checks to make sure there is more then one word then returns the sentence
def getInput():
    isSent = False
    while isSent== False:
        sent = input("Enter a sentence(hit return when you are done): ")
        if ' ' in sent:
            if sent.strip()!= "":
                isSent = True
                return sent
            else: print("error please enter more then one word")
        else:
            print("error please enter more then one word")
#function 'sentenceAsCharacterList' takes in a parameter of a sentence and returns it as a list of characters        
def sentenceAsCharacterList(sentence):
    sentence = sentence.replace(" ","")
    wordlist = list(sentence)
    #print(wordlist)
    return wordlist
#function 'sentenceAsList' takes one parameter of a sentence(string) and returns a list of words in the sentence
def sentenceAsList(sentence):
    wordList = sentence.split()
    
    return wordList

#funtion 'lowerCaseList' gets passed a list and it makes all the values lowercase and returns the list
def lowerCaseList(sentenceList):
    i =0
    
    while i< len(sentenceList):
        sentenceList[i] = sentenceList[i].lower()
        i = i+1
    return sentenceList
#function 'wordcount' is passed a list of words. the funtion then prints how often each word appears in the sentence
def wordCount(sentenceList):

    i = 0
    words = [] 
    while i< len(sentenceList):
        if sentenceList[i] not in words:
            #print("word added:", sentenceList[i])
            words.append(sentenceList[i])
        i = i+1
    words = sorted(words)   
    for w in words:
        count = 0 
        for c in range(0,len(sentenceList)):
            if sentenceList[c] == w:
                count = count+1
        print("the word: ", w, "occurs", count, "time(s)")
#funtion 'letterCount' is passed a list of letters and prints how often each letter appears in the sentence        
def letterCount(letterList1):
    
    i = 0
    letters = [] 
    while i< len(letterList1):
        if letterList1[i] not in letters:
            #print("word added:", sentenceList[i])
            letters.append(letterList1[i])
        i = i+1
    letters = sorted(letters)   
    for l in letters:
        count = 0 
        for c in range(0,len(letterList1)):
            if letterList1[c] == l:
                count = count+1
        print("the letter: ", l, "occurs", count, "time(s)")

def main():
    run = True
    while run == True:
        sentence1 = getInput()
        sentence1List = sentenceAsList(sentence1)
        sentence1ListLower = lowerCaseList(sentence1List)
        sentence1LetterList = sentenceAsCharacterList(sentence1)
        sentence1LetterListLower = lowerCaseList(sentence1LetterList)
        print("the sentence you entered is:")
        print(sentence1)
        print()
        print("The list of words in the sentence is:")
        print(sentenceAsList(sentence1))
        print()
        print("The lowercase list of words in the sentence is: ")
        print(sentence1ListLower)
        print()
        print("The sorted list of (lowercase) words in the sentence is: ")
        print(sorted(sentence1ListLower))
        print()
        print("Word usage in the sentence is as follows:")
        
        wordCount(sentence1List)
        print()
        print("Letter usage in the sentence is as follows:")
        print("in the sentence: ", sentence1)
        
        letterCount(sentence1LetterListLower)
        print()
        cont = input("Would you like to process another sentence? (Enter 'y' or 'Y'):")
        if cont != "y" and "Y":
            run = False
        
           
if __name__ == '__main__':
    main()

        
    