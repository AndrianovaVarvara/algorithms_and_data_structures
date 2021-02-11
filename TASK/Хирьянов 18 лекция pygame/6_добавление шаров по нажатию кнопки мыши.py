import pygame
import random

width = 500
height = 500

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

def draw_ball(screen, x, y):
    return pygame.draw.circle(screen, RED, (x,y), 10)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

BALLS_coords = []

# Спрятать курсор мыши
# pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get(): # чтобы можно было закрыть
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = event.pos
                BALLS_coords.append(pos)
    clock.tick(20)

    # pos = pygame.mouse.get_pos()
    # BALLS_coords.append(pos)


    # Рисование
    screen.fill(BLACK)
    for i in range(len(BALLS_coords)):
        pygame.draw.circle(screen, random.choice(colors), BALLS_coords[i], 20)



    pygame.display.flip()
