import pygame
import sys

# Inicializace Pygame
pygame.init()

# Velikost okna
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Barvy
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Rychlost pohybu čtverce
SQUARE_SPEED = 5

# Pozice čtverce
square_x = WIDTH // 2
square_y = HEIGHT // 2

# Velikost čtverce
SQUARE_SIZE = 50

# Vytvoření okna
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Primitivní Pygame Hra")

# Hlavní herní smyčka
running = True
while running:
    # Pro každou událost v Pygame
    for event in pygame.event.get():
        # Pokud uživatel klikne na křížek okna, ukončíme hru
        if event.type == pygame.QUIT:
            running = False

    # Získání stisknutých kláves
    keys = pygame.key.get_pressed()
    # Pohyb čtverce
    if keys[pygame.K_LEFT]:
        square_x -= SQUARE_SPEED
    if keys[pygame.K_RIGHT]:
        square_x += SQUARE_SPEED
    if keys[pygame.K_UP]:
        square_y -= SQUARE_SPEED
    if keys[pygame.K_DOWN]:
        square_y += SQUARE_SPEED

    # Ohraničení hranic okna
    square_x = max(0, min(square_x, WIDTH - SQUARE_SIZE))
    square_y = max(0, min(square_y, HEIGHT - SQUARE_SIZE))

    # Vykreslení pozadí
    window.fill(WHITE)
    # Vykreslení čtverce
    pygame.draw.rect(window, BLUE, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))

    # Aktualizace obrazovky
    pygame.display.update()

    # Omezení počtu snímků za sekundu
    pygame.time.Clock().tick(60)

# Ukončení Pygame
pygame.quit()
sys.exit()
