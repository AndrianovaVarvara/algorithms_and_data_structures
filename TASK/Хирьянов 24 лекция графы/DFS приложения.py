N,M = [int(x) for x in input().split()]
# G - реализация графа списком смежностей
G = [set() for x in range(N)]
# A - реализация графа матрицей смежности (простой неориентированный граф
# A = [[0] * N for i in range(N)]
for i in range (M):
    v1,v2 = map(int, input().split())
    # A[v1][v2] = 1
    # A[v2_i][v1_i] = 1 # если граф ориентированный, эта строка не нужна
    G[v1].add(v2)
#
# print('Реализация графа списком смежностей:')
# print(*G, sep='\n')
#
# print('Реализация графа матрицей смежности:')
# print(*A, sep='\n')

# С помощью обхода в глубину мы можем:
# 1) подсчитать количество вершин
# 2) найти остовное дерево
# 3) обнаружить простой цикл
color = [0] * N
predki = []

def dfs(vertex):
    color[vertex] = 1
    if G[vertex] != set():
        for neig in G[vertex]:
            if color[neig] == 0:
                predki.append(vertex)
                dfs(neig)
                predki.pop()
            elif color[neig] == 1:
                predki.append(vertex)
                print(predki)

    color[vertex] = 2


for i in range(len(G)):
    if color[i] == 0:
        dfs(i)

# 4) выделить компоненты связности графа
# у орграфов:
# - выделение сильных компонент (алгоритм Косорайо)
# - топологическая сортировка
# 5) посчитать количество компонент
# 6) проверить граф на двудольность