import pytest 
import pygame 
from entities import Coin 
from settings import COIN_SIZE 
 
@pytest.fixture 
def coin(): 
    return Coin(x=50, y=50) 
 
def test_coin_initial_state(coin): 
    assert coin.rect.x == 50 
    assert coin.rect.y == 50 
    assert coin.rect.width == COIN_SIZE 
    assert not coin.collected 
 
def test_coin_draw_not_collected(coin, mocker): 
    mock_draw = mocker.patch('pygame.draw.rect') 
    coin.draw(pygame.Surface((100, 100))) 
    mock_draw.assert_called_once() 
 
def test_coin_draw_collected(coin, mocker): 
    coin.collected = True 
    mock_draw = mocker.patch('pygame.draw.rect') 
    coin.draw(pygame.Surface((100, 100))) 
    mock_draw.assert_not_called()