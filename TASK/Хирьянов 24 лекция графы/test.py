N,M = [int(x) for x in input().split()]
G = {x: set() for x in range(N)}
for i in range (M):
    v1,v2 = map(int, input().split())
    G[v1].add(v2)

color = [0] * N
path = []

def dfs(vertex):
    if G[vertex] != set():
        color[vertex] = 1
        path.append(vertex)
        for neig in G[vertex]:
            if color[neig] == 0:
                dfs(neig)
            elif color[neig] == 1:
                print('CYCLE', path)

        color[vertex] = 2
        path.pop()
    # else:
    #     color[vertex] = 2


for vertex in G:
    if color[vertex] == 0:  # последовательно обрабатываем все вершины
        dfs(vertex)
print(color)

