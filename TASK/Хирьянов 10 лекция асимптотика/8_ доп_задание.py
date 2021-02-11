# Дополнительное задание

# Если у вас осталось время, то напишите реализацию сортировки слияением с разбиением исходного массива
# на 3 части. Сравните скорость работы двух реализаций.
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

def merge_sort_three(A):
    if len(A) <= 1:
        return
    part = len(A) // 3
    first_part = [A[i] for i in range(0, part)]
    second_part = [A[i] for i in range(part, len(A)-1)]
    third_part = [A[i] for i in range(len(A)-1, len(A))]

    merge_sort_three(first_part)
    merge_sort_three(second_part)
    merge_sort_three(third_part)
    B = merge(first_part, second_part)
    C = merge (B, third_part)
    for i in range (len(A)):
        A[i] = C [i]
    return A


list = [5,3,7,4,9]
print(merge_sort_three(list))
print(len(list))

