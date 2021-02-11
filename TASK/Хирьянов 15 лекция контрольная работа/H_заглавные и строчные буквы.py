A = input()
big = 0
small = 0
for i in range (len(A)):
    if ord(A[i]) >= 65 and ord(A[i]) <=90:
        big+=1
    if ord(A[i]) >= 97 and ord(A[i]) <=122:
        small+=1
print(big, small)

