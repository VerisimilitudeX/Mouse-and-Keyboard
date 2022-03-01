import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([800, 600])

bg_color = (30, 190, 30)
track_color = (120, 110, 110)
outline_color = (220, 220, 220)

car_rect = pygame.Rect(350, 80, 40, 30)
track_rect = pygame.Rect(50, 50, 700, 500)
inner_rect = pygame.Rect(150, 150, 500, 300)

# --- Main loop --- #
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # --- Character Movement --- #
    if tsk.get_key_pressed(pygame.K_LEFT):
        car_rect.x -= 12
    if tsk.get_key_pressed(pygame.K_RIGHT):
        car_rect.x += 12
    if tsk.get_key_pressed(pygame.K_UP):
        car_rect.y -= 12
    if tsk.get_key_pressed(pygame.K_DOWN):
        car_rect.y += 12

    # --- Draw --- #
    window.fill(bg_color)
    pygame.draw.ellipse(window, track_color, track_rect)
    pygame.draw.ellipse(window, outline_color, track_rect, 5)
    pygame.draw.ellipse(window, bg_color, inner_rect)
    pygame.draw.ellipse(window, outline_color, inner_rect, 5)
    pygame.draw.line(window, outline_color, (400, 50), (400, 150), 10)
    pygame.draw.ellipse(window, (230, 0, 20), car_rect)
    pygame.draw.ellipse(window, (20, 0, 0), car_rect, 3)
    pygame.display.flip()
