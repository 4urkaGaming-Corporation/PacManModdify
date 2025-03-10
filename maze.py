import pygame
import time

# Ініціалізація Pygame
pygame.init()

# Налаштування розмірів
CELL_SIZE = 25
GRID_WIDTH = 28
GRID_HEIGHT = 31
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Лабіринт Пакмена")

# Лабіринт із кліткою для привидів
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
    "#######0#0#####0#0#####0000#",
    "#000-000000000000000000#000#",  
    "#000-0000####0000000#0#0000#",
    "#000-0000000000000000000000#",  # --- - двері клітки
    "#000-0000####0#####0#0#0000#",
    "#000-000000000000000000#000#",
    "#######0#0#####0#0#####0000#",
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

# Кольори
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)  # Колір дверей

# Клас для монеток
class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, COIN_SIZE, COIN_SIZE)
    def draw(self, window):
        pygame.draw.rect(window, YELLOW, self.rect)

# Клас для Power Pellets
class PowerPellet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        self.visible = True
        self.last_toggle = time.time()
    def draw(self, window):
        current_time = time.time()
        if current_time - self.last_toggle >= 0.5:
            self.visible = not self.visible
            self.last_toggle = current_time
        if self.visible:
            pygame.draw.circle(window, WHITE, (self.rect.centerx, self.rect.centery), CELL_SIZE // 3)

# Генерація об'єктів
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
            pellet_x = col * CELL_SIZE
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

# Основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    WINDOW.fill(BLACK)
    
    # Малюємо стіни та двері
    for row in range(len(labyrinth)):
        for col in range(len(labyrinth[row])):
            if labyrinth[row][col] == "#":
                pygame.draw.rect(WINDOW, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif labyrinth[row][col] == "-":  # Двері клітки
                pygame.draw.rect(WINDOW, GRAY, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Малюємо монетки
    for coin in coins:
        coin.draw(WINDOW)
    
    # Малюємо Power Pellets
    for pellet in power_pellets:
        pellet.draw(WINDOW)
    
    pygame.display.flip()

pygame.quit()