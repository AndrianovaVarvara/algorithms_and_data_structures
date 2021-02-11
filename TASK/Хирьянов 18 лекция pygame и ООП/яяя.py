# class D:
#     def __str__(self):
#         return self.name + ' ' + str(self.score)
# # Метод __str__ будет вызываться, когда вызывается функция str от данного объекта, например, str(Vasya).
# # То есть создавая метод __str__ вы даете указание Питону, как преобразовывать данный объект к типу str.
#
# class Vector:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
# # Теперь при вызове оператора a + b Питон вызовет метод a.__add__(b), то есть вызовет указанный метод,
# # где self = a, other = b.
#
# class Vector:
#     def __lt__(self, other):
#         return self.x < other.x or self.x == other.x and self.y < other.y
# # В этом примере оператор вернет True, если у левого операнда поле x меньше, чем у правого операнда,
# # а также если поля x у них равны, а поле y меньше у левого операнда.
#
    # class Animal:
    #     name=''
    #
    #     def __init__(self, name):
    #         self.name = name
    #         print('Animal ', self.name, ' was born')
    #
    #     def yum(self):
    #         print('Yum-yum')
    #
    #     def makeNoise(self):
    #         print(self.name,'say Grr')
    #
    # animal_1 = Animal('Timon')
    # animal_1.makeNoise()
    # animal_2 = Animal('Richard')
    # animal_2.makeNoise()
#
# class FirstClass: # Определяет объект класса
#     def setdata(self, value): # Определяет метод класса
#         self.data = value # self – это экземпляр
#         return  self.data
#     def display(self):
#         print(self.data)
#
# class SecondClass(FirstClass): # Наследует setdata
#     def display(self): # Изменяет display
#         print('Current value = "%s"' % self.data)
#
# class ThirdClass(SecondClass): # Наследует SecondClass
#     def __init__(self, value): # Вызывается из ThirdClass(value)
#         self.data = value
#     def __add__(self, other): # Для выражения “self + other”
#         return ThirdClass(self.data + other)
#     def __str__(self): # Вызывается из print(self), str()
#         return '[ThirdClass: %s]' % self.data
#     def mul(self, other):  # Изменяет сам объект: обычный метод
#         self.data *= other
#
# a = FirstClass()
# a.data = 'King'
# a.anothername = "Quine"
# a.display()
# print(a.anothername)
#
# b = FirstClass()
# b.setdata(3.514)
# b.display()
# # эквивалентно
# print(FirstClass.setdata(b, 3.14159))
#
# c = SecondClass()
# c.setdata('ZZZ')
# c.display()
#
# z = ThirdClass('abc')
# z.display()
# print(z)
#
# w = z + 'xyz'
# w.display()
#
# z.mul(3)
# print(z)

    # class Cat(Animal):
    #
    #     def __init__(self):
    #         Animal.__init__(self)
    #         print('Cat was born')
    #
    #     def makeNoise(self):
    #         print(self.name,'say Mew')
    #
    # class Dog(Animal):

    # def __init__(self):
    #     Animal.__init__(self)
    #     print('Dog was born')
    #
    # def makeNoise(self):
    #     print(self.name,'say Gaw')

    # cat = Cat()
    # dog1 = Dog()
    # dog2 = Dog()



# cat.name = 'Tom'
# dog1.name = 'Ralf'
# dog2.name = 'Spot'

    # cat.makeNoise()
    # dog1.makeNoise()
    # dog2.makeNoise()
    # animal.makeNoise()
    # print(animal.name, animal.yum())
    # print(cat.name, cat.yum())
    # dog1.yum()
    # dog2.yum()



# import pygame
#
# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
#
#
# def draw_stick_figure(screen, x, y):
#     # Head
#     pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
#
#     # Legs
#     pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
#     pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
#
#     # Body
#     pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
#
#     # Arms
#     pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
#     pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
#
#
# # Setup
# pygame.init()
#
# # Set the width and height of the screen [width,height]
# size = [700, 500]
# screen = pygame.display.set_mode(size)
#
# pygame.display.set_caption("My Game")
#
# # Loop until the user clicks the close button.
# done = False
#
# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()
#
# # Hide the mouse cursor
# pygame.mouse.set_visible(0)
#
# # Speed in pixels per frame
# x_speed = 0
# y_speed = 0
#
# # Current position
# x_coord = 10
# y_coord = 10
#
# # -------- Main Program Loop -----------
# while not done:
#     # --- Event Processing
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#             # User pressed down on a key
#
#         elif event.type == pygame.KEYDOWN:
#             # Figure out if it was an arrow key. If so
#             # adjust speed.
#             if event.key == pygame.K_LEFT:
#                 x_speed = -3
#             elif event.key == pygame.K_RIGHT:
#                 x_speed = 3
#             elif event.key == pygame.K_UP:
#                 y_speed = -3
#             elif event.key == pygame.K_DOWN:
#                 y_speed = 3
#
#         # User let up on a key
#         elif event.type == pygame.KEYUP:
#             # If it is an arrow key, reset vector back to zero
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 x_speed = 0
#             elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                 y_speed = 0
#
#     # --- Game Logic
#
#     # Move the object according to the speed vector.
#     x_coord = x_coord + x_speed
#     y_coord = y_coord + y_speed
#
#     # --- Drawing Code
#
#     # First, clear the screen to WHITE. Don't put other drawing commands
#     # above this, or they will be erased with this command.
#     screen.fill(WHITE)
#
#     draw_stick_figure(screen, x_coord, y_coord)
#
#     # Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()
#
#     # Limit frames per second
#     clock.tick(60)
#
# # Close the window and quit.
# pygame.quit()
#
# class Ball:
#
#     def __init__(self, x=0, y = 0, velosity_x = 1, velosity_y = 1, radius = 10, color = (255,255,255)):
#         self.velosity_x = 0
#         self.velosity_y = 0
#         self.x = 0
#         self.y = 0
#         self.radius = 10
#         self.color = (255,255,255)
#
#     def __repr__(self):
#         return self.__dict__.__repr__()
#
#
# class Vector:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#     def __add__(self, other):
#         x = self._x + other._x
#         y = self._y + other._y
#         return (x,y)
#
#
# ball = Ball(10,10, 1,1,20,(0,0,0))
# print(ball)
import pygame
import random


