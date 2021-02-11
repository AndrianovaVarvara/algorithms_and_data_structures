# def fibonachi(n):
#     '''Если n = 1 или n = 2, вернуть в вызывающую ветку единицу,
#     так как первый и второй элементы ряда Фибоначчи равны единице.
#     Во всех остальных случаях вызвать эту же функцию с аргументами n - 1 и n - 2.
#     Результат двух вызовов сложить и вернуть в вызывающую ветку программы.'''
#     if n in (1, 2):
#         return 1
#     return fibonachi(n - 1) + fibonachi(n - 2)
#
# print(fibonachi(0))

#
# def recursive_fib_with_cache(n, cache=None):
#     A = [0,1]
#     while len(A) < n+1:
#         A.append(0)
#     if n <= 1:
#         return n
#     else:
#         if A[n - 1] == 0:
#             A[n - 1] = recursive_fib_with_cache(n - 1)
#
#         if A[n - 2] == 0:
#             A[n - 2] = recursive_fib_with_cache(n - 2)
#
#         A[n] = A[n - 2] + A[n - 1]
#
#         return A[n]
#
#
#
#
# print(recursive_fib_with_cache(9, cache=None))

# реализация моя через for
def fib(n):
    if n == 0:
        return 0
    A = [1,1]
    while len(A) < n:
        A.append(0)
    for i in range (2, n):
        A[i] = A[i - 1] + A[i -2]
    return A[-1]

print(fib(1))
#
# # реализация через while
# fib1 = fib2 = 1
# n = int(input("Номер элемента ряда Фибоначчи: ")) - 2
# while n > 0:
#     fib1, fib2 = fib2, fib1 + fib2
#     n -= 1
# print(fib2)
