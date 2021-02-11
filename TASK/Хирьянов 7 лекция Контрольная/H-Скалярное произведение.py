#  vec1 = [int(x) for x in input().split(" ")]

def dot_product(N, vector1, vector2):
    A = []
    for i in range (N):
        x = vector1[i] * vector2[i]
        A.append(x)
    return sum(A)

