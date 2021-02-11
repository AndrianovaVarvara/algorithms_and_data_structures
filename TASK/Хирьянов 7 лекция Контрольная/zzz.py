A = [int(input()) for x in range(8)]
result = 0
if A[3] <= A[5]:
    if (A[1] + A[5]) <= A[7]:
        result += 1
        if (A[0] + A[2]) <= A[6]:
            result += 1
    else:
        (A[0] + A[2]+ A[4]) <= A[6]
        result += 1
        if (A[1] + A[3]) <= A[7]:
            result += 1
if result == 2:
    print('YES')
else:
    print('NO')