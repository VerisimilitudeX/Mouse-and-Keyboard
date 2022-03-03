import tsk
import pygame

pygame.init()
window = pygame.display.set_mode([600, 300])

ball_speed = 5

ball = pygame.Rect(275, 0, 50, 50)

player = pygame.Rect(0, 125, 20, 50)

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    if tsk.get_key_pressed(pygame.K_LEFT):
        player.x -= 5
        
    if tsk.get_key_pressed(pygame.K_RIGHT):
        player.x += 5

    if tsk.get_key_pressed(pygame.K_UP):
        player.y -= 5

    if tsk.get_key_pressed(pygame.K_DOWN):
        player.y += 5

    ball.y += ball_speed
    
    if ball.y < 0 or ball.y > 250:
        ball_speed = ball_speed * -1

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (23, 32, 243), player)
    pygame.draw.ellipse(window, (132, 53, 24), ball)

    pygame.display.flip()
    pygame.time.wait(10)
