N = int(input())
A = []
for i in range(N):
    x = list(map(float, input().split()))
    A.append(x)

for pos in range(0, N-1):
    for k in range(pos+1,N):
        if A[k][1] < A[pos][1]:
            A[k], A[pos] = A[pos], A[k]
        elif A[k][1] == A[pos][1]:
            if A[k][0] > A[pos][0]:
                A[k], A[pos] = A[pos], A[k]
for i in range (N):
    A[i][0] = '{:.2f}'. format(float(A[i][0]))
    A[i][1] = '{:.3f}'.format(float(A[i][1]))
    print(*A[i])