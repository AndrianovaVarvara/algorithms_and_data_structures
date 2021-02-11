A = [int(input()) for x in range(8)]

if A[0] + A[2] > A[6] or A[1] + A[5] > A[7]:
    print('NO')
    exit()

if A[3] <= A[5]:
    print('YES')
elif A[1]+A[3] <A [7]:
    print('YES')
elif A[0] + A[2] +A[4]<=A[6]:
    print('YES')
else:
    print('NO')

