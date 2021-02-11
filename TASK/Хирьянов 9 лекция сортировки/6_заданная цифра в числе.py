d, n = input().split()

count = 0
for char in n:
    if d == char:
        count+=1
if count > 0:
    print(count)
else:
    print(0)