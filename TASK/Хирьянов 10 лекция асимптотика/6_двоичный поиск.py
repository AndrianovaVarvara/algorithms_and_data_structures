# Задание №6: двоичный поиск

# Если массив упорядочен, то для такого массива можно написать эффективный алгоритм поиска — двоичный
# (или *бинарный*) поиск. Напишите реализацию этого алгоритма:

def binary_search(a, x):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right)//2
        if a[middle]<x:
            left = middle
        else:
            right = middle
    return right


# def binary_search_recursiv(arr, l, r, x):
#     if r >= l:
#         mid = l + (r - l) // 2
#
#         if arr[mid] == x:
#             return mid
#
#         elif arr[mid] > x:
#             return binary_search_recursiv(arr, l, mid - 1, x)
#
#         else:
#             return binary_search_recursiv(arr, mid + 1, r, x)
#     else:
#
#         return -1

assert binary_search([1, 2, 3, 4, 5], 5)  == 4
assert binary_search([1, 2, 3, 4, 5], 3)  == 2
assert binary_search([1, 2, 3, 4, 5], 1)  == 0