class Vec2d(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # сумма двух векторов
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # разность двух векторов
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, k):  # умножение вектора на число
        return Vec2d(self.x*k, self.y*k)

    def __len__(self):  # длинна вектора
        return (self.x**2 + self.y**2)**0.5

    def scal_mul(self, other):  # скалярное умножение векторов
        product = 0
        for i, j in zip((self.x, self.y), (other.x, other.y)):
            product += i*j
        return product

    def vec(self, other):  # создание вектора по началу (x) и концу (y) направленного отрезка
        return other - self

    def int_pair(self):
        return self.x, self.y  # получение пары (tuple) целых чисел


class Polyline(object):

    def __init__(self, points=None, speeds=None, screen_dim=(800, 600)):
        self.points = points or []
        self.speeds = speeds or []
        self.screen_dim = screen_dim

    def append(self, point, speed):
        self.points.append(point)
        self.speeds.append(speed)

    def set_points(self):  # пересчёт координат точек
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > self.screen_dim[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(- self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > self.screen_dim[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):  # отрисовка ломаной
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color, (int(self.points[p_n].x), int(self.points[p_n].y)),
                                 (int(self.points[p_n + 1].x), int(self.points[p_n + 1].y)), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p.x), int(p.y)), width)


# class Knot(Polyline):
#
#     def __init__(self, points=None, count=0):
#         super().__init__()
#         self.points = points or []
#         self.count = count
#
#     def __get_point(self, points, alpha, deg=None):
#         if deg is None:
#             deg = len(points) - 1
#         if deg == 0:
#             return points[0]
#         return points[deg]*alpha + self.__get_point(points, alpha, deg - 1)*(1 - alpha)
#
#     def __get_points(self, base_points, count):
#         alpha = 1 / count
#         res = []
#         for i in range(count):
#             res.append(self.__get_point(base_points, i * alpha))
#         return res
#
#     def get_knot(self):
#         if len(self.points) < 3:
#             return []
#         res = []
#         for i in range(-2, len(self.points) - 2):
#             ptn = []
#             ptn.append((self.points[i] + self.points[i + 1])*0.5)
#             ptn.append(self.points[i + 1])
#             ptn.append((self.points[i + 1] + self.points[i + 2])*0.5)
#             res.extend(self.__get_points(ptn, self.count))
#         return res
#
#
# def draw_help():
#     gameDisplay.fill((50, 50, 50))
#     font1 = pygame.font.SysFont("courier", 24)
#     font2 = pygame.font.SysFont("serif", 24)
#     data = []
#     data.append(["F1", "Show Help"])
#     data.append(["R", "Restart"])
#     data.append(["P", "Pause/Play"])
#     data.append(["Num+", "More points"])
#     data.append(["Num-", "Less points"])
#     data.append(["", ""])
#     data.append([str(steps), "Current points"])
#
#     pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
#         (0, 0), (800, 0), (800, 600), (0, 600)], 5)
#     for i, text in enumerate(data):
#         gameDisplay.blit(font1.render(
#             text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
#         gameDisplay.blit(font2.render(
#             text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# Основная программа
if __name__ == "__main__":
    screen_dim = (500, 500)
    pygame.init()
    gameDisplay = pygame.display.set_mode(screen_dim)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    polyline = Polyline(screen_dim=screen_dim)
    # show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    polyline = Polyline(screen_dim=screen_dim)
                if event.key == pygame.K_p:
                    pause = not pause
                # if event.key == pygame.K_KP_PLUS:
                #     steps += 1
                # # if event.key == pygame.K_F1:
                # #     show_help = not show_help
                # if event.key == pygame.K_KP_MINUS:
                #     steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                polyline.append(Vec2d(event.pos[0], event.pos[1]), Vec2d(random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        # hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        polyline.draw_points()
        # knot = Knot(polyline.points, steps)
        # curve = Polyline(knot.get_knot())
        # curve.draw_points("line", 3, color)

        if not pause:
            polyline.set_points()
        # if show_help:
        #     draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)