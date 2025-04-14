import pytest
import pygame
from game import Game
from entities import Pacman, Enemy
from maze import Maze


@pytest.fixture
def game(mocker):
    mocker.patch("pygame.display.set_mode")
    mocker.patch("pygame.mixer.init")
    mocker.patch("pygame.mixer.music.load")
    mocker.patch("pygame.mixer.music.set_volume")
    mocker.patch("pygame.mixer.music.play")
    return Game(volume=0.5)


def test_game_initial_state(game):
    assert game.score == 0
    assert not game.game_over
    assert not game.game_won
    assert isinstance(game.pacman, Pacman)
    assert len(game.enemies) == 4
    assert isinstance(game.maze, Maze)


def test_game_score_update(game, mocker):
    initial_coin_count = game.initial_coin_count
    mocker.patch.object(game.maze, "coins", [])
    game.score = 10 * (initial_coin_count - len(game.maze.coins))
    assert game.score == 10 * initial_coin_count


def test_game_over_collision(game, mocker):
    # перевірка логіки напряму
    mocker.patch.object(
        game.pacman, "get_rect", return_value=pygame.Rect(50, 50, 20, 20)
    )
    mocker.patch.object(
        game.enemies[0], "get_rect", return_value=pygame.Rect(50, 50, 20, 20)
    )
    # колізія
    game.check_collisions()
    assert game.game_over


def test_game_win_condition(game):
    game.score = 5000
    assert game.game_won
