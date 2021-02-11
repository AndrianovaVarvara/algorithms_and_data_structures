A = [['I', 1],['V', 5],['X', 10],['L',50],['C',100],['D', 500],['M', 1000]]
B = input()
C=[]
for i in range (len(B)):
    for j in range(len(A)):
        if B[i] == A[j][0]:
            C.append(A[j][1])

C = C + [0]

x=0
while len(C) >= 2:
    if C[0] < C[1]:
        x = x+(C[1]-C[0])
        C.pop(0)
        C.pop(0)

    else:
        x = x + C[0]
        C.pop(0)

print(x)




