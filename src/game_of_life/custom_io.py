from datatypes import GameBoard


def read_board_from_file(filename: str) -> GameBoard:
    """
    Reads a CSV file representing a Game of Life board.
    "1" = alive (True), "0" = dead (False).
    Args:
        filename (str): The name of the CSV file.
    Returns:
        GameBoard: Parsed board.
    """
    if not isinstance(filename, str) or len(filename) == 0:
        raise ValueError("filename must be a non-empty string.")

    # TODO: implement
    with open(filename, "r") as f:
        lines = f.readlines()

    board: GameBoard = []
    for line in lines:
        elements = line.strip().split(",")
        row = set_row_values(elements)
        board.append(row)

    return board


def set_row_values(line_elements: list[str]) -> list[bool]:
    """
    Convert a list of "0"/"1" strings into booleans.
    Args:
        line_elements (list[str]): Strings "0"/"1".
    Returns:
        list[bool]: Row with True/False.
    """
    if not isinstance(line_elements, list) or len(line_elements) == 0:
        raise ValueError("line_elements must be a non-empty list.")

    # TODO: implement
    row = [True if element == "1" else False for element in line_elements]
    return row
