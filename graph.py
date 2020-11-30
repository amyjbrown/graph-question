"""
Minimal Graph Data type Implementation for a undirected, edge-value-less graph
"""
from typing import Dict, Set, Optional
import unittest

class Graph:
    """
    Unidirected Graph, with no value stored on edges, and vertices are pure ints 
    """
    def __init__(self):
        self.edges: Dict[int, Set[int]] = dict()
    
    def addVert(self, vertex) -> bool:
        """
        Add the vertex `vertex` to the graph if it doesn't already exist, return if it adds it 
        """
        if vertex not in self.edges:
            self.edges[vertex] = set()
            return True
        else: return False
    
    def addEdge(self, a, b) -> bool:
        """
        Adds an edge between a and b, adding the vertices if needed
        This is undirected, so it shows up in both -- for that reason I've left adjacent() below to be unidirect
        """
        # see if it isn't already in there
        if a in self.edges and b in self.edges[a]: return False
        # add the vertices we need, addVert() is safe
        self.addVert(a)
        self.addVert(b)
        self.edges[a].add(b)
        self.edges[b].add(a)
        return True
    
    def adjacent(self, a, b) -> bool:
        """
        Return true if a has an edge in b, else false
        Will return false if a or b not in graph 
        """
        if a not in self.edges: return False
        return b in self.edges[a]
    
    def neighbours(self, a) -> Optional[Set[int]]:
        """
        Return all vertices that have edges with `a`, or None if a is not defined in the graph
        """
        return self.edges.get(a)

if __name__ == "__main__":
    class GraphTest(unittest.TestCase):
        def test_add_vetex(self):
            graph = Graph()
            # check that adding a vertices produces the right error code
            self.assertTrue(graph.addVert(1))
            self.assertFalse(graph.addVert(1))
            # check that 
            g1, g2 = Graph(), Graph()
            g1.addVert(1)
            self.assertEqual(
                g1.edges,
                {1: set()}
            )
            g2.addVert(1)
            self.assertEqual(g1.edges, g2.edges)
        
        def test_add_edge(self):
            g1 = Graph()
            g1.addEdge(1, 2)
            self.assertTrue(g1.edges[1])
            self.assertTrue(g1.edges[2])
            self.assertEqual(
                g1.edges,
                {
                    1: {2},
                    2: {1}
                }
            )
        
        def test_adjacent(self):
            g = Graph()
            g.addEdge(1, 2)
            self.assertTrue(g.adjacent(1,2))
            self.assertTrue(g.adjacent(2, 1))
            g.addEdge(1,3)
            self.assertTrue(g.adjacent(1,3))
            self.assertFalse(g.adjacent(2,3))