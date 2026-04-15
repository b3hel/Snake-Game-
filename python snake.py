import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


snake = [(300, 200), (280, 200), (260, 200)]
dx = 20
dy = 0


food = (random.randrange(0, 600, 20), random.randrange(0, 400, 20))

score = 0

font = pygame.font.SysFont(None, 30)

running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx = -20
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = 20
                dy = 0
            elif event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -20
            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = 20

    
    head = (snake[0][0] + dx, snake[0][1] + dy)

    
    if head[0] < 0 or head[0] >= 600 or head[1] < 0 or head[1] >= 400:
        print("Game Over! Score:", score)
        break

    
    if head in snake:
        print("Game Over! Score:", score)
        break

    snake.insert(0, head)

    
    if head == food:
        score += 1
        food = (random.randrange(0, 600, 20), random.randrange(0, 400, 20))
    else:
        snake.pop()

    
    screen.fill((0, 0, 0))

    
    for block in snake:
        pygame.draw.rect(screen, (0, 255, 0), (block[0], block[1], 20, 20))

    
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 20, 20))

    
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()