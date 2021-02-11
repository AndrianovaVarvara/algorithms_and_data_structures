start_sum = int(input())
traject = list(map(int, input().split()))
kapital = [0,start_sum,0] + [0]* (len(traject)-2)
Prev = [0,0,0]
for i in range(3,len(traject)+1):
    if kapital[i-2]>kapital[i-3]:
        x = kapital[i-2]
        kapital[i] = int(x + x * (traject[i-1] / 100))
        Prev.append(i-2)
    else:
        x = kapital[i - 3]
        kapital[i] = int(x + x * (traject[i - 1] / 100))
        Prev.append(i - 3)

Path = []
if max(kapital)>start_sum:
    if kapital[-2]==kapital[-1]:
        i = kapital.index(kapital[-2])

        while i > 0:
            Path.append(i)
            i = Prev[i]
    else:
        i = kapital.index(max(kapital))
        while i > 0:
            Path.append(i)
            i = Prev[i]
    Path = Path[::-1]
else:
    Path.append(1)


print(*Path, sep=' ')
