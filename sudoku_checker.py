import numpy as np

np_sudoku = np.random.randint(1, 9, (9, 9))
print(np_sudoku)


def sudoku_checker(numpy_arr):
    s = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for i in range(np_sudoku.shape[0]):
        if set(np_sudoku[i, :]) != s:
            return False

    for j in range(np_sudoku.shape[1]):
        if set(np_sudoku[:, i]) != s:
            return False

    x = 0
    while x < 9:
        y = 0
        while y < 9:
            if set(np_sudoku[x:x+3, y:y+3].ravel()) != s:
                return False
            y += 3
        x += 3

    return True


print(sudoku_checker(np_sudoku))


