import pygame

width = 900
height = 300
FPS = 60
x = 50
y = 250
speed = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
clock = pygame.time.Clock()
isJump = False
jumpCount = 10

while True:
    for event in pygame.event.get(): # чтобы можно было закрыть
        if event.type == pygame.QUIT:
            quit()

    clock.tick(FPS)

    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (x, y), 50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 50:
        x -=speed
    elif keys[pygame.K_RIGHT] and x < width - 50:
        x +=speed

    if not(isJump):
        if keys[pygame.K_UP] and y > 50:
            y -= speed
        elif keys[pygame.K_DOWN] and y < height - 50:
            y +=speed
        elif keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0: # наивысшая точка прыжка
                y += (jumpCount ** 2) // 2

            else:
                y -= (jumpCount ** 2) //2

            jumpCount -= 1
            if x < width:
                x += 10
            else:
                x -= (x+10) - width
        else: # прыжок завершен
            isJump = False
            jumpCount = 10

    pygame.display.flip()