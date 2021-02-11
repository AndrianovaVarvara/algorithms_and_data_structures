K = int(input())
A = list(map(int, input().split()))
A.sort()
B = []
for i in range (0, len(A) // 2 + 1):
    x= A.pop(0)
    B.append(x)
C = []
for i in range (len(B)):
    x = B[i]// 2 + 1
    C.append(x)
print(sum(C))
