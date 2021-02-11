# Формат входных данных
# В первой строке входного файла записаны два числа N и M - количество студентов и количество пар
# студентов, обменивающихся записками (1≤N≤1000, 0≤M≤20000). Далее в M строках расположены описания
# пар студентов: два числа, соответствующие номерам студентов, обменивающихся записками (нумерация
# студентов идёт с 0). Каждая пара студентов перечислена не более одного раза.
#
# Формат выходных данных
# Необходимо вывести ответ на задачу профессора. Если возможно разделить студентов на две группы -
# выведите номера вершин любой из этих групп(тех кому профессор поставит двойки =)) в одной строке
# через пробел, иначе выведите NO.
N,M = [int(x) for x in input().split()]
G = {x: set() for x in range(N)}
for i in range (M):
    v1,v2 = map(int, input().split())
    G[v1].add(v2)

color = [0] * N

def dfs (vertex):
    for neig in G[vertex]:

        if color[neig] == 0:
            color[neig] = 3 - color[vertex]
            dfs(neig)
        elif color[neig] == color[vertex]:
            if len(G[vertex]) == 1:
                color[vertex] = 3 - color[neig]
            else:
                print('NO')
                exit()


for i in range(N):
    if color[i] == 0:
        color[i] = 1
        dfs(i)


for i in range(len(color)):
    if color[i] == 1:
        print(i, end=' ')

        # 5 5
        # 0 1
        # 1 2
        # 2 3
        # 0 3
        # 3 4