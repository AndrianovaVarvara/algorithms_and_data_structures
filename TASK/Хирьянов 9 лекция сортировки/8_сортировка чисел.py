N = int(input())
A = list(input().split())
for i in range(len(A)):
    A[i] = A[i].rjust(5, '0')
    revers = A[i][::-1]
    A[i] = revers
def hoar_sort(A: list):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)

    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

    return A

hoar_sort(A)

for i in range(len(A)):
    A[i] = A[i].rstrip('0')
    revers = A[i][::-1]
    A[i] = revers
print(*A, end=' ')
