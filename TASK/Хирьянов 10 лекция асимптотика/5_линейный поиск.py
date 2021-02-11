#  Поиск элемента

# Теперь перейдём к алгоритмам поиска элемента в массиве.

# Задание №5: линейный поиск

# Для начала напишите самую простую реализацию поиска — линейный поиск элемента в массиве:

def search(a, x):
    for i in range (len(a)):
        if a[i] == x:
            return i
print(search([1, 2, 3, 4, 5], 5))
print(search([1, 2, 3, 4, 5], 3))
# Проверьте корректность реализации:

# assert search([1, 2, 3, 4, 5], 5)  == 4
# assert search([1, 2, 3, 4, 5], 3)  == 2

# Когда нам ничего не известно о данных, которые находятся в массиве, придумать какой-то более эффективный
# алгоритм достаточно сложно. Но если мы знаем какую-то дополнительную информацию о природе данных в массиве,
# то можно написать более эффективные алгоритмы.

