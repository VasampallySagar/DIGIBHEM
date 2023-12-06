import pygame
import random


pygame.init()

WIDTH, HEIGHT = 800, 800
SNAKE_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FONT = pygame.font.Font(None, 36)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def display_text(text, color, x, y):
    text_surface = FONT.render(text, True, color)
    win.blit(text_surface, (x, y))

snake = [(WIDTH // 2, HEIGHT // 2)]
direction = 'RIGHT'

food = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
        random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

score = 0

x_change = 0
y_change = 0


playing = True
game_over = False

while playing:
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        if direction == 'UP':
            y_change = -SNAKE_SIZE
            x_change = 0
        elif direction == 'DOWN':
            y_change = SNAKE_SIZE
            x_change = 0
        elif direction == 'LEFT':
            x_change = -SNAKE_SIZE
            y_change = 0
        elif direction == 'RIGHT':
            x_change = SNAKE_SIZE
            y_change = 0

        new_head = (snake[0][0] + x_change, snake[0][1] + y_change)
        snake.insert(0, new_head)

        if snake[0] == food:
            food = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                    random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
            score += 1
        else:
            snake.pop()

        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
                snake[0][1] < 0 or snake[0][1] >= HEIGHT or
                snake[0] in snake[1:]):
            game_over = True

        win.fill(WHITE)
        pygame.draw.rect(win, RED, (*food, SNAKE_SIZE, SNAKE_SIZE))
        for segment in snake:
            pygame.draw.rect(win, GREEN, (*segment, SNAKE_SIZE, SNAKE_SIZE))

        display_text(f"Score: {score}", GREEN, 10, 10)
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

    win.fill(WHITE)
    display_text("Game Over", RED, WIDTH // 2 - 80, HEIGHT // 2 - 30)
    display_text(f"Your Score: {score}", GREEN, WIDTH // 2 - 90, HEIGHT // 2 + 10)
    display_text("Press SPACE to Play Again", RED, WIDTH // 2 - 140, HEIGHT // 2 + 50)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                snake = [(WIDTH // 2, HEIGHT // 2)]
                direction = 'RIGHT'
                food = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                        random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
                score = 0
                game_over = False

pygame.quit()
