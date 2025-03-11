from main import WIDTH, HEIGHT
# Кольори
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 105, 180)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
# Параметри Пекмена
PACMAN_RADIUS = 15
PACMAN_SPEED = 5
INITIAL_PACMAN_POS = [WIDTH // 2 - 50, HEIGHT // 2]
# Параметри ворогів
ENEMY_RADIUS = 15
ENEMY_SPEED = 3
VISIBILITY_RANGE = 200
INITIAL_ENEMIES = [
    {"pos": [50, 50], "color": RED},
    {"pos": [750, 50], "color": PINK},
    {"pos": [50, 550], "color": CYAN},
    {"pos": [750, 550], "color": ORANGE}
]

COIN_COUNT = 30
COIN_SIZE = 10