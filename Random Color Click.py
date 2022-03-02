# Libraries
import random
import pygame
pygame.init()

# Window
window = pygame.display.set_mode([200, 200])
window.fill((255, 255, 255))
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))
            window.fill(color)
            pygame.display.flip()
