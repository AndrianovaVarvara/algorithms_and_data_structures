# Количество четных элементов

i = 0
while True:
    a = int(input())
    if a == 0:
        break
    elif a % 2 == 0:
        i += 1
print(i)
