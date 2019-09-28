#this script reads in text files and records what words occur in which files and writes them to a new file
filesList = ['doc1.txt','doc2.txt', 'doc3.txt', 'doc4.txt']
space = ' '
word_delimiters = (space, ',', ';', ':', '.', '"',"'", '(',
     ')','?','!')
dic = {}
for i in range(len(filesList)):
    handle = open(filesList[i], 'r', encoding = 'UTF-8')
    num = handle.readline().replace('\n','')
    filetxt = handle.read().replace('\n','').lower()
    handle.close()
    for ch in word_delimiters:
        filetxt = filetxt.replace(ch, " ")
    l1 = filetxt.split(" ")

    for elm in l1:
        if elm != '' and elm!= " " and elm != '':
            if elm in dic:
                if num not in dic[elm]:
                    val = dic[elm]
                    val.append(num)
                    dic[elm]: val
            else:
                dic[elm] = [num]
handle2 = open('kell2425.txt', 'w')
string = ''
keylist = dic.keys()
for keys in sorted(keylist):
    temp = " "
    for k in dic[keys]:
        string = string + keys + ' ' + str(k) + '\n'


handle2.writelines(string)
handle2.close()
