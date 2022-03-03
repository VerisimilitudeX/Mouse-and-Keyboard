import tsk
import random
import pygame

pygame.init()
window = pygame.display.set_mode([500, 300])

fly = pygame.Rect(100, 150, 20, 20)
box = pygame.Rect(200, 100, 100, 100)

caught = False
done = False

while not done and not caught:

    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            in_x = False
            in_y = False

            if fly.x - box.x >= 0 and fly.x - box.x <= 80:
                in_x = True

            if fly.y - box.y >= 0 and fly.y - box.y <= 80:
                in_y = True

            if in_x and in_y:
                caught = True

    fly.x += random.randint(-5, 5)
    fly.y += random.randint(-5, 5)

    if fly.x < 0:
        fly.x = 0
        
    if fly.x > 480:
        fly.x = 480
        
    if fly.y < 0:
        fly.y = 0

    if fly.y > 280:
        fly.y = 280

    if tsk.get_key_pressed(pygame.K_RIGHT):
        box.x += 2

    if tsk.get_key_pressed(pygame.K_LEFT):
        box.x -= 2

    window.fill((255, 255, 255))

    pygame.draw.rect(window, (0, 0, 0), box, 2)
    pygame.draw.ellipse(window, (23, 234, 42), fly)
    
    pygame.display.flip()
    pygame.time.wait(10)
    
if caught:
    print("Congratulations, you got it!! ")
