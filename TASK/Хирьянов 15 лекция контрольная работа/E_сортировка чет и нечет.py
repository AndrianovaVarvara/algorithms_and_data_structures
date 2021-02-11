A = list(map(int, input().split()))
even = []
odd = []
for i in range(len(A)):
    if A[i] % 2 == 0:
        even.append(A[i])
    else:
        odd.append(A[i])
even.sort()
odd.sort()
A = even + odd
print(*A, sep=' ')