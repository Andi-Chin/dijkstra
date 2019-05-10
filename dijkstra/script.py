import sys
import pygame
from math import pi
import time
from settings import Sett
from node import Node
from path import Path
from graph import Graph
from typing import *
from utils import *
from gameFunctions import *


#setup
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)
size = [Sett.width, Sett.height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("dijkstra")


sourceNode = Node(50, 50, 'start')
sourceNode.value = 10
sourceNode.searched = True
endNode = Node(700, 500, 'end')
Graph.sourceNode = sourceNode
Graph.endNode = endNode

n1: Node = Node(700, 650, 'n1')

Graph.addPath(Path(sourceNode, n1))
Graph.addPath(Path(n1, endNode))


while True:
    screen.fill(Sett.BLACK)

    if not userActionPhase():
        break
    Graph.draw(screen, myfont)
    pygame.display.flip()


# TODO organize game gym events


Graph.draw(screen, myfont)
pygame.display.flip()
time.sleep(2)
while True:

    screen.fill(Sett.BLACK)

    if Graph.finishedSearching == True:
        Graph.tracePath()
    else: 
        Graph.explore()


    Graph.draw(screen, myfont)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()

    print(pygame.mouse.get_pos())

    time.sleep(2)


