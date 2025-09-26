"""Ride The Duck - A terminal-based card gambling game."""

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

try:
    from .mainGame import main
except ImportError as e:
    def main():
        """Fallback main function if mainGame can't be imported."""
        print(f"Error: Could not import mainGame module: {e}")
        print("Please check that all required files are present.")
        import sys
        sys.exit(1)

__all__ = ["main", "__version__"]