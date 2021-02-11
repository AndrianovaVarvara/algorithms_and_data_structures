import A_stack

def is_braces_sequence_correct(s: str):
    '''
    Проверяет корректность скобочной последовательности из круглых, квадратных и фигурных скобок
    >>> is_braces_sequence_correct("(([{}]))")
    True
    >>> is_braces_sequence_correct("([{)]}")
    False
    >>> is_braces_sequence_correct(")")
    False
    >>> is_braces_sequence_correct("[")
    False
    '''
    for brace in s:
        if brace not in "()[]{}": # игнорирование не скобочных символов
            continue
        if brace in "([{": # это встроенная типовая функция, поиска подстроки в строке, лучше КМП или Z-функции
            A_stack.push(brace)
        else: # если мы сюда попали, точно закрывающаяся скобка встретилась, но пусть программа перепроверит
            assert brace in ")]}", "Катастрофа! Ожидалась закрывающая скобка: " + str(brace)
            # говорящий и действующий коммент, она для алгоритма не делает ничего
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            assert left in "([{",  "Катастрофа! Ожидалась закрывающая скобка: " + str(brace)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            elif left == "{":
                right = "}"
            if right!=brace:
                return False
    return A_stack.is_empty()


if __name__ =='__main__':
    import doctest
    doctest.testmod()
