import pygame
from settings import *

class Game:
    def init(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Пекмен с умными призраками")
        self.clock = pygame.time.Clock()
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
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.window.blit(score_text, (10, 10))
            pygame.display.flip()
            self.clock.tick(60)