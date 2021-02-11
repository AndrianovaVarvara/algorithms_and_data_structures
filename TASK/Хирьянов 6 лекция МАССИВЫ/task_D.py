# Обработка массива чисел

A = []
while True:
    a = input()
    if ' ' in a:
        a = a[3:] +' '+ a[:3]
        print(a.lstrip(' '))
        exit()

    elif a == '#':
        if len(A) % 3 == 0:
            break
        else:
            continue
    else:
        a = int(a)
        if a <= 0 or a > 102:
            print(0, 0, 0, 0)
            exit()
        A.append(a)

s = round((sum(A) / len(A)), 3)
m = max(A)
n = min(A)

C = []
while A:
    a = (A[0] + A[1] + A[2]) % A[2]
    for i in range(3):
        A.pop(0)
    C.append(a)
x = sum(C)

print(s, m, n, x)
