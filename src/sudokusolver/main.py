#exampleSudoku = "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
exampleSudoku = [[5,3,0,0,7,0,0,0,0],
                 [6,0,0,1,9,5,0,0,0],
                 [0,9,8,0,0,0,0,6,0],
                 [8,0,0,0,6,0,0,0,3],
                 [4,0,0,8,0,3,0,0,1],
                 [7,0,0,0,2,0,0,0,6],
                 [0,6,0,0,0,0,2,8,0],
                 [0,0,0,4,1,9,0,0,5],
                 [0,0,0,0,8,0,0,7,9]]

def check_row_valid(sudoku: list[list[int]], rowNum: int, proposedVal: int = 0) -> bool:
    """
    Determines whether or not there are or will be any repeated values in the selected row
    :param sudoku: The sudoku puzzle grid that is to be checked
    :param rowNum: The index of the row that is being checked
    :param proposedVal: A value that could be added to the row
    :return: Whether or not the row is valid and has no repeated values
    """

    numbers = [n for n in sudoku[rowNum] if n != 0]

    if proposedVal != 0:
        numbers.append(proposedVal)

    return len(numbers) == len(set(numbers))

def check_row_complete(sudoku: list[list[int]], rowNum: int) -> bool:
    """
    Determines whether the selected row is completed (all values 1-9 are present)
    :param sudoku: The sudoku puzzle grid that is to be checked
    :param rowNum: The index of the row that is to be checked
    :return: Whether or not the selected row is complete
    """
    return set(sudoku[rowNum]) == set(range(1,10))

def check_col_valid(sudoku: list[list[int]], colNum: int, proposedVal: int = 0) -> bool:
    """
    Determines whether or not there are or will be any repeated values in the selected column
    """

    col = [sudoku[row][colNum] for row in range(9)]
    numbers = [n for n in col if n != 0]

    if proposedVal != 0:
        numbers.append(proposedVal)

    return len(numbers) == len(set(numbers))

def check_col_complete(sudoku: list[list[int]], colNum: int) -> bool:
    col = [sudoku[row][colNum] for row in range(9)]
    return set(col) == set(range(1, 10))

def check_box_valid(sudoku: list[list[int]], boxNum: int, proposedVal: int = 0) -> bool:
    box = [sudoku[x][y] for x in range((boxNum // 3) * 3, (boxNum // 3) * 3 + 3) for y in range((boxNum % 3) * 3, (boxNum % 3) * 3 + 3)]
    numbers = [n for n in box if n != 0]
    if proposedVal != 0:
        numbers.append(proposedVal)
    return len(numbers) == len(set(numbers))

def check_box_complete(sudoku: list[list[int]], boxNum: int) -> bool:
    box = [sudoku[x][y] for x in range((boxNum // 3) * 3, (boxNum // 3) * 3 + 3) for y in range((boxNum % 3) * 3, (boxNum % 3) * 3 + 3)]
    return set(box) == set(range(1, 10))

def check_cell(sudoku: list[list[int]], rowNum: int, colNum: int, proposedVal: int) -> bool:
    return check_box_valid(sudoku, (3*(rowNum//3) + colNum//3), proposedVal) and check_row_valid(sudoku, rowNum, proposedVal) and check_col_valid(sudoku, colNum, proposedVal)

def backtracking():
    return

def main():
    return

if __name__ == '__main__':
    main()
