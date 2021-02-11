N = int(input())
A = [None]*N

for i in range(0,len(A)):
    A[i] = input()
dict = {}
with open("country_languages.txt", encoding="utf-8") as file:
    for line in file:
        key, *value = line.split()
        dict[key] = value[1:]
Otvet = [[] for k in range(N)]

for i in range(len(A)):
    for key in dict:
        if A[i] in dict[key]:
            x=key
            Otvet[i].append(x)
print(Otvet)
