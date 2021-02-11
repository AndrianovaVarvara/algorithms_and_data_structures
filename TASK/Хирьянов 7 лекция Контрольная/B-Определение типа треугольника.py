# Если выполняется теорема Пифагора: 
# с²=a²+b² , треугольник прямоугольный right. 

#  с² < a²+b² треугольник остроугольный acute. 

# с² > a²+b² – треугольник тупоугольный obtuse. 

A = [int(input()) for x in range(3)]
A.sort(reverse=True)
if A[0] > A[1]+A[2]:
    print ('impossible')
    exit()
if A[0]**2 == A[1]**2+A[2]**2:
    print('right')
elif A[0]**2 < A[1]**2+A[2]**2:
    print('acute')
elif A[0]**2 > A[1]**2+A[2]**2:
    if A[1] == A[2]:
        print('impossible')
    else:
        print('obtuse')

