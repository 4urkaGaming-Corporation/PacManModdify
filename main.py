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



# Завантаження зображення для фону
background = pygame.image.load("background.jpg")  # Картинка фону
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Масштабування під екран


# Шрифт для тексту
font = pygame.font.Font(None, 36)



# Функція для малювання кнопок
def draw_button(text, x, y, width, height, color, text_color):
    pygame.draw.rect(window, color, (x, y, width, height))
    label = font.render(text, True, text_color)
    window.blit(label, (x + (width - label.get_width()) // 2, y + (height - label.get_height()) // 2))


# Функція головного меню
def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Перевірка натискання на кнопку "Start"
                if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 250:
                    game = Game()
                    game.run()
                    return
                # Перевірка натискання на кнопку "Info"
                if 300 <= mouse_x <= 500 and 300 <= mouse_y <= 350:
                    show_info()



        # Малювання меню
        window.blit(background, (0, 0))  # Встановлення фону
        draw_button("Start", 300, 200, 200, 50, (0, 0, 255), (255, 255, 255))
        draw_button("Info", 300, 300, 200, 50, (0, 255, 0), (255, 255, 255))
        
        pygame.display.flip()

# Функція для відображення інформації
def show_info():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Вихід з інформаційного вікна
                    return
        
        # Малювання екрану інформації
        window.blit(background, (0, 0))  # Встановлення фону
        info_lines = [
            "Це фанова модифікація легендарної гри Pac-Man",
            "Розробники:",
            "Старостин Максим",
            "Возненко Богдан",
            "Науменко Данило",
            "Тимошенко Олександр"
        ]

        start_y = HEIGHT // 2 - 100  # Початкова координата Y

        for i, line in enumerate(info_lines):
            text_surface = font.render(line, True, (0, 0, 255))
            window.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, start_y + i * 30))

        back_text = font.render("Натисніть ESC, щоб повернутися назад", True, (0, 255, 0))
        window.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, start_y + len(info_lines) * 30 + 20))

        pygame.display.flip()



# Запуск гри
if __name__ == "__main__":
    main_menu()
    pygame.quit()






