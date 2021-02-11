def sort_station(list=input()):
    operators_stack = []
    output = []
    for token in list:
        if token not in ['+', '-','*', '/']:
            output.append(token)
        else:
            if len(operators_stack)==0:
                operators_stack.append(token)
            elif (operators_stack[-1] in ['+', '-']) and (token in ['*', '/']):
                operators_stack.append(token)
            elif (operators_stack[-1] in ['*', '/']) and (token in ['*', '/']):
                x = operators_stack.pop()
                output.append(x)
                operators_stack.append(token)
            else:
                while len(operators_stack) > 0:
                    x = operators_stack.pop()
                    output.append(x)
                operators_stack.append(token)
    while len(operators_stack) > 0:
        x = operators_stack.pop()
        output.append(x)

    print(output)

sort_station()

# a-b+c*d/a
# ['a', 'b', '-', 'c', 'd', '*', 'a', '/', '+']

# a+b∗c−d
# [a,b,c,*,+,d,-]

#