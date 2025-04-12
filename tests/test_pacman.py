import pytest
import pygame
from entities import Pacman
from settings import WIDTH, HEIGHT, PACMAN_SPEED, PACMAN_RADIUS, INITIAL_PACMAN_POS

@pytest.fixture
def pacman():
    """Фікстура для створення об'єкта Pacman."""
    return Pacman()

@pytest.mark.parametrize("key, expected_dx, expected_dy", [
    (pygame.K_LEFT, -PACMAN_SPEED, 0),
    (pygame.K_RIGHT, PACMAN_SPEED, 0),
    (pygame.K_UP, 0, -PACMAN_SPEED),
    (pygame.K_DOWN, 0, PACMAN_SPEED),
])
def test_pacman_move(pacman, mocker, key, expected_dx, expected_dy):
    """Перевіряє рух Pacman у різних напрямках."""
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}
    keys[key] = True
    mocker.patch('pygame.key.get_pressed', return_value=keys)
    initial_pos = pacman.pos.copy()
    pacman.move(keys, walls=[])
    assert pacman.pos[0] == initial_pos[0] + expected_dx
    assert pacman.pos[1] == initial_pos[1] + expected_dy

def test_pacman_border_limits(pacman, mocker):
    """Перевіряє, що Pacman не виходить за межі екрану."""
    pacman.pos = [WIDTH - PACMAN_RADIUS, HEIGHT - PACMAN_RADIUS]
    keys = {pygame.K_RIGHT: True, pygame.K_DOWN: True}
    mocker.patch('pygame.key.get_pressed', return_value=keys)
    pacman.move(keys, walls=[])
    assert pacman.pos[0] <= WIDTH - PACMAN_RADIUS
    assert pacman.pos[1] <= HEIGHT - PACMAN_RADIUS

def test_pacman_wall_collision(pacman, mocker):
    """Перевіряє, що Pacman не проходить крізь стіни."""
    wall = pygame.Rect(50, 50, 25, 25)
    pacman.pos = [60, 60]
    keys = {pygame.K_RIGHT: True}
    mocker.patch('pygame.key.get_pressed', return_value=keys)
    initial_pos = pacman.pos.copy()
    pacman.move(keys, walls=[wall])
    assert pacman.pos == initial_pos  # Pacman не рухається через колізію

def test_pacman_get_rect(pacman):
    """Перевіряє коректність прямокутника Pacman."""
    rect = pacman.get_rect()
    assert rect.center == (pacman.pos[0], pacman.pos[1])
    assert rect.width == PACMAN_RADIUS * 2
    assert rect.height == PACMAN_RADIUS * 2

@pytest.mark.slow
def test_pacman_initial_position(pacman):
    """Перевіряє початкову позицію Pacman."""
    assert pacman.pos == INITIAL_PACMAN_POS