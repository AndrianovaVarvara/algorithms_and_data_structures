# Дан ориентированный граф. Вершины пронумерованы от 0. Требуется с помощью топологической сортировки линейно
# упорядочить вершины графа в список так, чтобы для любого ребра графа из вершины A в вершину B, вершина A была
# левее чем B в списке.
#
# Формат входных данных
# На вход программе в первой строке подаются через пробел два числа: N (2 <= N <= 1000) - число вершин в графе
# и M (1 <= M <= 20000) - число ребер. В следующих M строках задаются ребра, по два числа в каждой строке -
# номера соединенных вершин (соответствующее ребро идет из первой вершины во вторую).
#
# Формат выходных данных
# Требуется распечатать топологически отсортированный список вершин, если такой существует.
# Если упорядочить вершины можно несколькими способами выведите любой из них.
# Если упорядочить вершины нельзя выведите "NO" без кавычек.

# __________ реализация с лекции Хирьянова__________
# visited = [False] * N # отслеживаем циклы
# ans = []
#
# def topology_sort(start, G, visited, ans):
#     visited[start] = True
#     for u in G[start]:
#         if not visited[u]:
#             topology_sort(u, G, visited, ans)
#     ans.append(start)
#
# for i in range(N):
#     if not visited[i]:
#         topology_sort(i, G, visited, ans)
# ans[:] = ans[::-1]
# print(ans)

# def dfs_TS(vertex, G, used):
#     print(vertex, used)
#     used.append(vertex)
#     Color[vertex] = 1
#     for u in G[vertex]:
#         if u not in used:
#             dfs_TS(u, G, used)
#         elif u in used and Color[u] == 2 and G[u] == set():
#             used.remove(u)
#             used.append(u)
#         elif u in used and Color == 2:
#             x = used.index(u)
#             used.insert(0 , vertex)
#         elif u in used and Color[u] == 1:
#             print('NO')
#             exit()
#     Color[vertex] = 2
#
#
# used = []
# for vertex in G:
#     if vertex not in used:
#         dfs_TS(vertex, G, used)
# print(*used, sep=' ')

N,M = [int(x) for x in input().split()]
G = {x: set() for x in range(N)}
for i in range (M):
    v1,v2 = map(int, input().split())
    G[v1].add(v2)

def dfs(vertex, G, color, ans):
    color[vertex] = 1
    for neib in G[vertex]:
        if color[neib] == 0:
            dfs(neib, G, color, ans)
        elif color[neib] == 1:
            print('NO')
            exit()
    color [vertex] = 2
    ans = ans.insert(0, vertex)

color = [0] * N
ans = []
for vertex in G:
    if color[vertex] == 0:
        dfs(vertex, G, color, ans)
print(*ans, sep=' ')