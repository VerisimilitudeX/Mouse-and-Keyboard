import pygame
pygame.init()
window = pygame.display.set_mode([510, 510])
column = 0
position = 0
color = 0
while column < 510:
    while position < 510:
        r = pygame.Rect(column, position, 10, 10)
        pygame.draw.rect(window, (0, int(column/2), int(position/2)), r)
        position += 10
    position = 0
    column += 10
    pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            color = (0, int(x/2), int(y/2))
            print(str(color))
