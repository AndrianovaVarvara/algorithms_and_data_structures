def stack(A):
    s = []
    for i in range (len(A)):
        s.append(A[i])
    while len(s) > 0:
        x = s.pop()
        print(x)


A = [1,2,3,4,5,6,7,8,9,10]
stack(A)