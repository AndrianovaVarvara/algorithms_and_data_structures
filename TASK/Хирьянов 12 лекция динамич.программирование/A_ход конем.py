x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Cоздадим массив где  эементами  будут являться первые позиции, в которые можно попасть с отправной точки.
# Нужна проверка, на выход-невыход за пределы доски. Проверка заданных координат (если да - принт 1).
# Если нет, создаем второй список. Проверка заданных координат (если да - принт 2, если нет - принт -1).

if x1 == x2 and y1 == y2:
    print(0)
    exit()

moves=[[1,2],[1,-2],[-1,2],[-1,-2], [2,1],[2,-1],[-2,1],[-2,-1]]
F = []
for dx,dy in moves:
    x = x1+dx
    y = y1+dy
    if 0<x<9 and 0<y<9 and [x,y] not in F:
        F.append([x,y])

if [x2,y2] in F:
    print(1)
    exit()

S = []
for Fx,Fy in F:
    for dx,dy in moves:
        x = Fx+dx
        y = Fy+dy
        if 0<x<9 and 0<y<9 and [x,y] not in S:
            S.append([x,y])

if [x2,y2] in S:
    print(2)
    exit()

if [x2,y2] not in F and [x2,y2] not in S:
    print(-1)
# n = 2
# m = 1
# if x1 - n > 0 and y1 - m > 0:
#     x = x1 - n
#     y = y1 - m
#     A[0][0] = x
#     A[0][1] = y
# n = 2
# m = -1
# if x1 - n > 0 and y1 - m > 0:
#     x = x1 - n
#     y = y1 - m
#     A[1][0] = x
#     A[1][1] = y
# n = 1
# m = 2
# if x1 - n > 0 and y1 - m > 0:
#     x = x1 - n
#     y = y1 - m
#     A[2][0] = x
#     A[2][1] = y
# n = 1
# m = -2
# if x1 - n > 0 and y1 - m > 0:
#     x = x1 - n
#     y = y1 - m
#     A[3][0] = x
#     A[3][1] = y
# n = -1
# m = 2
# if x1 - n > 0 and y1 - m > 0:
#     x = x1 - n
#     y = y1 - m
#     A[4][0] = x
#     A[4][1] = y
# n = -1
# m = -2
# if x1 - n > 0 and y1 - m > 0:
#     x = x1 - n
#     y = y1 - m
#     A[5][0] = x
#     A[5][1] = y
# n = -2
# m = 1
# if x1 - n > 0 and y1 - m > 0:
#     x = x1 - n
#     y = y1 - m
#     A[6][0] = x
#     A[6][1] = y
# n = -2
# m = -1
# if x1 - n > 0 and y1 - m > 0:
#     x = x1 - n
#     y = y1 - m
#     A[7][0] = x
#     A[7][1] = y
#
# F = []
# for row in A:
#     for elem in row:
#         if elem != 0:
#             F.append(elem)
#
# print(F)


# A = [[x - 1, y - 2], [x + 1, y - 2], [x - 2, y - 1], [x + 2, y - 1], [x - 2, y + 1], [x + 2, y + 1],
#      [x - 1, y + 2], [x + 1, y + 2]]


# РЕКУРСИВНОЕ РЕШЕНИЕ ЗАДАЧИ ИЗ ИНЕТА
#
# У меня переменная depth отвечает как раз за то, насколько глубоко нужно просчитать ходы.
#
# Есть функция GetNextMoves. Она на вход принимает координаты коня, а возвращает лист возможных позиций коня спустя ход.
#
# Также есть рекурсивная функция CalculateMoves, которая как раз "ходит" по древу всех вариантов.
#
# В итоге всё записывается в лист globalArr.

# moves=[[1,2],[1,-2],[-1,2],[-1,-2], [2,1],[2,-1],[-2,1],[-2,-1]]
# globalArr = []
#
# def CalculateMoves(depth, i, j):
#
#     arr = GetNextMoves(i, j)
#
#     if depth > 1:
#
#         for move in arr:
#             CalculateMoves(depth - 1, move[0], move[1])
#
#     else:
#
#         globalArr.extend(arr)
#         #на этом шаге наверное стоит почистить от повторений лист globalArr
#         #  и понять куда делись шаги первого порядка
#
#
# def GetNextMoves(i, j):
#     arr = []
#
#     for dx, dy in moves:
#         x = i + dx
#         y = j + dy
#
#         if 0 < x < 9 and 0 < y < 9 and [x, y] not in arr:
#             arr.append([x, y])
#
#     return arr
#
# i = int(input())
# j = int(input())
#
# CalculateMoves(2, i, j)
#
# print(globalArr)