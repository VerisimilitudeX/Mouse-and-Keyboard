import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])

ufo_color = (60, 65, 70)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    x, y = pygame.mouse.get_pos()
    rectangle = pygame.Rect(x, y, 80, 50)

    rectangle.x -= int(80 / 2)
    rectangle.y -= int(50 / 2)

    window.fill((0, 15, 30))
    pygame.draw.ellipse(window, ufo_color, rectangle)

    pygame.display.flip()
