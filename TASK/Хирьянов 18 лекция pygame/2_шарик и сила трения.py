import pygame

width = 500
height = 500
FPS = 60
BLACK = (0, 0, 0)
colors = [
    (255, 255, 255), # 0'WHITE'
    (125, 125, 125), # 1'GRAY'
    (64, 128, 255), # 2'LIGHT_BLUE'
    (0, 200, 64), # 3'GREEN'
    (225, 225, 0), # 4'YELLOW'
    (230, 50, 230), # 5'PINK'
    (192,5,248) # 6'FIOLET'
]

x,y = 250,200
velocity_x = 1
velocity_y = 0

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
    if velocity_y == 0:
        i = colors[3]
    elif velocity_y < 0:
        i = colors[4]
    elif velocity_y > 0:
        i = colors[5]
    pygame.draw.circle(screen, i, (x,y), 20)
    x = x + velocity_x
    velocity_y -= sila
    y = y + velocity_y

    if y <= 0 or (y + 20) >= height:
        velocity_y = - velocity_y
    if x <= 0 or (x + 20) >= width:
        velocity_x = - velocity_x

    if  pygame.key.get_pressed()[pygame.K_UP]:
        velocity_y += -3
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        velocity_y += 3

    pygame.display.flip()