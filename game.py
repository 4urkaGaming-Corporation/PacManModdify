import pygame
from settings import WIDTH, HEIGHT, INITIAL_ENEMIES, BLACK, WHITE
from entities import Pacman, Enemy
from maze import Maze


class Game:
    def __init__(self, volume):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pac Man: FunModify")
        self.clock = pygame.time.Clock()
        self.pacman = Pacman()
        self.enemies = [
            Enemy(enemy["pos"], enemy["color"])
            for enemy in INITIAL_ENEMIES
        ]
        self.maze = Maze()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.game_won = False
        self.initial_coin_count = len(self.maze.coins)
        pygame.mixer.init()
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if not self.game_over and not self.game_won:
                self.pacman.move(keys, self.maze.walls)
                for enemy in self.enemies:
                    enemy.move(self.pacman.pos, self.maze.walls)
                    if self.pacman.get_rect().colliderect(enemy.get_rect()):
                        self.game_over = True
                self.maze.coins = [
                    coin for coin in self.maze.coins
                    if not self.pacman.get_rect().colliderect(coin.rect)
                ]
                self.score = 10 * (self.initial_coin_count - len(self.maze.coins))
                if self.score >= 5000:
                    self.game_won = True

            self.window.fill(BLACK)
            self.maze.draw(self.window)
            self.pacman.draw(self.window)
            for enemy in self.enemies:
                enemy.draw(self.window)

            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.window.blit(score_text, (10, 10))

            if self.game_over:
                game_over_text = self.font.render(
                    "Game Over! Press Q to quit", True, WHITE
                )
                self.window.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
                if keys[pygame.K_q]:
                    pygame.mixer.music.stop()
                    running = False
            elif self.game_won:
                win_text = self.font.render(
                    "You Won! Press Q to quit", True, WHITE
                )
                self.window.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2))
                if keys[pygame.K_q]:
                    pygame.mixer.music.stop()
                    running = False

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game(0.5)
    game.run()
    pygame.quit()
