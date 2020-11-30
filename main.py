from graph import Graph
from reader import fromMatrix
from typing import List, Set


def regions(matrix: str):
    """
    Show all connected regions inside of an adjacency matrix, as described by `matrix`

    Returns:
        List[Set]: A list of each uniqiue region, with each region represented by a Set of vertices 
    """
    graph = fromMatrix(matrix)
    regions: List[Set] = []

    pass