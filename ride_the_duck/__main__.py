#!/usr/bin/env python3
"""
Entry point for the ride-the-duck package.
This allows the package to be run with:
- python -m ride_the_duck
- ride-the-duck (after pip install)
- RTD (after pip install)
"""

def console_entry():
    """Entry point for console commands (ride-the-duck, RTD)."""
    import sys
    import os
    
    # Check if we're on Windows and warn about termios
    if os.name == "nt":
        print("Running on Windows - using basic input methods.")
    
    try:
        # Try to import and run the game
        from .mainGame import main as game_main
        game_main()
    except ModuleNotFoundError as e:
        if "termios" in str(e):
            print("Windows detected: termios module not available.")
            print("Your game needs to be updated to support Windows.")
            print("Consider using cross-platform libraries or conditional imports.")
            sys.exit(1)
        else:
            print(f"Module not found: {e}")
            sys.exit(1)
    except ImportError as e:
        error_str = str(e).lower()
        if "termios" in error_str or "tty" in error_str or "no module named 'termios'" in error_str:
            print("Warning: Advanced terminal features not available on Windows.")
            print("The termios module is Unix/Linux specific and not available on Windows.")
            print("Please ensure your mainGame.py has Windows compatibility fallbacks.")
            print("\nTo fix this, modify your mainGame.py to handle Windows systems:")
            print("- Use try/except blocks around termios imports")
            print("- Provide Windows-compatible alternatives (like msvcrt)")
            sys.exit(1)
        else:
            print(f"Error importing mainGame: {e}")
            print("Please ensure the package is properly installed.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Please report this issue.")
        sys.exit(1)

def main():
    """Main entry point when called as python -m ride_the_duck."""
    console_entry()

if __name__ == "__main__":
    main()