
A = list(bin(int(input())))
count = 0
for element in A:
    if element == '1':
        count +=1

print(count)