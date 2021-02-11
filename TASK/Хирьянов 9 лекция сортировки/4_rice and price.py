price, delta, m = map(int,input().split())
day = 0
week = 0
summa = price
while week < m:
    while day < 7:
        price = price + delta
        summa += price
        day += 1

    day=0
    week += 1

print(summa-price)
