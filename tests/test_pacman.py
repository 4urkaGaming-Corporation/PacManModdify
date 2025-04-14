import pygame
import pytest
from entities import Pacman
from settings import CELL_SIZE, INITIAL_PACMAN_POS, PACMAN_RADIUS, PACMAN_SPEED


@pytest.fixture
def pacman():
    return Pacman()


@pytest.fixture
def walls():
    return [pygame.Rect(50, 50, CELL_SIZE, CELL_SIZE)]


def test_pacman_initial_position(pacman):
    assert pacman.pos == INITIAL_PACMAN_POS
    assert pacman.radius == PACMAN_RADIUS
    assert pacman.speed == PACMAN_SPEED


def test_pacman_move_right(pacman, walls):
    keys = {
        pygame.K_LEFT: False,
        pygame.K_RIGHT: True,
        pygame.K_UP: False,
        pygame.K_DOWN: False,
    }
    original_x = pacman.pos[0]
    pacman.move(keys, walls)
    assert pacman.pos[0] == original_x + PACMAN_SPEED


def test_pacman_move_left(pacman, walls):
    keys = {
        pygame.K_LEFT: True,
        pygame.K_RIGHT: False,
        pygame.K_UP: False,
        pygame.K_DOWN: False,
    }
    original_x = pacman.pos[0]
    pacman.move(keys, walls)
    assert pacman.pos[0] == original_x - PACMAN_SPEED


def test_pacman_move_up(pacman, walls):
    keys = {
        pygame.K_LEFT: False,
        pygame.K_RIGHT: False,
        pygame.K_UP: True,
        pygame.K_DOWN: False,
    }
    original_y = pacman.pos[1]
    pacman.move(keys, walls)
    assert pacman.pos[1] == original_y - PACMAN_SPEED


def test_pacman_move_down(pacman, walls):
    keys = {
        pygame.K_LEFT: False,
        pygame.K_RIGHT: False,
        pygame.K_UP: False,
        pygame.K_DOWN: True,
    }
    original_y = pacman.pos[1]
    pacman.move(keys, walls)
    assert pacman.pos[1] == original_y + PACMAN_SPEED


def test_pacman_collision_with_wall(pacman, walls):
    pacman.pos = [50 + PACMAN_RADIUS, 50 + PACMAN_RADIUS]
    keys = {
        pygame.K_LEFT: True,
        pygame.K_RIGHT: False,
        pygame.K_UP: False,
        pygame.K_DOWN: False,
    }
    original_pos = pacman.pos.copy()
    pacman.move(keys, walls)
    assert pacman.pos == original_pos


def test_pacman_get_rect(pacman):
    rect = pacman.get_rect()
    assert rect.width == PACMAN_RADIUS * 2
    assert rect.height == PACMAN_RADIUS * 2
    assert rect.center == (pacman.pos[0], pacman.pos[1])
