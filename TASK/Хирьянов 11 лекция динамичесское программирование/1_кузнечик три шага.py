def traject(N):  # +1, +2, +3
    K = [0, 1, 2] + [None] * (N - 2)
    for i in range(3, N + 1):
        K[i] = K[i - 1] + K[i - 2] + K[i - 3]
    return K[N]

print(traject(6))


def traject_v2(N):  # +1, +2, *3
    K = [1, 1, 2] + [None] * (N - 2)
    # создаем отдельный массив где хранятс номера позиций *3
    check = [2]+[0]*int(N**(1/3))
    for i in range(1, len(check)):
        check[i] = check [i-1]*3
    # и если номер позиции находится в check то к сумме надо прибавить еще один способ
    for i in range(3, N + 1):
        if i not in check:
            K[i] = K[i - 1] + K[i - 2]
        else:
            K[i] = K[i - 1] + K[i - 2] + 1
    return K[N]


print(traject_v2(3))
