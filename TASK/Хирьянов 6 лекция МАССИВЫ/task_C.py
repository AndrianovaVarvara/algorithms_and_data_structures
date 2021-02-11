# Максимальное число подряд идущих 1

N = int(input())
A = [0] * N
top = 0
while top < N:
    x = int(input())
    A[top] = x
    top +=1
count = 0
B = []
for i in range (N):
    if A [i] == 1:
        count +=1
    else:
        B.append(count)
        count = 0
B.append(count)
print(max(B))
