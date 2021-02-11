N = int(input())
A = list(map(int, input().split()))
B=[]
count = 0
for i in range(N):
    if A[i] > 0:
        count+=1
    else:
        B.append(count)
        count=0
B.append(count)
print(max(B))