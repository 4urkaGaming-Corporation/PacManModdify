# Константи гри
WIDTH = 700
HEIGHT = 775
CELL_SIZE = 25
GRID_WIDTH = 28
GRID_HEIGHT = 31


# Кольори
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 105, 180)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
GRAY = (150, 150, 150)


# Параметри Pacman
PACMAN_RADIUS = 10
PACMAN_SPEED = 2
INITIAL_PACMAN_POS = [CELL_SIZE * 5, CELL_SIZE * 20]  # (350, 575)


# Параметри ворогів
ENEMY_RADIUS = 10
ENEMY_SPEED = 2
VISIBILITY_RANGE = 250
INITIAL_ENEMIES = [
    {"pos": [CELL_SIZE * 26, CELL_SIZE * 29], "color": RED},  # (25, 25)
    {"pos": [CELL_SIZE * 26, CELL_SIZE * 29], "color": PINK},  # (650, 25)
    {"pos": [CELL_SIZE * 26, CELL_SIZE * 29], "color": CYAN},  # (25, 725)
    {"pos": [CELL_SIZE * 26, CELL_SIZE * 29], "color": ORANGE},  # (650, 725)
]


# Параметри монет
COIN_SIZE = 5
COIN_COUNT = 30
