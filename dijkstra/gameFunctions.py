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


def getNearestNode(x: float, y: float) -> Node:
    min = Graph.nodeS[rd(0, len(Graph.nodeS) - 1)]  #by default
    for node in Graph.nodeS:
        if distance(node.x, node.y, x, y) < distance(min.x, min.y, x, y):
            min = node
    return min


def userActionPhase() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            mousePos: Tuple[float] = pygame.mouse.get_pos()

            if not Sett.isSelecting :
                Sett.selectionNode1 = getNearestNode(mousePos[0], mousePos[1])
                Sett.isSelecting = True
            elif Sett.isSelecting:
                Graph.addPath(Path(Sett.selectionNode1, Node(mousePos[0], mousePos[1])))

                Sett.isSelecting = False

            # newNode: Node = Node(mousePos[0], mousePos[1])  # this is the node created at the user's mouse position


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return False  # terminate the user action phase


    return True