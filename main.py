import pygame
from settings import *
from game import Game

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac Man: FunModify")

font = pygame.font.Font(None, 36)

background_image = pygame.image.load("background.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

pygame.mixer.init()
pygame.mixer.music.load("menu_song.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

def draw_button(text, x, y, width, height, color, text_color):
    pygame.draw.rect(window, color, (x, y, width, height))
    label = font.render(text, True, text_color)
    window.blit(label, (x + (width - label.get_width()) // 2, y + (height - label.get_height()) // 2))
    return (x, y, width, height)

def settings_menu():
    global volume 
    running = True
    volume = pygame.mixer.music.get_volume()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 200 <= mouse_x <= 300 and 300 <= mouse_y <= 350:
                    volume = min(1.0, volume + 0.1)
                    pygame.mixer.music.set_volume(volume)
                if 400 <= mouse_x <= 500 and 300 <= mouse_y <= 350:
                    volume = max(0.0, volume - 0.1)
                    pygame.mixer.music.set_volume(volume)

        window.blit(background_image, (0, 0))
        volume_text = font.render(f"Music Volume: {int(volume * 100)}%", True, WHITE)
        window.blit(volume_text, (WIDTH // 2 - volume_text.get_width() // 2, 200))
        draw_button("+", 200, 300, 100, 50, BLUE, WHITE)
        draw_button("-", 400, 300, 100, 50, BLUE, WHITE)
        back_text = font.render("Press ESC to return", True, (0, 255, 0))
        window.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, 400))
        pygame.display.flip()

def main_menu():
    global volume
    running = True
    start_button_rect = (250, 250, 200, 50)
    info_button_rect = (250, 350, 200, 50)
    settings_button_rect = (250, 450, 200, 50)
    volume = 0.5 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                x, y, w, h = start_button_rect
                if x <= mouse_x <= x + w and y <= mouse_y <= y + h:
                    pygame.mixer.music.stop()
                    game = Game(volume) 
                    game.run()
                    pygame.mixer.music.load("menu_song.mp3")
                    pygame.mixer.music.set_volume(volume)
                    pygame.mixer.music.play(-1)
                    return
                x, y, w, h = info_button_rect
                if x <= mouse_x <= x + w and y <= mouse_y <= y + h:
                    show_info()
                x, y, w, h = settings_button_rect
                if x <= mouse_x <= x + w and y <= mouse_y <= y + h:
                    settings_menu()

        window.blit(background_image, (0, 0))
        start_button_rect = draw_button("Start", 250, 250, 200, 50, BLUE, WHITE)
        info_button_rect = draw_button("Info", 250, 350, 200, 50, (0, 255, 0), WHITE)
        settings_button_rect = draw_button("Settings", 250, 450, 200, 50, BLACK, WHITE)
        pygame.display.flip()

def show_info():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        window.blit(background_image, (0, 0))
        info_lines = [
            "Це фанова модифікація легендарної гри Pac-Man",
            "Розробники:",
            "Старостин Максим",
            "Возненко Богдан",
            "Науменко Данило",
            "Тимошенко Олександр"
        ]
        start_y = HEIGHT // 2 - 100
        for i, line in enumerate(info_lines):
            text_surface = font.render(line, True, BLUE)
            window.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, start_y + i * 30))
        back_text = font.render("Натисніть ESC, щоб повернутися назад", True, (0, 255, 0))
        window.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, start_y + len(info_lines) * 30 + 20))
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
    pygame.quit()