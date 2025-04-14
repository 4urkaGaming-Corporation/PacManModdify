import pygame
import pytest
from entities import Coin
from settings import COIN_SIZE, YELLOW


@pytest.fixture
def coin():
    return Coin(50, 50)


def test_coin_initialization(coin):
    assert coin.rect.x == 50
    assert coin.rect.y == 50
    assert coin.rect.width == COIN_SIZE
    assert coin.rect.height == COIN_SIZE
    assert coin.collected is False


def test_coin_draw(coin, mocker):
    window = mocker.Mock(spec=pygame.Surface)
    mock_draw = mocker.patch("pygame.draw.rect")
    coin.draw(window)
    if not coin.collected:
        mock_draw.assert_called_once_with(window, YELLOW, coin.rect)
    else:
        mock_draw.assert_not_called()
