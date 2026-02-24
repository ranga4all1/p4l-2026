import glob
import os
import re
import imageio
import pygame
import numpy


def animate_surfaces(surfaces: list[pygame.Surface], video_path: str) -> None:
    """
    Convert a list of Pygame surfaces into an MP4 video.

    Args:
        surfaces (list[pygame.Surface]):
            A sequence of frames to encode.
        video_path (str):
            Output path for the video file (e.g., "output.mp4").

    The video is written using H.264 encoding at 10 FPS.
    """
    writer = imageio.get_writer(video_path, fps=10, codec="libx264", quality=8)

    for surface in surfaces:
        frame = pygame_surface_to_numpy(surface)
        writer.append_data(frame)

    writer.close()


def pygame_surface_to_numpy(surface: pygame.Surface) -> numpy.ndarray:
    """
    Convert a Pygame Surface to a NumPy RGB image array.

    Returns:
        numpy.ndarray: The frame as (height, width, 3) uint8 RGB.
    """

    # get a numpy array associated with the surface and swap its axes
    return pygame.surfarray.array3d(surface).swapaxes(0, 1)


def animate_image_files(output_prefix: str, video_path: str, fps: int = 10) -> None:
    """
    Read generated PNG frames from the `output/` directory matching
    ``{output_prefix}_gen_*.png`` and write them into an MP4 video.

    Args:
        output_prefix: Prefix used when images were written (the same
            prefix passed to `draw_game_boards`).
        video_path: Path to write the resulting video (e.g. "out.mp4").
        fps: Frames per second for the output video.
    """
    # look for frames in the package's output folder first, then cwd/output
    script_dir = os.path.dirname(__file__)
    search_dirs = [
        os.path.join(script_dir, "output"),
        os.path.join(os.getcwd(), "output"),
    ]

    files = []
    for d in search_dirs:
        pattern = os.path.join(d, f"{output_prefix}_gen_*.png")
        files = glob.glob(pattern)
        if files:
            break

    if not files:
        searched = ", ".join(search_dirs)
        raise FileNotFoundError(
            f"No files found for prefix '{output_prefix}'. Searched: {searched}"
        )

    # sort by the generation number embedded in the filename
    def gen_key(path: str) -> int:
        m = re.search(r"_gen_(\d+)\.png$", os.path.basename(path))
        return int(m.group(1)) if m else -1

    files.sort(key=gen_key)

    writer = imageio.get_writer(video_path, fps=fps, codec="libx264", quality=8)
    try:
        for fname in files:
            frame = imageio.imread(fname)
            # imageio returns HxWxC already; append directly
            writer.append_data(frame)
    finally:
        writer.close()


if __name__ == "__main__":
    # simple CLI: animate files with prefix and output path
    import sys

    if len(sys.argv) < 3:
        print("Usage: python animate.py <output_prefix> <video_path> [fps]")
        raise SystemExit(1)

    prefix = sys.argv[1]
    out = sys.argv[2]
    fps = int(sys.argv[3]) if len(sys.argv) >= 4 else 10
    animate_image_files(prefix, out, fps=fps)
