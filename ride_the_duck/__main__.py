#!/usr/bin/env python3
"""
Entry point for running Ride the Duck as a module.
Usage: python -m ride_the_duck or ride-the-duck
"""

def console_entry():
    """Console script entry point for the game."""
    import sys
    import os
    
    # Add current directory to path for imports
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    try:
        from .mainGame import main
        main()
    except ImportError:
        # Fallback for direct execution
        try:
            import mainGame
            mainGame.main()
        except ImportError as e:
            print(f"Error: Could not import mainGame module: {e}")
            print("Please ensure the game files are properly installed.")
            print(f"Looking in directory: {current_dir}")
            sys.exit(1)

if __name__ == "__main__":
    console_entry()