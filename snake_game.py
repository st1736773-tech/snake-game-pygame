import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# -------------------- SCREEN --------------------
WIDTH, HEIGHT = 900, 500
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# -------------------- COLORS --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)


# -------------------- FUNCTIONS --------------------
def start_screen():
    while True:
        gameWindow.fill((200, 240, 200))
        title = font.render("SNAKE GAME", True, BLACK)
        msg = font.render("Press ENTER to Start", True, BLACK)

        gameWindow.blit(title, (360, 200))
        gameWindow.blit(msg, (320, 260))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # 👈 ENTER WORKS HERE


def show_score(score):
    text = font.render(f"Score : {score}", True, BLACK)
    gameWindow.blit(text, (10, 10))


def game_over_screen(score):
    while True:
        gameWindow.fill(WHITE)
        over = font.render("GAME OVER", True, RED)
        scr = font.render(f"Score : {score}", True, BLACK)
        msg = font.render("Press ENTER to Restart", True, BLACK)

        gameWindow.blit(over, (380, 200))
        gameWindow.blit(scr, (390, 240))
        gameWindow.blit(msg, (310, 280))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return


# -------------------- GAME START --------------------
while True:

    start_screen()  # 👈 START MENU

    # Game variables
    snake_x = 100
    snake_y = 100
    snake_size = 10
    velocity_x = 0
    velocity_y = 0

    food_x = random.randrange(20, WIDTH - 20, 10)
    food_y = random.randrange(20, HEIGHT - 20, 10)

    snake_list = []
    snake_length = 1
    score = 0
    fps = 25

    exit_game = False

    # -------------------- GAME LOOP --------------------
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = 10
                    velocity_y = 0
                if event.key == pygame.K_LEFT:
                    velocity_x = -10
                    velocity_y = 0
                if event.key == pygame.K_UP:
                    velocity_y = -10
                    velocity_x = 0
                if event.key == pygame.K_DOWN:
                    velocity_y = 10
                    velocity_x = 0

        snake_x += velocity_x
        snake_y += velocity_y

        # Eat food
        if snake_x == food_x and snake_y == food_y:
            score += 10
            food_x = random.randrange(20, WIDTH - 20, 10)
            food_y = random.randrange(20, HEIGHT - 20, 10)
            snake_length += 5

        gameWindow.fill(WHITE)
        pygame.draw.rect(gameWindow, RED, [food_x, food_y, snake_size, snake_size])

        head = [snake_x, snake_y]
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Collision with self
        if head in snake_list[:-1]:
            game_over_screen(score)
            exit_game = True

        # Collision with wall
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            game_over_screen(score)
            exit_game = True

        for block in snake_list:
            pygame.draw.rect(gameWindow, GREEN, [block[0], block[1], snake_size, snake_size])

        show_score(score)
        pygame.display.update()
        clock.tick(fps)
