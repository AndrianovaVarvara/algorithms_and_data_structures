# Дан невзвешенный связный граф. Вершины пронумерованы от 0.
# Трeбуется с помощью обхода в ширину найти расстояние от одной указанной вершины до другой.
#
# Формат входных данных
# На вход программе в первой строке подаются через пробел четыре числа: n, m, x, y.
# Число n (2 <= n <= 1000) - количество вершин в графе, m (1 <= m <= 20000) - количество ребер.
# x и y - начальная и конечная вершины соответственно (0 <= x,y < n).
# В следующих m строках задаются ребра, по два числа в каждой строке - номера соединенных вершин.
#
# Формат выходных данных
# Требутеся распечатать одно число - расстояние от вершины x до вершины y .

n, m, x, y = map(int, input().split())
graph = {i: set() for i in range(n)}
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

from collections import deque

distance = [None] * n
start_vertex = x
queue = deque([start_vertex])
distance[start_vertex] = 0
while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distance[neigh_v] is None:
            distance[neigh_v] = distance[cur_v] + 1
            queue.append(neigh_v)
print(distance[y])
