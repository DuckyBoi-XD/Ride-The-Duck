"""
Ride The Duck - A terminal-based gambling card game.

A Python implementation of the popular drinking/gambling card game
"Ride The Bus" (also known as "Up The River, Down The River").
"""

try:
    from ._version import version as __version__
except ImportError:
    # Fallback for development installs
    __version__ = "unknown"

# Make main function available at package level
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

def test_import():
    """Test function to verify package can be imported correctly."""
    print(f"ride_the_duck version: {__version__}")
    print("Package imported successfully!")
    return True