# Максимум последовательности
list = []
while True:
    a = int(input())
    list.append(a)
    if a == 0:
        break
print(max(list))