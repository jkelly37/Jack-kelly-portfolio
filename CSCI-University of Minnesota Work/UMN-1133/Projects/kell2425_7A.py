#funtion 'addDicts' accepts 2 dictionarys and adds the elements together and returns the sum of the 2 dictionaries as a new dictionary
def addDicts(d1,d2):
    dsum = {}
    for key in d1:
        if key in d2:
            newVal = d1[key] + d2[key]
            dsum[key] = newVal
        else:
            dsum[key] = d1[key]
    for key2 in d2:
        if key2 not in dsum:
            dsum[key2] = d2[key2]
    return dsum