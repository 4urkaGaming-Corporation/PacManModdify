import pygame
from settings import *

labyrinth = [
    "############################",
    "#00000#00000000#0000000000##",
    "#0####0#0#####00#0####00000#",
    "#0####0#0000000000####00000#",
    "#000000#0#0##000000000#0000#",
    "#0#####0000##0#####000#0000#",
    "#0#0000000#0000000#000#0000#",
    "#0#0####00#0#####0#0###0000#",
    "#00000000000000000000000000#",
    "#0#0####00#00000#####000000#",
    "#0#####000#0##0000000#####0#",
    "#000000#0000000##0000000000#",
    "#######0#0#####0#0#####0000#",
    "#000#000000000000000000#000#",
    "#000#0000####0000000#0#0000#",
    "#000#0000000000000000000000#",
    "#000#0000####0#####0#0#0000#",
    "#000#000000000000000000#000#",
    "#0000000#0#####0#0#####0000#",
    "#00000000000000##0000000000#",
    "#000000000#0##0000000#####0#",
    "#0#000000000000000###000000#",
    "#000000#00#00000#0000000000#",
    "#0####0#00#0###0#0####00000#",
    "#0####0#0000000000####00000#",
    "#000000#0#####00#0000000000#",
    "#0#####000000000#0#####000##",
    "#0#000#0#000#000#0000#00000#",
    "#0#0###0#0###000#0###0#0000#",
    "#00000000000000000000000000#",
    "############################"
]

class Maze:
    def __init__(self):
        self.walls = self.get_walls()
        self.coins = []
        
        for row in range(len(labyrinth)):
            for col in range(len(labyrinth[row])):
                if labyrinth[row][col] == "0":
                    coin_x = col * CELL_SIZE + (CELL_SIZE - COIN_SIZE) // 2
                    coin_y = row * CELL_SIZE + (CELL_SIZE - COIN_SIZE) // 2
                    self.coins.append(Coin(coin_x, coin_y))

    def get_walls(self):
        walls = []
        for row in range(len(labyrinth)):
            for col in range(len(labyrinth[row])):
                if labyrinth[row][col] == "#":
                    walls.append(pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        return walls

    def draw(self, window):
        for row in range(len(labyrinth)):
            for col in range(len(labyrinth[row])):
                if labyrinth[row][col] == "#":
                    pygame.draw.rect(window, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif labyrinth[row][col] == "-":
                    pygame.draw.rect(window, GRAY, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for coin in self.coins:
            coin.draw(window)

from entities import Coin