import pygame
import time

# Ініціалізація Pygame
pygame.init()

# Крок 1: Налаштовуємо розміри
CELL_SIZE = 25
GRID_WIDTH = 28
GRID_HEIGHT = 31
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Лабіринт Пакмена")

# Крок 2: Задаємо лабіринт із Power Pellets (P)
labyrinth = [
    "############################",
    "#P0000#00000000#000000000P##",
    "#0####0#0#####00#0####00000#",
    "#0####0#0000000000####00000#",
    "#000000#0#0##000000000#0000#",
    "#0#####0000##0#####000#0000#",
    "#0#0000000#0000000#000#0000#",
    "#0#0####00#0#####0#0###0000#",
    "#00000000000000000000000000#",
    "#0#0####00#00000#####000000#",
    "#0#####000#0##0000000#####0#",
    "#000000#0000000##0000000000#",
    "#0#####0#0#####0#0#####0000#",
    "#000000#000000000000000#000#",
    "#000000#0####0#####0#0#0000#",
    "#00000000000000000000000000#",
    "#000000#0####0#####0#0#0000#",
    "#000000#000000000000000#000#",
    "#0#####0#0#####0#0#####0000#",
    "#000000#0000000##0000000000#",
    "#0#####000#0##0000000#####0#",
    "#0#000000000000000###000000#",
    "#000000#00#00000#0000000000#",
    "#0####0#00#0###0#0####00000#",
    "#0####0#0000000000####00000#",
    "#000000#0#####00#0000000000#",
    "#0#####000000000#0#####000##",
    "#0#000#0#000#000#0000#00000#",
    "#0#0###0#0###000#0###0#0000#",
    "#P000000000000000000000000P#",
    "############################"
]

# Крок 3: Визначаємо кольори
BLACK = (0, 0, 0)    # Проходи
BLUE = (0, 0, 255)   # Стіни
YELLOW = (255, 255, 0)  # Монетки
WHITE = (255, 255, 255)  # Power Pellets

# Клас для монеток
class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, COIN_SIZE, COIN_SIZE)
    def draw(self, window):
        pygame.draw.rect(window, YELLOW, self.rect)

# Клас для Power Pellets (більші та мигаючі)
class PowerPellet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)  # Збільшений розмір до CELL_SIZE
        self.visible = True
        self.last_toggle = time.time()  # Час останнього перемикання видимості

    def draw(self, window):
        current_time = time.time()
        # Міняємо видимість кожні 0.5 секунди
        if current_time - self.last_toggle >= 0.5:
            self.visible = not self.visible
            self.last_toggle = current_time
        
        if self.visible:
            pygame.draw.circle(window, WHITE, (self.rect.centerx, self.rect.centery), CELL_SIZE // 3)

# Генерація монеток і Power Pellets
COIN_SIZE = 5
coins = []
power_pellets = []
for row in range(len(labyrinth)):
    for col in range(len(labyrinth[row])):
        if labyrinth[row][col] == "0":
            coin_x = col * CELL_SIZE + (CELL_SIZE - COIN_SIZE) // 2
            coin_y = row * CELL_SIZE + (CELL_SIZE - COIN_SIZE) // 2
            coins.append(Coin(coin_x, coin_y))
        elif labyrinth[row][col] == "P":
            pellet_x = col * CELL_SIZE  # Без зміщення, щоб заповнити клітинку
            pellet_y = row * CELL_SIZE
            power_pellets.append(PowerPellet(pellet_x, pellet_y))

# Функція для стін
def get_walls():
    walls = []
    for row in range(len(labyrinth)):
        for col in range(len(labyrinth[row])):
            if labyrinth[row][col] == "#":
                walls.append(pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    return walls

# Основний цикл (для тестування)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    WINDOW.fill(BLACK)
    
    # Малюємо стіни
    for row in range(len(labyrinth)):
        for col in range(len(labyrinth[row])):
            if labyrinth[row][col] == "#":
                pygame.draw.rect(WINDOW, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Малюємо монетки
    for coin in coins:
        coin.draw(WINDOW)
    
    # Малюємо Power Pellets із миготінням
    for pellet in power_pellets:
        pellet.draw(WINDOW)
    
    pygame.display.flip()

pygame.quit()