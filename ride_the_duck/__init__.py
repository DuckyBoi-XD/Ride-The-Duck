"""
Ride the Duck - A terminal-based gambling card game.

A Python package that brings the classic "Ride The Bus" drinking game
to your terminal as a gambling game with save files, statistics, and
colorful ASCII art.
"""

__version__ = "1.0.0"
__author__ = "Braeden Sy Tan"
__email__ = "braedenjairsytan@icloud.com"

# Import main function when package is imported
try:
    from .main import main
    __all__ = ["main"]
except ImportError:
    # Handle case where main module isn't available during development
    __all__ = []