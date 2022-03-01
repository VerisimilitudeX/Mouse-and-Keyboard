import pygame
import random
pygame.init()

window = pygame.display.set_mode([512, 512])

drawing = True
while drawing:

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    window.fill(color)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Store color
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            # Print values
            print(r, g, b)

            # Pause until user hits enter
            input("Press enter to continue...")

    pygame.time.wait(500)
