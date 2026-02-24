import os
import pygame
from datatypes import GameBoard
from functions import count_rows, count_cols


def draw_game_board(
    board: GameBoard,
    live_color: tuple[int, int, int],
    dead_color: tuple[int, int, int],
    cell_width: int,
    scaling_factor: float = 0.8,
) -> pygame.Surface:
    """
    Draws a Game of Life automaton to a pygame.Surface object.

    Parameters:
    - board: 2-D list of booleans (True = alive, False = dead)
    - live_color: tuple of RGB values corresponding to live cells
    - dead_color: tuple of RGB values corresponding to dead cells
    - cell_width: integer representing the number of pixels (wide and tall) to represent a given cell of the game
    - scaling_factor: float representing a multiplier that is multiplied by the radius of the cell when we draw it (to prevent touching)

    Output:
    - pygame.Surface: canvas object corresponding to drawing the Game of Life board using the given parameters.
    """
    if not isinstance(cell_width, int) or cell_width <= 0:
        raise ValueError("Error: cell_width parameter has inappropriate type or value.")
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("Error: board has inappropriate type or no rows.")
    # colors too

    # first thing we do is make the surface
    width = cell_width * len(board[0])
    height = cell_width * len(board)
    surface = pygame.Surface((width, height))

    # fill the board with the background color, which is dead
    surface.fill(dead_color)

    # range over all the cells in the board, and color each one with the appropriate color
    # note: because the background color is the dead color, I don't need to color the dead cells
    for row in range(len(board)):
        for col in range(len(board[0])):
            # if the cell is alive, draw it!
            if board[row][col]:
                # draw circle: where is the center? Radius?

                radius = scaling_factor * (cell_width / 2)
                # top left coordinates?
                x = col * cell_width + cell_width / 2
                y = row * cell_width + cell_width / 2

                pygame.draw.circle(surface, live_color, (int(x), int(y)), int(radius))

    return surface


def draw_game_boards(
    boards: list[GameBoard], output_prefix: str, cell_width: int
) -> list[pygame.Surface]:
    """
    Draw multiple GameBoards and save them as PNG files.
    Args:
        boards (list[GameBoard]): List of GameBoard objects.
        output_prefix (str): Prefix for output filenames.
        cell_width (int): Pixel width of each cell.
    Returns:
        list[pygame.Surface]: Surfaces drawn for each board.
    """
    if not isinstance(boards, list) or len(boards) == 0:
        raise ValueError("boards must be a non-empty list.")
    if not isinstance(output_prefix, str) or len(output_prefix) == 0:
        raise ValueError("output_prefix must be a non-empty string.")
    if not isinstance(cell_width, int) or cell_width <= 0:
        raise ValueError("cell_width must be a positive integer.")

    surfaces = []
    # ensure the package output directory exists (src/game_of_life/output)
    package_output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(package_output_dir, exist_ok=True)

    for i, board in enumerate(boards):
        surface = draw_game_board(board, (255, 0, 0), (0, 0, 255), cell_width)
        filename = os.path.join(package_output_dir, f"{output_prefix}_gen_{i}.png")
        pygame.image.save(surface, filename)
        surfaces.append(surface)
    return surfaces
