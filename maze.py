import pygame

# Ініціалізація Pygame
pygame.init()

# Крок 1: Налаштовуємо розміри
CELL_SIZE = 40  # Розмір клітинки
GRID_WIDTH = 10  # Ширина лабіринту
GRID_HEIGHT = 10  # Висота лабіринту
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE  # Ширина вікна
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE  # Висота вікна
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Лабіринт Пакмена")  # Заголовок вікна

# Крок 2: Задаємо лабіринт вручну
labyrinth = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "0", "0", "#", "0", "#", "0", "0", "#", "0"],
    ["#", "#", "0", "#", "0", "#", "#", "0", "#", "#"],
    ["0", "0", "0", "0", "#", "0", "0", "0", "0", "#"],
    ["#", "#", "0", "#", "#", "0", "#", "#", "0", "#"],
    ["#", "0", "0", "0", "0", "#", "0", "#", "0", "0"],
    ["#", "0", "#", "#", "0", "0", "0", "0", "#", "#"],
    ["0", "#", "0", "#", "#", "0", "#", "0", "0", "#"],
    ["#", "0", "0", "0", "#", "0", "0", "#", "0", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

# Крок 3: Визначаємо кольори та цикл
BLACK = (0, 0, 0)    # Проходи
BLUE = (0, 0, 255)   # Стіни
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Очищення екрана (чорний фон для проходів)
    WINDOW.fill(BLACK)
    
    # Крок 4: Малюємо стіни синім
    for row in range(len(labyrinth)):
        for col in range(len(labyrinth[row])):
            if labyrinth[row][col] == "#":  # Стіни малюємо синім
                pygame.draw.rect(WINDOW, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Оновлюємо екран
    pygame.display.flip()

# Завершення
pygame.quit()