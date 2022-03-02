import pygame
import random
pygame.init()

window = pygame.display.set_mode([400, 400])

moon_color = (random.randint(200, 255), random.randint(180, 240), random.randint(80, 180))
corona_color = (random.randint(100, 150), random.randint(20, 80), random.randint(60, 90))

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            moon_color = (random.randint(160, 255), random.randint(80, 180), random.randint(0, 100))
            corona_color = (random.randint(100, 150), random.randint(20, 80), random.randint(60, 90))
    x, y = pygame.mouse.get_pos()

    window.fill((20, 30, 60))

    pygame.draw.circle(window, corona_color, (x, y), 60)

    pygame.draw.circle(window, moon_color, (x, y), 50)

    ground_rect = pygame.Rect(0, 250, 400, 150)
    pygame.draw.rect(window, (70, 60, 70), ground_rect)
    pygame.draw.polygon(window, (60, 75, 95), [(50, 250), (50, 50), (100, 50), (100, 100), (175, 100), (175, 50), (225, 50), (225, 100), (300, 100), (300, 50), (350, 50), (350, 250)])
    door_rect = pygame.Rect(150, 170, 100, 80)
    pygame.draw.rect(window, (65, 45, 40), door_rect)

    pygame.display.flip()
    pygame.time.wait(50)
