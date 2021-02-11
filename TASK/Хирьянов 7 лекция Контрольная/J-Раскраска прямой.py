N = int(input())
a = [[int(input()) for x in range(3)] for i in range(N)]

M = int(input())
c = [int(input()) for x in range(M)]
if len(c)==0:
    for i in range (M):
        print(0, end=' ')

itog = []
tmp = []
for k in range(M):
    for i in range(len(a)):
        if a[i][0] <= c[k] <= a[i][1]:
            tmp.append(a[i])

    if len(tmp) > 0:
        x = (tmp[-1][-1])
        itog.append(x)
        tmp.clear()
    else:
        itog.append(0)
print(*itog, end=' ')
