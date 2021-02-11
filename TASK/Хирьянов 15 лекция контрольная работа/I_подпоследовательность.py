A=input()
B=[0]*len(A)
# из 30 заваливает 13 тестов.
# можно попробовать проверять подстроку не на увеличение,  на уменьшение
for i in range(2,len(A)):
    s = A[:i+1]
    x = len(s)-2
    sub = A[:x]

    while x>=1:

        if s.rfind(sub)==len(s)-len(sub):
            if sub in s[1:len(s)-1]:
                if len(sub) < B[i]:
                    break
                B[i] = len(sub)

        x-=1
        sub = A[:x]


print(*B, sep=' ')