import pygame

width = 500
height = 500
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
FIOLET = (192,5,248)

x,y = 250,200
direct_x = 1
direct_y = 1

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
    pygame.draw.circle(screen, PINK, (x,y), 20)
# заставляем шар двигаться (direct) и отскакивать от стенок (условие)
    x = x + direct_x
    if x + 20 >= width or x <= 0:
        direct_x = - direct_x
    y = y + direct_y
    if y + 20 >= height or y <= 0:
        direct_y = - direct_y

# придадим ускорение шарику, при помощи кнопок (СТРЕЛОЧКИ)
    if  pygame.key.get_pressed()[pygame.K_UP]:
        direct_x -=1
        direct_y -=1
    elif  pygame.key.get_pressed()[pygame.K_DOWN]:
        direct_x +=1
        direct_y +=1
    elif  pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_LEFT]:
        direct_x = 1
        direct_y = 1

    pygame.display.flip()