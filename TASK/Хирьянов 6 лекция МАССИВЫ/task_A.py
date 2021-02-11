# Принадлежность точки кругу

x, y, r = map(int, input().split())
if r ** 2 >= x ** 2 + y ** 2:
    print('YES')
else:
    print('NO')
