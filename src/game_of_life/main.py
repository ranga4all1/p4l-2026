import sys
import pygame
from custom_io import read_board_from_file
from functions import play_game_of_life
from drawing import draw_game_board, draw_game_boards
from animate import animate_image_files

# Usage example:
#   Run from the repository root to generate frames and an MP4 animation:
#
#   python3 src/game_of_life/main.py src/game_of_life/boards/rPentomino.csv output 8 50
#
#   This will:
#   - read the initial board CSV at `src/game_of_life/boards/rPentomino.csv`
#   - write PNG frames to `src/game_of_life/output/` with prefix `output_gen_<n>.png`
#   - create `src/game_of_life/output/output.mp4` (10 FPS) after frames are written
#


def main():
    print("Coding the Game of Life!")

    if len(sys.argv) != 5:
        raise ValueError(
            "Usage: python main.py initial_board.csv output_prefix cell_width num_gens"
        )

    input_csv = sys.argv[1]
    output_prefix = sys.argv[2]
    cell_width = int(sys.argv[3])
    num_gens = int(sys.argv[4])

    print("Parameters read in successfully!")
    # TODO: implement simulation, drawing, video writing
    initial_board = read_board_from_file(input_csv)
    game_boards = play_game_of_life(initial_board, num_gens)
    draw_game_boards(game_boards, output_prefix, cell_width)
    # create an MP4 animation from the generated PNG frames
    try:
        video_path = f"src/game_of_life/output/{output_prefix}.mp4"
        print(f"Writing animation to {video_path}...")
        animate_image_files(output_prefix, video_path, fps=10)
        print("Animation written successfully.")
    except Exception as e:
        print(f"Warning: failed to create animation: {e}")


if __name__ == "__main__":
    main()
