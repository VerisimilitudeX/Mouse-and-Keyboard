import pygame
import random
import tsk
pygame.init()

window = pygame.display.set_mode([400, 400])
points = 0
total_points = 0
icon_rect = pygame.Rect(0, 0, 100, 100)

side = random.randint(1, 4)
if side == 1:
    correct_key = pygame.K_UP
    icon_rect.x = 150
    icon_rect.y = 0
elif side == 2:
    correct_key = pygame.K_DOWN
    icon_rect.x = 150
    icon_rect.y = 300
elif side == 3:
    correct_key = pygame.K_LEFT
    icon_rect.x = 0
    icon_rect.y = 150
else:
    correct_key = pygame.K_RIGHT
    icon_rect.x = 300
    icon_rect.y = 150

drawing = True
while drawing:

    side = random.randint(1, 4)
    if side == 1:
        correct_key = pygame.K_UP
        icon_rect.x = 150
        icon_rect.y = 0
    elif side == 2:
        correct_key = pygame.K_DOWN
        icon_rect.x = 150
        icon_rect.y = 300
    elif side == 3:
        correct_key = pygame.K_LEFT
        icon_rect.x = 0
        icon_rect.y = 150
    else:
        correct_key = pygame.K_RIGHT
        icon_rect.x = 300
        icon_rect.y = 150

    guessing = True
    total_points += points
    points = 100
    while guessing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guessing = False
                drawing = False

            if event.type == pygame.KEYDOWN:

                if tsk.get_key_pressed(correct_key):
                    guessing = False
                    print(total_points)

                    print("You lost! ")
                    guessing = False

        window.fill((235, 220, 230))
        pygame.draw.rect(window, (120, 10, 40), icon_rect)
        pygame.display.flip()

        points -= 1
        if points <= 0:
            print("You ran out of time!")
            guessing = False
            drawing = False

print("Final score: " + str(total_points))
