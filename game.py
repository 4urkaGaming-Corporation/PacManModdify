import pygame
from settings import WIDTH, HEIGHT, YELLOW, WHITE, INITIAL_ENEMIES
from entities import Pacman, Enemy
from maze import Maze


class Game:
    def __init__(self, volume):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pac Man: FunModify")
        self.clock = pygame.time.Clock()
        self.score = 0
        self.game_over = False
        self.game_won = False
        self.pacman = Pacman()
        self.enemies = [Enemy(enemy["pos"], enemy["color"]) for enemy in INITIAL_ENEMIES]
        self.maze = Maze()
        self.initial_coin_count = len(self.maze.coins)
        pygame.mixer.init()
        pygame.mixer.music.load("game_song.mp3")
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        self.font = pygame.font.Font(None, 36)

    def check_collisions(self):
        # Перевірка колізії пекмена з ворогами
        pacman_rect = self.pacman.get_rect()
        for enemy in self.enemies:
            enemy_rect = enemy.get_rect()
            if pacman_rect.colliderect(enemy_rect):
                self.game_over = True
                return
        # Перевірка колізії пекмена з монетами
        for coin in self.maze.coins:
            if not coin.collected and pacman_rect.colliderect(coin.rect):
                coin.collected = True
                self.score += 10

    def check_win_condition(self):
        if self.score >= 5000:
            self.game_won = True

    def run(self):
        while not self.game_over and not self.game_won:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_over = True

            keys = pygame.key.get_pressed()
            self.pacman.move(keys, self.maze.walls)
            for enemy in self.enemies:
                enemy.move(self.pacman.pos, self.maze.walls)

            self.check_collisions()
            self.check_win_condition()

            self.window.fill((0, 0, 0))
            self.maze.draw(self.window)
            self.pacman.draw(self.window)
            for enemy in self.enemies:
                enemy.draw(self.window)

            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.window.blit(score_text, (10, 10))

            if self.game_over:
                game_over_text = self.font.render("Game Over!", True, YELLOW)
                self.window.blit(
                    game_over_text,
                    (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2)
                )
            elif self.game_won:
                game_won_text = self.font.render("You Won!", True, YELLOW)
                self.window.blit(
                    game_won_text,
                    (WIDTH // 2 - game_won_text.get_width() // 2, HEIGHT // 2)
                )

            pygame.display.flip()
            self.clock.tick(60)

        pygame.mixer.music.stop()
