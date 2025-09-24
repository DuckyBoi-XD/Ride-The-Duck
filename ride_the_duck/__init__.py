"""
Ride the Duck - A terminal-based gambling card game.
"""

__version__ = "1.0.3"
__author__ = "Braeden Sy Tan"

# Ensure mainGame is importable
try:
    from . import mainGame
    __all__ = ['mainGame']
except ImportError:
    # Fallback if mainGame can't be imported
    __all__ = []

from .mainGame import main

__all__ = ["main"]