from settings import Sett
from node import Node
from path import Path
import pygame
import math
from typing import *
from utils import *
import copy

class Graph:
    sourceNode: Node = None
    endNode: Node = None
    nodeS: List[Node] = []
    pathS: List[Path] = []
    currentNode: Node = None
    finishedSearching: bool = False

    @staticmethod
    def addPath(path: Path):

        def addNode(node: Node):
            if node not in Graph.nodeS:
                Graph.nodeS.append(node)

        if path not in Graph.pathS:
            Graph.pathS.append(path)
            addNode(path.node1)
            addNode(path.node2)

    @staticmethod
    def whichPath(node1: Node, node2: Node) -> Path:
        for path in Graph.pathS:
            one = (path.node1 == node1 and path.node2 == node2)
            theOther = (path.node2 == node1 and path.node1 == node2)
            if one or theOther:
                return path
        
        # if nothing was find
        raise ValueError('lol something went wrong' + ('!' * 100))

    @staticmethod
    # find the path with the minimum cost
    def findMinPath(pathS: List[Path]) -> Path:
        min: Path = pathS[0]  # by default

        for path in pathS:
            if path.weight < min.weight:
                min = path
        return min

    @staticmethod
    def findClosestNeighbour(node1: Node, canFindSearched: bool = True) -> Node:
        nodeS: List[Node] = node1.neighbourS
        min: Node = nodeS[0]  # by default

        for node in nodeS:
            if nodeDistance(node1, node) < nodeDistance(node1, min):
                if canFindSearched is False and node.searched is True:
                    continue
                min = node
        return min


    @staticmethod
    def traverse(node1: Node):
        nodeS = node1.neighbourS
        # by default it's the first node in the list
        sortedNodes: List[Node] = sortNodes(nodeS)

        # minNode: Node = sortedNodes[0]  # this is the node that is the least furthest away from the source

        for node in sortedNodes:
            if node.searched:
                continue
            newValue: float = Graph.whichPath(node1, node).weight + node1.value

            if newValue < node.value:
                node.value = newValue
                node.searched = True
                node.color = Sett.RED
                node.previousNode = node1

                Graph.whichPath(node1, node).color = Sett.RED

    @staticmethod
    def findEdgeNodes():
        edgeNodes: List[Node] = []
        for node in Graph.nodeS:
            if node.searched:
                for neighbour in node.neighbourS:
                    if not neighbour.searched and node not in edgeNodes:
                        edgeNodes.append(node)
        return edgeNodes

        return edgeNodes
    @staticmethod
    def explore() -> None:

        #first time checking
        if Graph.currentNode == None:
            Graph.currentNode = Graph.sourceNode
    
        Graph.traverse(Graph.currentNode)
        if Graph.endNode.searched:
            Graph.finishedSearching = True
            return
        edgeNodes: List[Node] = Graph.findEdgeNodes()
        Graph.currentNode = sortNodes(edgeNodes)[0]

    @staticmethod
    def tracePath():

        route: List[Node] = []
        currentNode = Graph.endNode
        while True:
            route.append(currentNode.previousNode)
            currentNode = currentNode.previousNode

            if currentNode == Graph.sourceNode:
                break
        route = route[::-1]
        route.append(Graph.endNode)

        for i in range(0, len(route) - 1):
            Graph.whichPath(route[i], route[i + 1]).color = Sett.DARK_KHAKI
            route[i].color = Sett.DARK_KHAKI
            route[i+1].color = Sett.DARK_KHAKI





    @staticmethod
    def draw(screen: pygame.Surface, font: pygame.font.Font):
        for path in Graph.pathS:
            path.draw(screen, font)







