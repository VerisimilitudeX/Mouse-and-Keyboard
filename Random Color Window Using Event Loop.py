# Libraries
import random
import pygame
pygame.init()

# random color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

color = (r, g, b)

# Window
window = pygame.display.set_mode([200, 200])

# Main loop
running = True
while running:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Fill the window with color
    window.fill(color)
    pygame.display.flip()
