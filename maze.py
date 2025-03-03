import pygame

# Ініціалізація Pygame
pygame.init()

# Крок 1: Налаштовуємо розміри
CELL_SIZE = 25  # Збільшений розмір клітинки
GRID_WIDTH = 28  # Збільшена ширина лабіринту
GRID_HEIGHT = 31  # Збільшена висота лабіринту
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE  # Ширина вікна = 700 пікселів
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE  # Висота вікна = 775 пікселів
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Лабіринт Пакмена")

# Крок 2: Задаємо лабіринт вручну (більший, у стилі Пакмена)
labyrinth = [
    "############################",
    "#000000#00000000#0000000000#",
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
    "#0#####000000000#0#####0000#",
    "#0#000#0#000#000#0000#00000#",
    "#0#0###0#0###000#0###0#0000#",
    "#00000000000000000000000000#",
    "############################"
]

# Крок 3: Визначаємо кольори
BLACK = (0, 0, 0)    # Проходи
BLUE = (0, 0, 255)   # Стіни
YELLOW = (255, 255, 0)  # Монетки

# Клас для монеток
class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, COIN_SIZE, COIN_SIZE)
    def draw(self, window):
        pygame.draw.rect(window, YELLOW, self.rect)

# Генерація монеток
COIN_SIZE = 5  # Уточни у товариша
coins = []
for row in range(len(labyrinth)):
    for col in range(len(labyrinth[row])):
        if labyrinth[row][col] == "0":
            coin_x = col * CELL_SIZE + (CELL_SIZE - COIN_SIZE) // 2
            coin_y = row * CELL_SIZE + (CELL_SIZE - COIN_SIZE) // 2
            coins.append(Coin(coin_x, coin_y))

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
    
    pygame.display.flip()

pygame.quit()