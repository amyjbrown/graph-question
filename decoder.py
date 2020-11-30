"""
Main test for the question
"""
from graph import Graph

def fromText(s: str) -> Graph:
    """
    Generate a valid graph from the adjacency matrix
    """
    g = Graph()
    for sender, line in enumerate(s.strip().split()):
        g.addVert(sender)
        for reciever, glyph in enumerate(line):
            if glyph == "1" and reciever != sender: # We wish to ignore the case of edges to yourself
                g.addEdge(sender, reciever) # this is symetric, but oh well
    
    return g


if __name__ == "__main__":
    matt = (
        "1101\n"
        "1100\n"
        "0011\n"
        "1011"
    )
    print(
        fromText(
            matt
        ).edges
    )

    print(fromText(
        "1000\n"
        "0100\n"
        "0010\n"
        "0001"
        ).edges
    )

    print(fromText(
        "1000\n"
        "0100\n"
        "0010\n"
        "0001"

        ).edges
    )
    # new format
    print(fromText(
        """
        1000
        0100
        0010
        0001
        """
    ).edges)

    print(fromText(
        """
        1100
        1100
        0011
        0011
        """
    ).edges)