# Libraries
import pygame
import tsk
pygame.init()

# Setup
circ_x = 100
circ_y = 100

# Window
window = pygame.display.set_mode([600, 400])


# Main loop
running = True
while running:
    window.fill((255, 255, 255))
    
    # Constant motion
    if tsk.get_key_pressed(pygame.K_LEFT):
        circ_x -=2
    if tsk.get_key_pressed(pygame.K_RIGHT):
        circ_x += 2
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move per press
        if event.type == pygame.K_LEFT:
            circ_x -= 2
        if event.type == pygame.K_RIGHT:
            circ_x += 2

    pygame.draw.circle(window, (0, 0, 0), (circ_x, circ_y), 25)
    pygame.display.flip()
