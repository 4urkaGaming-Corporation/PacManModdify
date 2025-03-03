import pygame
import random
import math
from settings import *

#Клас пакмен
class Pacman:
    def init(self):
        self.pos = INITIAL_PACMAN_POS.copy()
        self.radius = PACMAN_RADIUS
        self.speed = PACMAN_SPEED

    def move(self, keys, walls):
        new_pos = self.pos.copy()
        if keys[pygame.K_LEFT]:
            new_pos[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            new_pos[0] += self.speed
        if keys[pygame.K_UP]:
            new_pos[1] -= self.speed
        if keys[pygame.K_DOWN]:
            new_pos[1] += self.speed

        rect = pygame.Rect(new_pos[0] - self.radius, new_pos[1] - self.radius,
                           self.radius * 2, self.radius * 2)
        if not any(rect.colliderect(wall) for wall in walls):
            self.pos = new_pos

    def draw(self, window):
        pygame.draw.circle(window, YELLOW, (int(self.pos[0]), int(self.pos[1])), self.radius)

    def get_rect(self):
        return pygame.Rect(self.pos[0] - self.radius, self.pos[1] - self.radius,
                           self.radius * 2, self.radius * 2)

class Enemy:
    def init(self, pos, color):
        self.pos = pos.copy()
        self.radius = ENEMY_RADIUS
        self.speed = ENEMY_SPEED
        self.color = color
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]

    def move(self, pacman_pos, walls):
        dx = pacman_pos[0] - self.pos[0]
        dy = pacman_pos[1] - self.pos[1]
        distance = math.sqrt(dx**2 + dy**2)
        new_pos = self.pos.copy()

        if distance < VISIBILITY_RANGE and distance > 0:
            new_pos[0] += (dx / distance) * self.speed
            new_pos[1] += (dy / distance) * self.speed
        else:
            new_pos[0] += self.direction[0] * self.speed
            new_pos[1] += self.direction[1] * self.speed
            if random.random() < 0.02:
                self.direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]

        rect = pygame.Rect(new_pos[0] - self.radius, new_pos[1] - self.radius,
                           self.radius * 2, self.radius * 2)
        if not any(rect.colliderect(wall) for wall in walls):
            self.pos = new_pos
        elif distance >= VISIBILITY_RANGE:
            self.direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)

    def get_rect(self):
        return pygame.Rect(self.pos[0] - self.radius, self.pos[1] - self.radius,
                           self.radius * 2, self.radius * 2)

class Coin:
    def init(self, x, y):
        self.rect = pygame.Rect(x, y, COIN_SIZE, COIN_SIZE)
    def draw(self, window):
        pygame.draw.rect(window, WHITE, self.rect)