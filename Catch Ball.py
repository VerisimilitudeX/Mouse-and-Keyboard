import pygame
pygame.init()
window = pygame.display.set_mode([500, 300])

caught = False
done = False
ball = pygame.Rect(225, 0, 50, 50)
player = pygame.Rect(200, 280, 100, 20)

while not caught and not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            distance = player.y - ball.y
            if distance < 50 and distance > 0:
                caught = True
                
    ball.y += 5
    if ball.y > 300:
        ball.y = 0

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 255, 249), player)
    pygame.draw.ellipse(window, (255, 182, 0), ball)

    pygame.display.flip()
    pygame.time.wait(10)

if caught == True:
    print("Congratulations, you won! ")
