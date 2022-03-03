import pygame
pygame.init()
window = pygame.display.set_mode([500, 300])

pygame.mouse.set_visible(False)
cursor_size = 10
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cursor_size = 20
        elif event.type == pygame.MOUSEBUTTONUP:
            cursor_size = 10

    x, y = pygame.mouse.get_pos()

    window.fill((0, 0, 0)) # black on purpose, dark mode looks better
    pygame.draw.circle(window, (255, 0, 0), (x, y), cursor_size)
    pygame.display.flip()
