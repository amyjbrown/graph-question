"""
graph-regions
Create a program that will take in an adjacency matrix, 
and then calculate the unique regions represented by that adjacency matrix.

The adjacency matrix should be in the form of a string matrix of '1's and '0's, with '1's representing a connection.

Will output the representation of the regions, which is a list of sets
"""
from graph import Graph
from reader import fromMatrix
from typing import List, Set

Region = Set[int]

def addToRegion(graph: Graph, node: int, region: Region):
    """
    Add every transitively connected node that originates from `node` in `graph` to  `region`
    """
    # if node in region: return
    region.add(node)
    for n in graph.neighbours(node):
        if n in region: continue
        else:
            region.add(n)
            addToRegion(graph, n, region)


def getRegions(graph: Graph) -> List[Region]:

    def discovered(node: int, regions: List[Region]) -> bool:
        """
        Predicate for if node has already been added to some region
        """
        for r in regions:
            if node in r: return True

        return False

    regions: List[Region] = []
    for node in graph.edges.keys():
        if discovered(node, regions): continue
        else:
            rg = set()
            addToRegion(graph, node, rg)
            regions.append(rg)
    
    return regions


def runMain(form: int) -> List[Region]:
    return getRegions(fromMatrix(form))


if __name__ == "__main__":
    s1 = (
        "1000\n"
        "0100\n"
        "0010\n"
        "0001"
    )
    print(runMain(s1))
    assert runMain(s1) == [{0}, {1}, {2}, {3}]