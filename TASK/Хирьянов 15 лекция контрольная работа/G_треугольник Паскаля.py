N=int(input())+1
A = [[0]*i for i in range (1,N+1)]
for i in range (N):
    A[i][0] = A[i][i] = 1
    for j in range (1, len(A[i])-1):
        A[i][j] = A[i-1][j-1]+A[i-1][j]
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end = ' ')
    print()