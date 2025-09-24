#!/usr/bin/env python3
"""
Entry point for running Ride the Duck as a module.
Usage: python -m ride_the_duck or ride-the-duck
"""

def console_entry():
    """Console script entry point for the game."""
    try:
        from .mainGame import main
        main()
    except ImportError:
        # Fallback for direct execution
        try:
            import mainGame
            mainGame.main()
        except ImportError:
            print("Error: Could not import mainGame module.")
            print("Please ensure the game files are properly installed.")
            import sys
            sys.exit(1)

if __name__ == "__main__":
    console_entry()