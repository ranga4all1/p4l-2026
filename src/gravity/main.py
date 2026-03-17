"""
CLI entry point for the gravity simulation.

Usage:
    python main.py <scenario_name> <num_gens> <time_step> <canvas_width> <drawing_frequency>

Example:
    python main.py jupiterMoons 2000 0.01 800 5

This will read:   data/jupiterMoons.txt
and write video:  output/jupiterMoons.mp4
"""

import sys
import pygame
from custom_io import read_universe
from gravity import simulate_gravity
from drawing import animate_system
from animate import animate_surfaces

def main():
    print("Building a gravity simulator.")

if __name__ == "__main__":
    main()
