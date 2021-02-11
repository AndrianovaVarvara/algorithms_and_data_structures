import pygame

width = 500
height = 500
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
PURPLE = (120, 22, 217)

x1,y1 = 150,80
x2,y2 = 270,100
velocity_x1 = 1
velocity_y1 = 2
velocity_x2 = 1
velocity_y2 = 2

sila = -1

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('VARVARA')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get(): # чтобы можно было закрыть
        if event.type == pygame.QUIT:
            quit()
    clock.tick(FPS)

    screen.fill(BLACK)

    pygame.draw.circle(screen, WHITE, (x1,y1), 50)
    pygame.draw.circle(screen, GREEN, (x2, y2), 50)

# придаем шарикам ускорение (с учетом силы тяжести)
    x1 = x1 + velocity_x1

    velocity_y1 -= sila
    y1 = y1 + velocity_y1


    x2 = x2 + velocity_x2

    velocity_y2 -= sila
    y2 = y2 + velocity_y2


# условие отскакивания от стенок
    if y1 <= 0 or (y1+velocity_y1) >= height:
        velocity_y1 = - velocity_y1
    elif y2 <= 0 or (y2+velocity_y2) >= height:
        velocity_y2 = - velocity_y2
    elif x1 <= 0 or (x1+velocity_x1) >= width:
        velocity_x1 = - velocity_x1
    elif x2 <= 0 or (x2+velocity_x2)  >= width:
        velocity_x2 = - velocity_x2
# условие ускорения при нажатии стрелочек
    if  pygame.key.get_pressed()[pygame.K_LEFT]:
        velocity_x1 +=2
        velocity_y1 +=2
    elif  pygame.key.get_pressed()[pygame.K_RIGHT]:
        velocity_x2 +=2
        velocity_y2 +=2

# соударение шаров

    if y1 == y2 + 25 or y1 == y2 - 25:
        velocity_y1 = - velocity_y1
        velocity_y2 = - velocity_y2
    if x2 == x1 + 25 or x2 == x1 - 25:
        velocity_x1 = - velocity_x1
        velocity_x2 = - velocity_x2

    pygame.display.flip()