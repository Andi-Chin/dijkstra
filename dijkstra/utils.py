from typing import *
import math


def distance(x: float, y: float, x1: float, y1: float):
    xDist: float = abs(x1 - x)
    yDist: float = abs(y1 - y)
    return math.sqrt(xDist * xDist + yDist * yDist)


def nodeDistance(node1, node2):
    return distance(node1.x, node1.y, node2.x, node2.y)



def sortNodes(array: List[any]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x.value < pivot.value:
                less.append(x)
            elif x.value == pivot.value:
                equal.append(x)
            elif x.value > pivot.value:
                greater.append(x)
        return sortNodes(less)+equal+sortNodes(greater)
    else:
        return array



