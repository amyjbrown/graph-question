from graph import Graph
from decoder import fromText
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
    return getRegions(fromText(form))
