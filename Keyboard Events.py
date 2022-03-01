# Libraries
import random
import pygame
pygame.init()

# Setup
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

# Window
window = pygame.display.set_mode([200, 200])
window.fill((r, g, b))
pygame.display.flip()

# Main loop
running = True
while running:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            print("Key released " )
        elif event.type == pygame.KEYDOWN:
            print("Key pressed " )
