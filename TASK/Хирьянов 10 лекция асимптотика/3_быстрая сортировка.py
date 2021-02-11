# Задание №3: быстрая сортировка
import random
# Напишите реализацию быстрой сортировки, использую первый элемент в качестве опорного

def quick_sort_first(a):
    if len(a)<=1:
        return
    barrier = a[0]
    l=[]
    m=[]
    r=[]
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    quick_sort_first (l)
    quick_sort_first (r)
    k=0
    for x in l+m+r:
        a[k] = x
        k+=1
    return a

# Проверьте свою реализацию:

a = [5, 4, 3, 2, 1]
print(quick_sort_first(a))
# assert util.is_sorted(a)

# Как вы знаете, скорость работы алгоритма быстрой сортировки напрямую зависит от способа выбора
# опорного элемента. Поэтому реализуем ещё два варианта. Сначала будем выбирать в качестве опорного
# элемента средний:
#
def quick_sort_middle(a):
    if len(a) <= 1:
        return
    barrier = a[len(a)//2]
    l = []
    m = []
    r = []
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    quick_sort_first(l)
    quick_sort_first(r)
    k = 0
    for x in l + m + r:
        a[k] = x
        k += 1
    return a

# Проверяем реализацию:

a = [5, 4, 3, 2, 1]
print(quick_sort_middle(a))
# assert util.is_sorted(a)

# А теперь в качестве опорного элемента выбираем произвольный элемент (при помощи вызова `random.choice(a)`)#    ]

def quick_sort_random(a):
    if len(a) <= 1:
        return
    barrier = random.choice(a)
    print(barrier)
    l = []
    m = []
    r = []
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    quick_sort_first(l)
    quick_sort_first(r)
    k = 0
    for x in l + m + r:
        a[k] = x
        k += 1
    return a

# Проверяем реализацию:

a = [5, 4, 3, 2, 1]
print(quick_sort_random(a))
# assert util.is_sorted(a)

# Сравним скорости работы трёх реализаций на различных входных данных:

util.plot_quick_sort_results(
    ('Первый элемент в качестве опорного', quick_sort_first),
    ('Средний элемент в качестве опорного', quick_sort_middle),
    ('Произвольный элемент в качестве опорного', quick_sort_random)
    )

# **Вопрос**: какую асимптотическую сложность имеют эти реализации на разных входных данных?
# Чем это объясняется?

