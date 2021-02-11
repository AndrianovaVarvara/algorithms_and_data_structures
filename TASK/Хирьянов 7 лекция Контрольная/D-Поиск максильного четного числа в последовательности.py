

# если четные числа в ней присутствуют, иначе - 0.
A = []
while 1:
    x = int(input())
    if x == 0:
        break
    elif x %2 == 0:
        A.append(x)
if len(A) == 0:
    print(0)
else:
    print(max(A))