#!/usr/bin/env python3
"""
Entry point for running Ride the Duck as a module.
Usage: python -m ride_the_duck or ride-the-duck
"""

def console_entry():
    """Console script entry point for the game."""
    import sys
    import os
    
    # Add current package directory to Python path as fallback
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    # Try multiple import strategies
    main_func = None
    
    # Strategy 1: Relative import (when run as module)
    try:
        from .mainGame import main
        main_func = main
    except ImportError:
        pass
    
    # Strategy 2: Absolute import (when installed via pip)
    if main_func is None:
        try:
            from ride_the_duck.mainGame import main
            main_func = main
        except ImportError:
            pass
    
    # Strategy 3: Direct import (fallback)
    if main_func is None:
        try:
            import mainGame
            main_func = mainGame.main
        except ImportError:
            pass
    
    # Strategy 4: Try with full path import
    if main_func is None:
        try:
            sys.path.insert(0, os.path.join(current_dir, '..'))
            from ride_the_duck import mainGame
            main_func = mainGame.main
        except ImportError:
            pass
    
    # If all strategies failed, provide detailed error
    if main_func is None:
        print("Error: Could not import mainGame module using any method.")
        print("Tried the following import strategies:")
        print("  1. from .mainGame import main")
        print("  2. from ride_the_duck.mainGame import main") 
        print("  3. import mainGame")
        print("  4. Full path import")
        print(f"Current directory: {current_dir}")
        print(f"Python path: {sys.path[:3]}...")
        print("Please ensure the game files are properly installed with 'pip install -e .'")
        sys.exit(1)
    
    # Run the game
    try:
        main_func()
    except Exception as e:
        print(f"Error running game: {e}")
        sys.exit(1)

if __name__ == "__main__":
    console_entry()