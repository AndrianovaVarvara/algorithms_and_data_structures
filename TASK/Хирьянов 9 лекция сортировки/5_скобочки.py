A = input()
if A [0] == ')':
    print('NO')
    exit()
check = 0
while A != '':
    if A[0]== '(' and A[1] == ')':
        A = A[2:]

    elif A[0]== '(' and A[1] == '(':
        check += 1
        A = A[2:]

    elif A[0] == ')' and A[1] == ')':
        check -=1
        A = A[2:]

if A == '' and check == 0:
    print("YES")
else:
    print('NO')