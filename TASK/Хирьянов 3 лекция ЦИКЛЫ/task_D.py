# Список квадратов
N = int(input())
A = []
for i in range (N):
    if 0 < i ** 2 <= N:
        A.append(i**2)
print(*A)