"""
Interfaces for reading from a file or stdin
"""
from typing import TextIO, Optional, Iterator, Tuple

def read(file: TextIO) -> Iterator[int, str]:
    """
    Read input from any file and perform the appropriate actions/outputs
    """
    graphnum = int(file.readline().split())

    for n in range(graphnum):
        dims = file.readline().split().strip()
        _, height = int(dims[0]), int(dims[1])

        graph_lines = []
        graph = None
        for h in range(height):
            graph_lines.append( file.readline() )
        graph = "".join(graph_lines)

        yield n, graph


if __name__ == "__main__":
    pass