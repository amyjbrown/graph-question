"""
graph-regions
Create a program that will take in an adjacency matrix, 
and then calculate the unique regions represented by that adjacency matrix.

The adjacency matrix should be in the form of a string matrix of '1's and '0's, with '1's representing a connection.

Will output the representation of the regions, which is a list of sets
"""
import sys
from region import Region, runMain

if __name__ == "__main__":
    s1 = (
        "1000\n"
        "0100\n"
        "0010\n"
        "0001"
    )
    print(runMain(s1))
    assert runMain(s1) == [{0}, {1}, {2}, {3}]