# for row in range(10):
#
#     for j in range(row):
#         print(" ", end=" ")
#
#     for j in range(10 - row):
#         print(j, end=" ")
#
#     print()
def hw():
    print('Hello World.')

hw()

def Bob(name: str):
    print('Hello ' + name)

Bob('Bobby')

def prodact(a,b):
    print(a*b)

prodact(3,4)

def seven(phrase:str, count:int):
    print(phrase*count)

seven('Hello ', 5)

def stepen_4isla(a):
    return a**2

print(stepen_4isla(5))

def centrifugal_forse(radius:int, angular_velosity: int, massa: int):
    return (massa * radius * (angular_velosity**2))

print(centrifugal_forse(3,2,5))

def what_iside_list(A:list):
    for i in range(len(A)):
        print(A[i])

what_iside_list([1,2,3])


