def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(A[1:])
    return list[0] if list[0] > sub_max else sub_max

A = [2,4,6]
print(max(A))
