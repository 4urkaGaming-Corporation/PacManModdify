import pytest 
import pygame 
from maze import Maze 
from entities import Coin 
from settings import CELL_SIZE, COIN_SIZE 
 
@pytest.fixture 
def maze(): 
    return Maze() 
 
def test_maze_walls(maze): 
    walls = maze.get_walls() 
    assert len(walls) > 0 
    assert all(isinstance(wall, pygame.Rect) for wall in walls) 
 
def test_maze_coins(maze): 
    assert len(maze.coins) > 0 
    assert all(isinstance(coin, Coin) for coin in maze.coins) 
    coin = maze.coins[0] 
    assert coin.rect.width == COIN_SIZE 
 
def test_maze_draw(maze, mocker): 
    mock_draw_rect = mocker.patch('pygame.draw.rect') 
    mock_draw_coin = mocker.patch.object(Coin, 'draw') 
    maze.draw(pygame.Surface((700, 775))) 
    assert mock_draw_rect.called 
    assert mock_draw_coin.called