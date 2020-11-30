"""
Interfaces for reading from a file or stdin
"""
from typing import TextIO, Optional, Tuple, Iterator

def getGraphs(file: TextIO) -> Iterator[Tuple[int, str]]:
    """
    Read input from any file and perform the appropriate actions/outputs
    """
    graphnum = int(file.readline())

    for n in range(graphnum):
        dims = file.readline().strip().split()
        _, height = int(dims[0]), int(dims[1])

        graph_lines = []
        graph = None
        for h in range(height):
            graph_lines.append( file.readline() )
        graph = "".join(graph_lines)

        yield n, graph


if __name__ == "__main__":
    pass