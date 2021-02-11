# Високосный год
N = int(input())
if N % 4 == 0:
    if N % 100 == 0 :
        if N % 400 != 0:
            print ('NO')
        else:
            print('YES')
    else:
        print('YES')
else:
    print('NO')


