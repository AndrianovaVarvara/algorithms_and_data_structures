import pygame
import random

width = 500
height = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

snow_list = []
for i in range(50):
    x=random.randrange(0,width)
    y=random.randrange(0,height)
    snow_list.append([x,y])

while 1:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #
    screen.fill(BLACK)

    for i in range(len(snow_list)):
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)

        # Move the snow flake down one pixel
        snow_list[i][1] += 1

        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > height:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, width)
            snow_list[i][0] = x

    pygame.display.update()
