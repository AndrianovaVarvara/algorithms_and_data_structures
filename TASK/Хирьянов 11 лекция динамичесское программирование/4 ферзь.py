def queen(N, M):
    '''ДОСКА ПЕРЕВЕРНУТА! определяет выйгрышная(= 1) или пройгрышная (= 0) позиция у первого игрока'''
    A = [[1] * M for i in range(N)]
    # координаты нулей выше основной диагонали
    n = b = a = 0
    while a < N and b < M:
        a = b-n
        i = a
        j = b
        A[i][j] = 0
        if n % 2 == 0:
            b += 2
        else:
            b += 3
        n += 1
    # координаты нулей ниже основной диагонали
    n = b = a = 0
    while a < N and b < M:
        b = a - n
        i = a
        j = b
        A[i][j] = 0
        if n % 2 == 0:
            a += 2
        else:
            a += 3
        n += 1
# print(*A, sep="\n")

    return A[N-1][M-1]

print(queen(2,3))

def king (N,M):
    '''определяет в выйгрышной (=1) или пройгрышной (=0) позиции находится первый игрок'''
    A = [[1] * M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if j % 2 == 0 and i % 2 == 0:
                A[i][j] =  0
#print(*A, sep="\n")
    return A[N - 1][M - 1]

print(king(3,5))
