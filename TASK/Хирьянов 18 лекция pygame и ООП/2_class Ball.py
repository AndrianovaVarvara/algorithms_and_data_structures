import pygame
import random

class Vector:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def intpair(self):
        return self.x, self.y


class Ball:
    def __init__(self, coords=None, speeds=None, screen=((500, 500))):
        self.coords = coords or []
        self.speeds = speeds or []
        self.screen = screen


    def append(self, coord, speed):
        self.coords.append(coord)
        self.speeds.append(speed)

    def update(self):  # пересчёт координат точек
        for i in range(len(self.coords)):
            self.coords[i] = self.coords[i] + self.speeds[i]
            if self.coords[i].x > self.screen[0] or self.coords[i].x < 0:
                self.speeds[i] = Vector(- self.speeds[i].x, self.speeds[i].y)
            if self.coords[i].y > self.screen[1] or self.coords[i].y < 0:
                self.speeds[i] = Vector(self.speeds[i].x, -self.speeds[i].y)

    def draw(self):  # отрисовка ломаной
        for p in self.coords:
            pygame.draw.circle(screen, BALL_COLOR, (int(p.x), int(p.y)), BALL_SIZE)

width = 500
height = 500

BLACK = (0, 0, 0)
BALL_COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
BALL_SIZE = random.randint(10,30)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
ball=Ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ball.append(Vector(event.pos[0], event.pos[1]), Vector(random.randint(-3,3), random.randint(-3,3)))

    clock.tick(60)

    screen.fill(BLACK)

    ball.draw()

    ball.update()

    pygame.display.flip()
