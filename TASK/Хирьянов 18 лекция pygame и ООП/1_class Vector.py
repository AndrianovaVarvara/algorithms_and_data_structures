class Vector:
    name =''

    def __init__(self, x, y):

        self.x = x
        self.y = y

    # def __repr__(self):
    #     return self.__dict__.__repr__()

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __neg__(self):
        return Vector(self.x * (-1), self.y * (-1))

    def center_of_mass(n: int, coords: list):
        x = y = 0
        for i in range(len(coords)):
            coord = coords[i]
            x += coord.x
            y += coord.y
        return print('Center of mass is (' + str(x/n) + ', ' + str(y/n) + ')')

    def show(self):
        print('Vector',  self.name,  '(' + str(self.x) + ',' + str(self.y) + ')')

a = Vector(1,2)
a.name = 'a'
a.show()
b = Vector(3,4)
b.name = 'b'
b.show()
c = Vector(5,6)
c.name = 'c'
c.show()

print(a.name, '+', b.name, a + b)
# print('Sub', a - b)
# print('Mul', a * 2)
# print('Neg', -a)
# # Vector.center_of_mass(3, coords)
# print(Vector(7,8))



