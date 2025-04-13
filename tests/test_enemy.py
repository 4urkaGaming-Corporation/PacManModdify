import pygame
import pytest
from entities import Enemy
from settings import RED, CELL_SIZE, ENEMY_RADIUS, ENEMY_SPEED


@pytest.fixture
def enemy(mocker):
    mocker.patch("maze.Maze.get_walls", return_value=[])
    return Enemy([100, 100], RED)


@pytest.fixture
def pacman_pos():
    return [200, 200]


@pytest.fixture
def walls():
    return [pygame.Rect(150, 150, CELL_SIZE, CELL_SIZE)]


def test_enemy_initialization(enemy):
    assert enemy.pos == [100, 100]
    assert enemy.radius == ENEMY_RADIUS
    assert enemy.speed == ENEMY_SPEED
    assert enemy.color == RED


def test_enemy_move_toward_pacman(enemy, pacman_pos, walls, mocker):
    mocker.patch("maze.Maze.get_walls", return_value=[])
    original_pos = enemy.pos.copy()
    enemy.move(pacman_pos, [])
    distance_before = (
        (original_pos[0] - pacman_pos[0])**2 +
        (original_pos[1] - pacman_pos[1])**2
    )**0.5
    distance_after = (
        (enemy.pos[0] - pacman_pos[0])**2 +
        (enemy.pos[1] - pacman_pos[1])**2
    )**0.5
    assert distance_after <= distance_before


def test_enemy_collision_with_wall(enemy, walls, mocker):
    enemy.pos = [100, 100]
    enemy.direction = [0, 0]
    original_pos = enemy.pos.copy()
    mocker.patch("random.choice", return_value=0)
    walls = [pygame.Rect(110, 110, CELL_SIZE, CELL_SIZE)]
    enemy.move([1000, 1000], walls)
    assert enemy.pos == original_pos


def test_enemy_get_rect(enemy):
    rect = enemy.get_rect()
    assert rect.width == ENEMY_RADIUS * 2
    assert rect.height == ENEMY_RADIUS * 2
    assert rect.center == (enemy.pos[0], enemy.pos[1])
