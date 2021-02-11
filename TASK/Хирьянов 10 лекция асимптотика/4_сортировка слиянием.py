# Задание №4: сортировка слиянием

# Напишите реализацию сортировки слиянием:

def merge(a, b):
    C = [0]*(len(a)+len(b))
    i=k=n=0
    while i < len(a) and k < len(b):
        if a[i]<=b[k]:
            C[n]=a[i]
            i+=1
            n+=1
        else:
            C[n] = b[k]
            k+=1
            n+=1
    while i < len(a):
        C[n]=a[i]
        i+=1
        n+=1
    while k < len(b):
        C[n] = b[k]
        k+=1
        n+=1
    return C

def merge_sort(a):
    if len(a) <= 1:
        return
    middle = len(a)//2
    l=[a[i] for i in range(0,middle)]
    r=[a[i] for i in range(middle, len(a))]
    merge_sort(l)
    merge_sort(r)
    C = merge(l,r)
    for i in range(len(a)):
        a[i] = C[i]
    return a
# Проверьте корректность реализации:

a = [5, 4, 3, 2, 1]
print(merge_sort(a))

# assert util.is_sorted(a)

# А теперь сравним скорость работы трёх написанных нами алгоритмов:

util.plot_sort_results(
    ('Быстрая сортировка: произвольный элемент в качестве опорного', quick_sort_random),
    ('Сортировка слиянием', merge_sort),
    ('Сортировка пузырьком: обычная реализация', bubble_sort)
    )
util.plot_sort_results(
    ('Быстрая сортировка: первый элемент в качестве опорного', quick_sort_first),
    ('Сортировка слиянием', merge_sort),
    ('Сортировка пузырьком: пеализация с проверкой на отсортированность', bubble_sort)
    )

# **Вопрос**: какие выводы можно сделать из полученных результатов?
# В чём принципиальное отличие сортировки слиянием от двух других рассмотренных?

