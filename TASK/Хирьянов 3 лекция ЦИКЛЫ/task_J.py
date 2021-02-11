# Количество элементов, равных максимуму
list = []
while True:
    a = int(input())
    list.append(a)
    if a == 0:
        break
print(list.count(max(list)))