"""
graph-regions
Create a program that will take in an adjacency matrix, 
and then calculate the unique regions represented by that adjacency matrix.

The adjacency matrix should be in the form of a string matrix of '1's and '0's, with '1's representing a connection.

Will output the representation of the regions, which is a list of sets
"""
import sys
from region import Region, runMain
from reader import getGraphs
from argparse import ArgumentParser

parser = ArgumentParser(
    description="Get the regions from a group of adjacency matrices."
    )
parser.add_argument('input', metavar="file",default=None, nargs="?")

if (file := parser.parse_args()).input is None:
    FILE = sys.stdin
else:
    FILE = open(file.input, 'r')


for num, graph in getGraphs(FILE):
    print(f"#{num+1}", graph, runMain(graph), sep="\n")

FILE.close()