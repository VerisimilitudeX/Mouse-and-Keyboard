import pygame
import tsk

pygame.init()

window = pygame.display.set_mode([400, 400])

background_color = (0, 0, 0)
number_color = (50, 255, 60)

window.fill(background_color)

# --- Main loop --- #
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.KEYDOWN:
            window.fill(background_color)
            
            if tsk.get_key_pressed(pygame.K_0):
                zero = pygame.Rect(150, 200, 80, 100)
                pygame.draw.ellipse(window, number_color, zero, 5)

            elif tsk.get_key_pressed(pygame.K_1):
                one = pygame.Rect(150, 200, 20, 100)
                pygame.draw.rect(window, number_color, one, 5)

    pygame.display.flip()
