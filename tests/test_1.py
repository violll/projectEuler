import pytest
# import sys

import cyclicalFigurateNumbers  

@pytest.mark.parametrize("polynIdx, expectedTri, expectedSquare, expectedPent, expectedHex, expectedHep, expectedOct", [
    (1,  1,  1,  1,  1,  1,  1),
    (2,  3,  4,  5,  6,  7,  8),
    (3,  6,  9, 12, 15, 18, 21),
    (4, 10, 16, 22, 28, 34, 40),
    (5, 15, 25, 35, 45, 55, 65)
])

def test_PolyNums(polynIdx, expectedTri, expectedSquare, expectedPent, expectedHex, expectedHept, expectedOct):
    assert cyclicalFigurateNumbers.triNum(polynIdx) == expectedTri
    # assert cyclicalFigurateNumbers.squareNum(polynIdx) == expectedSquare
    # assert cyclicalFigurateNumbers.pentNum(polynIdx) == expectedPent
    # assert cyclicalFigurateNumbers.hexNum(polynIdx) == expectedHex
    # assert cyclicalFigurateNumbers.heptNum(polynIdx) == expectedHept
    # assert cyclicalFigurateNumbers.octNum(polynIdx) == expectedOct

if __name__ == "__main__":
    test_PolyNums()