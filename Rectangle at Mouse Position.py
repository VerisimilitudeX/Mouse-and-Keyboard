import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((220, 210, 200))

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Store mouse position
            x, y = pygame.mouse.get_pos()

            # Draw rectangle
            rect = pygame.Rect(x, y, 50, 50)
            pygame.draw.rect(window, (255, 255, 255), rect) 

    pygame.display.flip()
