from settings import Sett
import pygame
from typing import *
import math
from utils import *

class Node:

    def __init__(self, x: float, y: float, name: str = 'unamed'):
        self.name = name
        self.x: float = x
        self.y: float = y
        self.neighbourS: List[any] = []
        self.value: float = math.inf
        self.searched: bool = False

        self.previousNode: Node = None  # the last node which had 'found' this node

        self.color: str = Sett.CADET_BLUE

    def addNeighbour(self, neighbour):
        if neighbour not in self.neighbourS:
            self.neighbourS.append(neighbour)
        if self not in neighbour.neighbourS:
            neighbour.neighbourS.append(self)

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):


        pygame.draw.rect(screen, self.color, [self.x, self.y, Sett.gridSize, Sett.gridSize])


        displayValue = self.value if self.value != math.inf else 'inf'
        textsurface = font.render(str(displayValue), False, Sett.WHITE)
        screen.blit(textsurface, (self.x + Sett.gridSize / 2 - 10, self.y + Sett.gridSize / 2 - 10))

        textsurface = font.render(self.name, False, Sett.DARK_VIOLET)
        screen.blit(textsurface, (self.x - 20, self.y - 20))


