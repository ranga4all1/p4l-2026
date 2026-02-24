from datatypes import GameBoard


def count_rows(board: GameBoard) -> int:
    """
    Count the number of rows in a GameBoard.
    Args:
        board (GameBoard): A 2D list of booleans representing the game state.
    Returns:
        int: Number of rows in the board.
    """
    if not isinstance(board, list):
        raise ValueError("board must be a list.")

    # TODO: implement
    if not isinstance(board, list):
        raise ValueError("board must be a list.")
    return len(board)


def count_cols(board: GameBoard) -> int:
    """
    Count the number of columns in a GameBoard.
    Args:
        board (GameBoard): A 2D list of booleans representing the game state.
    Returns:
        int: Number of columns in the board.
    Raises:
        ValueError: If the board is not rectangular.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty 2D list.")

    # TODO: implement
    if not isinstance(board[0], list):
        raise ValueError("board must be a 2D list.")
    return len(board[0])


def assert_rectangular(board: GameBoard) -> None:
    """
    Ensure that a GameBoard is rectangular.
    Args:
        board (GameBoard): A 2D list of booleans representing the game state.
    Raises:
        ValueError: If the board has no rows or if its rows are not of equal length.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty 2D list.")

    # TODO: implement
    if not isinstance(board[0], list):
        raise ValueError("board must be a 2D list.")
    num_cols = len(board[0])
    for row in board:
        if not isinstance(row, list):
            raise ValueError("board must be a 2D list.")
        if len(row) != num_cols:
            raise ValueError(
                "All rows in the board must have the same number of columns."
            )


def play_game_of_life(initial_board: GameBoard, num_gens: int) -> list[GameBoard]:
    """
    Simulate Game of Life for a given number of generations.
    Args:
        initial_board (GameBoard): The starting game board.
        num_gens (int): The number of generations to simulate.
    Returns:
        list[GameBoard]: Boards from initial through num_gens generations.
    """
    if not isinstance(initial_board, list) or len(initial_board) == 0:
        raise ValueError("initial_board must be a non-empty GameBoard.")
    if not isinstance(num_gens, int) or num_gens < 0:
        raise ValueError("num_gens must be a non-negative integer.")

    if len(initial_board[0]) == 0:
        raise ValueError("No elements in first row.")

    assert_rectangular(initial_board)

    # TODO: implement
    boards = [initial_board]
    for _ in range(num_gens):
        current_board = update_board(boards[-1])
        boards.append(current_board)

    return boards


def update_board(current_board: GameBoard) -> GameBoard:
    """
    Apply Game of Life rules for one generation.
    Args:
        current_board (GameBoard): The current game board.
    Returns:
        GameBoard: A new board representing the next generation.
    """
    if not isinstance(current_board, list) or len(current_board) == 0:
        raise ValueError("current_board must be a non-empty GameBoard.")

    # TODO: implement
    new_board = []
    for row in range(len(current_board)):
        new_row = []
        for col in range(len(current_board[0])):
            new_row.append(update_cell(current_board, row, col))
        new_board.append(new_row)

    return new_board


def initialize_board(num_rows: int, num_cols: int) -> GameBoard:
    """
    Initialize a GameBoard with the given number of rows and columns.
    Args:
        num_rows (int): Number of rows.
        num_cols (int): Number of columns.
    Returns:
        GameBoard: A num_rows x num_cols board filled with False values.
    """
    if not isinstance(num_rows, int) or num_rows <= 0:
        raise ValueError("num_rows must be a positive integer.")
    if not isinstance(num_cols, int) or num_cols <= 0:
        raise ValueError("num_cols must be a positive integer.")

    # TODO: implement
    new_board = []
    for _ in range(num_rows):
        new_board.append([False] * num_cols)
    return new_board


def update_cell(board: GameBoard, r: int, c: int) -> bool:
    """
    Determine the next state of the cell at (r, c).
    Args:
        board (GameBoard): The current game board.
        r (int): Row index.
        c (int): Column index.
    Returns:
        bool: True if alive next generation, False otherwise.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty GameBoard.")
    if not isinstance(r, int) or not isinstance(c, int):
        raise ValueError("r and c must be integers.")

    # TODO: implement
    live_neighbors = count_live_neighbors(board, r, c)
    if board[r][c]:
        return live_neighbors == 2 or live_neighbors == 3
    else:
        return live_neighbors == 3


def count_live_neighbors(board: GameBoard, r: int, c: int) -> int:
    """
    Count live neighbors of board[r][c].
    Args:
        board (GameBoard): The current game board.
        r (int): Row index.
        c (int): Column index.
    Returns:
        int: Number of live neighbors.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty GameBoard.")

    # TODO: implement
    live_neighbors = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            if in_field(board, r + dr, c + dc):
                live_neighbors += board[r + dr][c + dc]

    return live_neighbors


def in_field(board: GameBoard, i: int, j: int) -> bool:
    """
    Check if the given (i, j) indices are within the board.
    Args:
        board (GameBoard): The current game board.
        i (int): Row index.
        j (int): Column index.
    Returns:
        bool: True if inside the board, False otherwise.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty GameBoard.")
    if not isinstance(i, int) or not isinstance(j, int):
        raise ValueError("i and j must be integers.")

    # TODO: implement
    num_rows = len(board)
    num_cols = len(board[0])
    if 0 <= i < num_rows and 0 <= j < num_cols:
        return True
    return False
