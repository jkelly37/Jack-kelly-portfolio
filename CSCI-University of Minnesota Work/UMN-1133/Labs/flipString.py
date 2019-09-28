def reverseString(n):
    if len(n)== 0:
        return n
    else:
        return(reverseString(n[1:]) + n[0])
print(reverseString("hey"))