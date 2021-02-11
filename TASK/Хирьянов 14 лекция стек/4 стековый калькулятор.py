def calc(A):
    '''читает выражение в обратной польской нотации и считает его значение или пишет, что выражение составлено не
     корректно (если оно некорректно)'''
    s = []
    for token in A:
        type(token) == str
        if type(token) != str:
            s.append(token)
            print(s)
        else:
            if token == '+':
                x = s.pop()
                y = s.pop()
                z = y + x
                s.append(z)
            elif token == '*':
                x = s.pop()
                y = s.pop()
                z = y * x
                s.append(z)
            elif token == '-':
                x = s.pop()
                y = s.pop()
                z = y - x
                s.append(z)
            elif token == '/':
                x = s.pop()
                y = s.pop()
                z = y / x
                s.append(z)


    res = s.pop()

    return res

A = [2,7,'+',5,'*']
print(calc(A))