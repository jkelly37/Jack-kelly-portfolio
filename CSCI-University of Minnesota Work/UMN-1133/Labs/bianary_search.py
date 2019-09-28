A1 = [2,435,5,36,24,4,70,3,82,44,5,667,86,53,23,44,3,2,3,45,654,]
def bianary(A,v):
    found = False
    A.sort()
    print("A sorted:",  A)
    quad = len(A)//2
    if v > A[quad]:
        bianary(A[quad+1:],v)
    
    if v < A[quad]:
        bianary(A[:(quad-1)], v)
    if v == A[quad]:
        print("sol found", A[quad])
bianary(A1, 44)