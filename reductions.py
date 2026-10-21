"""
15-251 Great Ideas in Theoretical Computer Science
Assignment: Reductions
Version: Fall 2026

STARTER CODE
"""
from classes import UGraph, CNF, DistanceMatrix, ZPMOMatrix
from typing import Tuple, List


"""
Show that EQUAL-COL is NP-hard.
- Input: x is an object representing the instance you are reducing from
- Output: a UGraph object representing a EQUAL-COL instance
"""
choice_EQUAL_COL_reduce_from = "" # TODO: pick from "SAT", "3SAT", "CLIQUE", "INDEPENDENT-SET", "VERTEX-COVER", "HAMILTONIAN-CYCLE", "3COL", "SUBSET-SUM"
def to_EQUAL_COL(x) -> UGraph:
    # TODO: implement the reduction
    return UGraph(...)


"""
The type of UNITED-NATIONS is a tuple (k, D, t, n):
- k (int): number of countries. Assume countries are labeled by 0, 1, 2, ..., k-1
- D (DistanceMatrix): D[i][j] is the distance between countries c_i and c_j
- t (int)
- n (int)

Show that UNITED-NATIONS is NP-hard.
Input: x is an object representing the instance you are reducing from
Output: a tuple (k, D, t, n) representing a UNITED-NATIONS instance
"""
choice_UNITED_NATIONS_reduce_from = "" # TODO: pick from "SAT", "3SAT", "CLIQUE", "INDEPENDENT-SET", "VERTEX-COVER", "HAMILTONIAN-CYCLE", "3COL", "SUBSET-SUM"
def to_UNITED_NATIONS(x) -> Tuple[int, DistanceMatrix, int, int]:
    # TODO: implement the reduction
    k = ...
    D = DistanceMatrix(...)
    t = ...
    n = ...
    return (k, D, t, n)


"""
Show that NONZERO-MATRIX is NP-hard.
Input: x is an object representing the instance you are reducing from
Output: a ZPMOMatrix object M representing a NONZERO-MATRIX instance
"""
choice_NONZERO_MATRIX_reduce_from = "" # TODO: pick from "SAT", "3SAT", "CLIQUE", "INDEPENDENT-SET", "VERTEX-COVER", "HAMILTONIAN-CYCLE", "3COL", "SUBSET-SUM"
def to_NONZERO_MATRIX(x) -> ZPMOMatrix:
    # TODO: implement the reduction
    return ZPMOMatrix(...)


# DO NOT EDIT
choices = {
    "EQUAL-COL": choice_EQUAL_COL_reduce_from,
    "UNITED-NATIONS": choice_UNITED_NATIONS_reduce_from,
    "NONZERO-MATRIX": choice_NONZERO_MATRIX_reduce_from
}
