def main():
    print("Two-dimensional arrays (tuples and lists) in Python")

    kernel = (
        (0.05, 0.20, 0.05),
        (0.20, 0.00, 0.20),
        (0.05, 0.20, 0.05),
    )

    print("Kernel:", kernel)

    # we can access elements using row and column indices
    print("Element at row 0, column 2:", kernel[0][2])
    print("Element at row 1, column 1:", kernel[1][1])
    print("Element at row 2, column 1:", kernel[2][1])

    # tuples are immutable, so we cannot change their elements
    # kernel[1][0] = 0.07  # This will raise a TypeError

    # Let's declare a two-dimensional list (which is mutable)- 7 rows and 4 columns with default zero values
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    print("Matrix:", matrix)

    # alternate way to create a 7x4 matrix using list comprehension with default zero values
    matrix_comprehension = [[0 for _ in range(4)] for _ in range(7)]
    print("Matrix created using list comprehension:", matrix_comprehension)

    # alternate way
    # a = [[0] * 4] * 7
    # print("Matrix created using multiplication:", a)
    # # However, the above method creates a matrix where all rows reference the same list, which can lead to unexpected behavior when modifying elements
    # a[1][2] = 19
    # print("Matrix after modifying element at row 1, column 2:", a)
    # # In the above case, modifying one element modifies all rows because they reference the same list

    a = []
    for i in range(7):
        new_row = [0] * 4
        a.append(new_row)

    print("Matrix created using a loop:", a)

    a[0][0] = 42
    a[1][2] = 19
    a[6][3] = 100

    print("Matrix after modifications:", a)

    # we can get number of rows and columns using len() function
    print("Number of rows in the matrix:", len(a))
    print("Number of columns in the matrix:", len(a[0]))

    # we can have non-rectangular (jagged) arrays in Python
    num_rows = 4
    board = []
    for row in range(num_rows):
        board.append([False] * row)

    print("Jagged board:", board)

    # let's add false to every row of the board
    for row in range(len(board)):
        board[row].append(False)

    print("Jagged board after adding False to each row:", board)

    set_first_element_to_true(board)
    print("Jagged board after setting the first element to True:", board)

    print_board(board)


def set_first_element_to_true(a: list[list[bool]]) -> None:
    """
    Sets the element in the "top left" of a given 2-D boolean list to True

    :param
    - a: a 2-D boolean list

    output: None (modifies the input list in place)
    """
    if len(a) == 0 or len(a[0]) == 0:
        raise ValueError("Error: Invalid dimensions of the board.")

        a[0][0] = True


def print_board(board: list[list[bool]]) -> None:
    """
    Prints a 2-D boolean list in a readable format

    :param
    - board: a 2-D boolean list

    output: None (prints the board to the console)
    """
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(board[r][c], end=" ")
        print()  # move to the next line after printing each row


if __name__ == "__main__":
    main()
