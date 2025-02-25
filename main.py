import pygame
import pygame_gui
# from game import Game - в майбутньому реалізуємо файл game для логіки гри та основного циклу

# Ініциалізація Pygame
pygame.init()


# Розміри вікна
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac Man: FunModify")


# Шрифт для тексту
font = pygame.font.Font(None, 36)

# Запуск гри
if name == "main":
    game = Game()
    game.run()
    pygame.quit()


