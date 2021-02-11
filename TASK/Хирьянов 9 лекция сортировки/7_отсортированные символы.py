A = input().split('.')[0]
B = []
for i in range(len(A)):
    x = ord(A[i])
    B.append(x)
B.sort()
C= []
for i in range(len(B)):
    x = chr(B[i])
    C.append(x)
C.append('.')
print(*C, sep='')


