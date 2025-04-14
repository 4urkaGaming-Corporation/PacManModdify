python

Копировать
import pygame
import random
import math
import time
from settings import (
    INITIAL_PACMAN_POS, PACMAN_RADIUS, PACMAN_SPEED, WIDTH, HEIGHT, YELLOW,
    ENEMY_RADIUS, ENEMY_SPEED, VISIBILITY_RANGE, COIN_SIZE, CELL_SIZE, WHITE
)


class Pacman:
    def __init__(self):
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

        new_pos[0] = max(self.radius, min(WIDTH - self.radius, new_pos[0]))
        new_pos[1] = max(self.radius, min(HEIGHT - self.radius, new_pos[1]))

        rect = pygame.Rect(
            new_pos[0] - self.radius, new_pos[1] - self.radius,
            self.radius * 2, self.radius * 2
        )
        if not any(rect.colliderect(wall) for wall in walls):
            self.pos = new_pos

    def draw(self, window):
        pygame.draw.circle(window, YELLOW, (int(self.pos[0]), int(self.pos[1])), self.radius)

    def get_rect(self):
        return pygame.Rect(
            self.pos[0] - self.radius, self.pos[1] - self.radius,
            self.radius * 2, self.radius * 2
        )


class Enemy:
    def __init__(self, pos, color):
        self.pos = pos.copy()
        self.radius = ENEMY_RADIUS
        self.speed = ENEMY_SPEED
        self.color = color
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        from maze import Maze
        rect = self.get_rect()
        walls = Maze().walls
        while any(rect.colliderect(wall) for wall in walls):
            self.pos[0] += self.speed
            rect = self.get_rect()

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
            if random.random() < 0.05:
                self.direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]

        rect = pygame.Rect(
            new_pos[0] - self.radius, new_pos[1] - self.radius,
            self.radius * 2, self.radius * 2
        )
        if not any(rect.colliderect(wall) for wall in walls):
            self.pos = new_pos
        else:
            self.direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)

    def get_rect(self):
        return pygame.Rect(
            self.pos[0] - self.radius, self.pos[1] - self.radius,
            self.radius * 2, self.radius * 2
        )


class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, COIN_SIZE, COIN_SIZE)
        self.collected = False

    def draw(self, window):
        if not self.collected:
            pygame.draw.rect(window, YELLOW, self.rect)


class PowerPellet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        self.visible = True
        self.last_toggle = time.time()

    def draw(self, window):
        current_time = time.time()
        if current_time - self.last_toggle >= 0.5:
            self.visible = not self.visible
            self.last_toggle = current_time
        if self.visible:
            pygame.draw.circle(
                window, WHITE, (self.rect.centerx, self.rect.centery),
                CELL_SIZE // 3
            )
