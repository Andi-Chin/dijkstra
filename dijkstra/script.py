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


#setup
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)
size = [Sett.width, Sett.height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("dijkstra")


sourceNode = Node(100, 100, 'start')
sourceNode.value = 10
sourceNode.searched = True
endNode = Node(700, 500, 'end')
Graph.sourceNode = sourceNode
Graph.endNode = endNode

n1 = Node(334, 283, 'n1')
n2 = Node(600, 100, 'n2')
n3 = Node(123, 337, 'n3')
n4 = Node(448, 195, 'n4')
n5 = Node(522, 305, 'n5')
n6 = Node(662, 285, 'n6')
n7 = Node(380, 407, 'n7')
n8 = Node(511, 437, 'n8')
n9 = Node(205, 474, 'n9')
n10 = Node(424, 544, 'n10')

Graph.addPath(Path(n9, n10))
Graph.addPath(Path(n10, n8))
Graph.addPath(Path(n9, n7))
Graph.addPath(Path(n1, n5))
Graph.addPath(Path(sourceNode, n2))
Graph.addPath(Path(sourceNode, n3))
Graph.addPath(Path(sourceNode, n4))
Graph.addPath(Path(n4, n2))
Graph.addPath(Path(n5, n4))
# Graph.addPath(Path(n5, endNode))
Graph.addPath(Path(n3, n1))
Graph.addPath(Path(n5, n6))
Graph.addPath(Path(n2, n6))
# Graph.addPath(Path(n6, endNode))
Graph.addPath(Path(n3, n7))
Graph.addPath(Path(n7, n5))
Graph.addPath(Path(n7, n8))
Graph.addPath(Path(n8, endNode))
Graph.addPath(Path(n3, n9))





# TODO organize game gym events

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


