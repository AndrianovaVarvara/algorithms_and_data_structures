# Дан невзвешенный неориентированный связный граф. Вершины пронумерованы от 0.
# Трeбуется с помощью обхода в ширину найти расстояния от 0-й до всех остальных вершин.
#
# Формат входных данных
# На вход программе в первой строке подаются через пробел два числа: n (2 <= n <= 1000) — число вершин в графе
# и m (1 <= m <= 20000) — число рёбер. В следующих m строках задаются ребра: по два числа в каждой строке —
# номера соединённых вершин.
#
# Формат выходных данных
# Требуется распечатать n чисел, каждое на новой строке. В первой строке — расстояния от 0-й вершины до 0-й,
# во второй - от 0-й до 1-й, в третьей — от 0-й до 2-й и т.д.

n, m = map(int, input().split())
graph = {i: set() for i in range(n)}
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

from collections import deque

distance = [None] * n
start_vertex = 0
queue = deque([start_vertex])
distance[start_vertex] = 0
while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distance[neigh_v] is None:
            distance[neigh_v] = distance[cur_v] + 1
            queue.append(neigh_v)
for i in range(n):
    print(distance[i])