import pygame
import sys

pygame.init()

# =========================
# MAPA
# =========================
WIDTH, HEIGHT = 2000, 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TRON")

clock = pygame.time.Clock()

CELL = 1
SPEED = 4

BLACK = (0, 0, 0)
BLUE = (0, 180, 255)
RED = (255, 60, 60)

font_big = pygame.font.SysFont("Arial", 120, bold=True)
font_med = pygame.font.SysFont("Arial", 60)

# =========================
# NEON TEXT
# =========================
def neon(text, font, x, y, color):
    base = font.render(text, True, color)

    for i in range(6, 0, -1):
        glow = font.render(text, True, color)
        glow.set_alpha(20 * i)
        screen.blit(glow, (x - i*2, y - i*2))

    screen.blit(base, (x, y))

# =========================
# DRAW
# =========================
def draw_block(color, pos):
    pygame.draw.rect(screen, color, (pos[0], pos[1], CELL, CELL))

# =========================
# MOVE + COLLISION
# =========================
def move(player, direction):
    head = player[-1][:]
    head[0] += direction[0]
    head[1] += direction[1]
    player.append(head)
    return head

def out(pos):
    x, y = pos
    return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT

def hit(pos, body):
    return pos in body[:-1]

# =========================
# MENU
# =========================
def menu():
    while True:
        screen.fill(BLACK)

        neon("TRON", font_big, WIDTH//2 - 200, HEIGHT//3, BLUE)
        neon("Start (Enter)", font_med, WIDTH//2 - 160, HEIGHT//2, RED)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return

# =========================
# GAME OVER SCREEN
# =========================
def game_over():
    while True:
        screen.fill(BLACK)

        neon("TRON", font_big, WIDTH//2 - 200, 100, BLUE)
        neon("GAME OVER", font_big, WIDTH//2 - 350, HEIGHT//3, RED)
        neon("R = Restart", font_med, WIDTH//2 - 150, HEIGHT//2, BLUE)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    return

# =========================
# GAME
# =========================
def game():
    p1 = [[300, 600]]
    p2 = [[1700, 600]]

    d1 = [CELL, 0]
    d2 = [-CELL, 0]

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # PLAYER 1
        if keys[pygame.K_w] and d1 != [0, CELL]:
            d1 = [0, -CELL]
        if keys[pygame.K_s] and d1 != [0, -CELL]:
            d1 = [0, CELL]
        if keys[pygame.K_a] and d1 != [CELL, 0]:
            d1 = [-CELL, 0]
        if keys[pygame.K_d] and d1 != [-CELL, 0]:
            d1 = [CELL, 0]

        # PLAYER 2
        if keys[pygame.K_UP] and d2 != [0, CELL]:
            d2 = [0, -CELL]
        if keys[pygame.K_DOWN] and d2 != [0, -CELL]:
            d2 = [0, CELL]
        if keys[pygame.K_LEFT] and d2 != [CELL, 0]:
            d2 = [-CELL, 0]
        if keys[pygame.K_RIGHT] and d2 != [-CELL, 0]:
            d2 = [CELL, 0]

        # MOVE
        for _ in range(SPEED):
            h1 = move(p1, d1)
            h2 = move(p2, d2)

            # 💀 GAME OVER
            if (
                out(h1) or hit(h1, p1) or hit(h1, p2) or
                out(h2) or hit(h2, p2) or hit(h2, p1)
            ):
                game_over()
                return

        # DRAW
        for b in p1:
            draw_block(BLUE, b)

        for b in p2:
            draw_block(RED, b)

        pygame.display.flip()

# =========================
# LOOP
# =========================
while True:
    menu()
    game()

pygame.quit()
sys.exit()
