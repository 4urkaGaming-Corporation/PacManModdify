import pygame
# from game import Game - в майбутньому реалізуємо файл game для логіки гри та основного циклу

# Инициализация Pygame
pygame.init()

# Запуск гри
if name == "main":
    game = Game()
    game.run()
    pygame.quit()