# Дан неориентированный граф содержащий гамильтонов цикл, требуется найти этот цикл.
#
# Формат входных данных
# На вход программе в первой строке подаются через пробел два числа: N (3 <= N <= 18) -
# число вершин в графе и M (1 <= M <= 200) - число ребер. В следующих M строках задаются ребра,
# по два числа в каждой строке - номера соединенных вершин.
#
# Формат выходных данных
# Требуется распечатать номера вершин, задающих гамильтонов цикл в графе.
# Номера вершин нужно вывести в порядке следования по циклу. Если циклов несколько вывести любой.

# 3 3
# 0 2
# 0 1
# 1 2
#
# 0 2 1

# 5 6
# 1 3
# 3 2
# 1 0
# 1 2
# 4 2
# 4 0

# 0 1 3 2 4

N,M = [int(x) for x in input().split()]
G = {x: set() for x in range(N)}
for i in range (M):
    v1,v2 = map(int, input().split())
    G[v1].add(v2)
    G[v2].add(v1)


Visited = [False] * N
Path = []

def hamilton(vertex):
    Path.append(vertex)
    Visited[vertex] = True
    if len(Path) == N:
        if Path[0] in G[Path[-1]]:
            for i in Path:
                print(i, end = " ")
            exit()

    for neig in G[vertex]:
        if Visited[neig] == False:
            hamilton(neig)
    Visited[vertex] = False
    Path.pop()

hamilton(0)