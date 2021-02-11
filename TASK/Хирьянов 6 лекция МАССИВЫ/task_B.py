# Банковский вклад
try:
    x, p, y = map(int, input().split())
    A = []
    while x < y:
        per = round((x * p / 100 - 0.005), 2)  # 0.005 решает проблему с округлением
        x = round((x + per), 2)
        A.append(x)
    print(len(A))
except ValueError:
    print(0)
