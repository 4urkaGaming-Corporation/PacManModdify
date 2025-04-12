import pytest
import pygame
import math
from entities import Enemy
from settings import ENEMY_SPEED, ENEMY_RADIUS, VISIBILITY_RANGE

@pytest.fixture
def enemy():
    return Enemy(pos=[100, 100], color=(255, 0, 0))

@pytest.mark.parametrize("pacman_pos, distance, expected_movement", [
    ([200, 200], VISIBILITY_RANGE - 10, True),
    ([400, 400], VISIBILITY_RANGE + 10, False),
])
def test_enemy_move_to_pacman(enemy, mocker, pacman_pos, distance, expected_movement):
    mocker.patch('random.random', return_value=1.0)
    initial_pos = enemy.pos.copy()
    enemy.move(pacman_pos, walls=[])
    dx = pacman_pos[0] - initial_pos[0]
    dy = pacman_pos[1] - initial_pos[1]
    expected_distance = math.sqrt(dx**2 + dy**2)
    if expected_movement and expected_distance > 0:
        assert abs(enemy.pos[0] - initial_pos[0]) > 0 or abs(enemy.pos[1] - initial_pos[1]) > 0
    else:
        assert enemy.pos == initial_pos

def test_enemy_wall_collision(enemy, mocker):
    wall = pygame.Rect(110, 110, 25, 25)
    pacman_pos = [200, 200]
    initial_pos = enemy.pos.copy()
    enemy.move(pacman_pos, walls=[wall])
    assert enemy.pos == initial_pos

def test_enemy_random_move(enemy, mocker):
    mocker.patch('random.random', return_value=0.0)
    mocker.patch('random.choice', return_value=1)
    pacman_pos = [1000, 1000]
    initial_pos = enemy.pos.copy()
    enemy.move(pacman_pos, walls=[])
    assert enemy.pos != initial_pos

def test_enemy_get_rect(enemy):
    rect = enemy.get_rect()
    assert rect.center == (enemy.pos[0], enemy.pos[1])
    assert rect.width == ENEMY_RADIUS * 2