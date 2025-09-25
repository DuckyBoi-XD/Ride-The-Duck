#!/usr/bin/env python3
"""
Entry point for the ride-the-duck package.
This allows the package to be run with:
- python -m ride_the_duck
- ride-the-duck (after pip install)
- RTD (after pip install)
"""

# CRITICAL: Set up mocks IMMEDIATELY before any other code
import sys
import os

# Windows compatibility - must be the FIRST thing that runs
if os.name == "nt":
    import types
    
    # Ensure termios mock is available before ANY other imports
    if 'termios' not in sys.modules:
        termios = types.ModuleType('termios')
        termios.TCSADRAIN = 1
        termios.TCSAFLUSH = 2
        termios.TCSANOW = 0
        termios.tcgetattr = lambda fd: [0, 0, 0, 0, 0, 0, []]
        termios.tcsetattr = lambda fd, when, attrs: None
        sys.modules['termios'] = termios
    
    if 'tty' not in sys.modules:
        tty = types.ModuleType('tty')
        tty.setraw = lambda fd, when=2: None
        tty.setcbreak = lambda fd, when=2: None
        sys.modules['tty'] = tty

def console_entry():
    """Entry point for console commands (ride-the-duck, RTD)."""
    if os.name == "nt":
        print("Running on Windows - terminal compatibility enabled.")
    
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