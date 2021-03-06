#  Сортировки
# Здесь и далее мы предполагаем, что все функции сортировки упорядочивают исходный массив по возрастания.
# Функции сортировки в этой работе должны изменять переданный массив, а не возвращать новый.

# Задание №2: сортировка пузырьком

# Напишите обычную реализацию сортировки пузырьком:

def bubble_sort(a):
    N = len(a)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
                print(a[k], a[k + 1])
    return a

# Убедитесь, что сортировка написана верно:

a = [4, 3, 5, 8, 6, 2]
print(bubble_sort(a))
# assert util.is_sorted(a)

# Особенность обычной реализации пузырьковой сортировки состоит в том, что она «не замечает»
# отсортированности массива. Это означает, что даже если массив уже отсортирован, алгоритм
# всё равно будет выполнен от начала и до конца. Чтобы этого избежать, можно добавить специальный флаг,
# показывающий, была ли за прошлый проход выполнена хоть одна перестановка. Если перестановок не было,
# значит, массив уже отстортирован. Напишите улучшенную реализацию сортировки пузырьком:
#
def bubble_sort_adaptive(a):
    j = len(a) - 1
    IsNotOrdered = True
    while IsNotOrdered:
        IsNotOrdered = False
        for i in range(0, j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                print(a[i], a[i + 1])
                IsNotOrdered = True
        j -= 1

    return a

# Проверьте свою реализацию:

b = [4, 3, 5, 8, 6, 2]
print(bubble_sort_adaptive(b))
# assert util.is_sorted(a)

# А теперь сравните скорость работы двух реализаций одного алгоритма при различных входных данных:

# util.plot_bubble_sort_results(
#     ('Обычная реализация', bubble_sort),
#     ('Реализация с проверкой на отсортированность', bubble_sort_adaptive)
#     )

# **Вопрос**: какие выводы можно сделать из полученных результатов?
