import pygame
from settings import *
from entities import Pacman, Enemy
from maze import Maze

class Game:
    def init(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Пекмен с умными призраками")
        self.clock = pygame.time.Clock()
        self.pacman = Pacman()
        self.enemies = [Enemy(enemy["pos"], enemy["color"]) for enemy in INITIAL_ENEMIES]
        self.maze = Maze()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill(BLACK)
            self.maze.draw(self.window)
            self.pacman.draw(self.window)
            for enemy in self.enemies:
                enemy.draw(self.window)

            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.window.blit(score_text, (10, 10))
            pygame.display.flip()
            self.clock.tick(60)