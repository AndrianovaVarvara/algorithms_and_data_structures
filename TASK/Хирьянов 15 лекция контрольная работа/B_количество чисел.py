x = int(input())
m = x
count = 0
while 1:
    x = int(input())
    if x == 0:
        break
    else:
        if x != m:
            if x > m:
                m = x
            count+=1
print(count)
