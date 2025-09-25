#!/usr/bin/env python3
"""
Entry point for the ride-the-duck package.
This allows the package to be run with:
- python -m ride_the_duck
- ride-the-duck (after pip install)
- RTD (after pip install)
"""

import sys

def console_entry():
    """Entry point for console commands (ride-the-duck, RTD)."""
    try:
        from .mainGame import main as game_main
        game_main()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    """Main entry point when called as python -m ride_the_duck."""
    console_entry()

if __name__ == "__main__":
    main()