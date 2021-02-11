def calculate_min_cost(n, price):
    C = [float('-inf'), price[1], price[1] + price[2]] + [0] * (n - 2)
    for i in range(3, n + 1):
        C[i] = price[i] + min(price[i - 1], price[i - 2])
        # по другому минимум можно записать (price[i-1] if price[i-1]<price[i-2] else price[i-2])
    return C[n]


print(calculate_min_cost(5, [0, 1, 3, 1, 2, 5]))


def traject_min_cost(n, price):
    C = [None, price[1], price[1]+price[2]] + [0]*(n-2)
    Prev = []
    for i in range(3, n+1):
        C[i] = price[i] + min(price[i-1], price[i-2])
        if  C[i-1] < C[i-2]:
            Prev.append(i-1)
        else:
            Prev.append(i-2)
    print (C)
    print(Prev)



print(traject_min_cost(5, [0, 1, 3, 1, 2, 5]))
