# Одно число, которое встречается наибольшее количество раз.
N = int(input())
A = [0] * N
for i in range(len(A)):
    x = int(input())
    A[i] = x
B =[]
for i in range (N):
    x = A.count(A[i])
    B.append (x)
print (A[B.index(max(B))])
