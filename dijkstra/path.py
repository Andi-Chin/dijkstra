from settings import Sett
from node import Node
import pygame
from typing import *
from utils import *

class Path:
    # of course you can just add a weight parameter and make it user defined
    def __init__(self, node1: Node, node2: Node):
        node1.addNeighbour(node2)
        node2.addNeighbour(node1)
        self.node1 = node1
        self.node2 = node2
        #for now, let's make this by default the distance between them
        self.weight = round(distance(node1.x, node1.y, node2.x, node2.y))
        self.color = Sett.GREEN

    def calculate(self):
        self.node2.value = self.node1.value + self.weight

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        # drawing the actual line
        pygame.draw.line(screen, self.color,
                         [self.node1.x + Sett.gridSize / 2, self.node1.y + Sett.gridSize / 2],
                         [self.node2.x + Sett.gridSize / 2, self.node2.y + Sett.gridSize / 2], 5)
        # displaying the weight of the path (text)
        textsurface = font.render(str(self.weight), False, Sett.WHITE)
        xHalf = (self.node1.x - self.node2.x) / 2
        yHalf = (self.node1.y - self.node2.y) / 2
        screen.blit(textsurface, (self.node1.x - xHalf, self.node1.y - yHalf))

        self.node1.draw(screen, font)
        self.node2.draw(screen, font)

