# This is a Sudoku Solver script
# Some of the Code samples from https://www.sudoku-solutions.com/
from SudokuSolver import SudokuSolver

TestData1 = [
    [  5 ,   3 , None, None,   7 , None, None, None, None],
    [  6 , None, None,   1 ,   9 ,   5 , None, None, None],
    [None,   9 ,   8 , None, None, None, None,   6 , None],
    [  8 , None, None, None,   6 , None, None, None,   3 ],
    [  4 , None, None,   8 , None,   3 , None, None,   1 ],
    [  7 , None, None, None,   2 , None, None, None,   6 ],
    [None,   6 , None, None, None, None,   2 ,   8 , None],
    [None, None, None,   4 ,   1 ,   9 , None, None,   5 ],
    [None, None, None, None,   8 , None, None,   7 ,   9 ]
]

# 3094
SimpleTestData1 = [
    [None, None, None, None, None,   4 ,   5 , None, None],
    [  2 , None,   3 , None, None,   7 , None, None,   8 ],
    [None, None, None, None, None,   2 ,   3 ,   7 ,   6 ],
    [None,   2 , None, None,   9 , None, None,   8 , None],
    [None,   7 , None, None, None, None, None,   1 , None],
    [None,   4 , None, None,   5 , None, None,   2 , None],
    [  8 ,   5 ,   4 ,   3 , None, None, None, None, None],
    [  6 , None, None,   2 , None, None,   4 , None,   9 ],
    [None, None,   2 ,   1 , None, None, None, None, None]
]

# 7634
SimpleTestData2 = [
    [None, None, None, None,   3 , None,   8 ,   4 ,   7 ],
    [None, None, None,   9 ,   8 , None, None, None, None],
    [  4 , None, None, None, None, None, None,   6 ,   5 ],
    [None, None,   1 , None,   7 , None, None, None,   3 ],
    [None,   8 , None, None,   1 ,   3 , None, None, None],
    [  7 , None, None,   4 , None, None, None, None, None],
    [  5 , None, None,   7 , None, None,   6 , None,   9 ],
    [None, None, None, None, None, None,   7 , None,   4 ],
    [  8 , None, None, None, None, None, None,   5 , None]
]

# 4948
MediumTestData1 = [
    [None, None, None, None, None,   7 , None, None, None],
    [None,   6 , None,   3 , None, None, None,   8 , None],
    [  4 ,   1 ,   5 ,   6 , None, None, None, None, None],
    [None, None,   8 ,   5 , None, None, None, None, None],
    [  6 ,   5 , None,   7 , None,   9 , None,   2 ,   3 ],
    [None, None, None, None, None,   6 ,   7 , None, None],
    [None, None, None, None, None,   3 ,   8 ,   1 ,   4 ],
    [None,   2 , None, None, None,   1 , None,   3 , None],
    [None, None, None,   9 , None, None, None, None, None]
]

# 3499
HardTestData1 = [
    [  7 , None, None, None,   4 , None, None,   9 , None],
    [None,   3 , None,   9 ,   5 , None,   6 , None, None],
    [  8 , None,   5 , None, None,   7 , None,   4 , None],
    [  6 , None,   1 , None, None, None, None, None, None],
    [None,   7 ,   9 , None, None, None,   4 ,   1 , None],
    [None, None, None, None, None, None,   9 , None,   6 ],
    [None,   1 , None,   4 , None, None,   5 , None,   8 ],
    [None, None,   8 , None,   1 ,   3 , None,   2 , None],
    [None,   6 , None, None,   8 , None, None, None,   4 ]
]

# 7179
HardTestData2 = [
    [None,   7 , None, None,   3 , None,   4 , None, None],
    [ 8  , None, None,   6 , None,   2 , None, None,   7 ],
    [None, None, None,   7 ,   4 , None, None,   2 , None],
    [None,   1 , None, None, None, None,   2 , None,   5 ],
    [None, None,   8 ,   4 , None,   5 ,   1 , None, None],
    [  9 , None,   3 , None, None, None, None,   7 , None],
    [None,   8 , None, None,   7 ,   6 , None, None, None],
    [  6 , None, None,   8 , None,   4 , None, None,   1 ],
    [None, None,   7 , None,   1 , None, None,   6 , None]
]

if __name__ == '__main__':
    solver1 = SudokuSolver(TestData1)

