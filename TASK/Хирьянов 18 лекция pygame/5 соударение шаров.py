import pygame

width = 500
height = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 64)
PINK = (230, 50, 230)

velocity_x1 = 1
velocity_y1 = 2
velocity_x2 = 1
velocity_y2 = 2

# Текущая позиция
x1 = 10
y1 = 10
x2 = 400
y2 = 10

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get(): # чтобы можно было закрыть
        if event.type == pygame.QUIT:
            quit()

    clock.tick(60)

    # заставим шары двигаться
    x1 = x1 + velocity_x1
    y1 = y1 + velocity_y1
    x2 = x2 + velocity_x2
    y2 = y2 + velocity_y2

    # отскакивание от стенок
    if y1 <= 0 or (y1+velocity_y1) >= height:
        velocity_y1 = - velocity_y1
    elif y2 <= 0 or (y2+velocity_y2) >= height:
        velocity_y2 = - velocity_y2
    elif x1 <= 0 or (x1+velocity_x1) >= width:
        velocity_x1 = - velocity_x1
    elif x2 <= 0 or (x2+velocity_x2)  >= width:
        velocity_x2 = - velocity_x2

    # заставим их отскакивать еще и друг от друга
    if abs(x1 - x2) <= 20:
        velocity_x1 = velocity_x1 * (-1)
        velocity_x2 = velocity_x2 * (-1)


    screen.fill(BLACK)

    pygame.draw.circle(screen, WHITE, (x1,y1), 10)
    pygame.draw.circle(screen, GREEN, (x2, y2), 10)



    pygame.display.flip()