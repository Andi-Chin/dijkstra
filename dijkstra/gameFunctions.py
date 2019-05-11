import pygame
from typing import List
from typing import Tuple
import sys
from settings import Sett
from node import Node
from path import Path
from graph import Graph
from utils import *
from random import randint as rd
from datetime import datetime


def getNearestNodeS(x: float, y: float) -> List[Node]:
    min: Node = Graph.nodeS[rd(0, len(Graph.nodeS) - 1)]  #by default
    min2: Node = Graph.nodeS[rd(0, len(Graph.nodeS) - 1)]  #by default

    for node in Graph.nodeS:
        if distance(node.x, node.y, x, y) < distance(min.x, min.y, x, y):
            min = node
    for node in Graph.nodeS:
        if distance(node.x, node.y, x, y) < distance(min2.x, min2.y, x, y) and node is not min:
            min2 = node
    return [min, min2]


def userActionPhase() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        timeDiff: int = (datetime.now() - Sett.timeWhenClicked).microseconds
        if pygame.mouse.get_pressed()[0] and timeDiff > 100000:
            Sett.timeWhenClicked = datetime.now()

            mousePos: Tuple[float] = pygame.mouse.get_pos()

            # this is the node created at the user's mouse position
            newNode: Node = Node(mousePos[0], mousePos[1])

            n1, n2 = getNearestNodeS(mousePos[0], mousePos[1])

            Graph.addPath(Path(newNode, n1))
            Graph.addPath(Path(newNode, n2))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return False  # terminate the user action phase


    return True