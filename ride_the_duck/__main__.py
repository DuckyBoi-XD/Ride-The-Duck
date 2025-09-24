#!/usr/bin/env python3
"""
Entry point for running Ride the Duck as a module.
Usage: python -m ride_the_duck
"""

if __name__ == "__main__":
    try:
        from .main import main
        main()
    except ImportError:
        # Fallback for direct execution
        import sys
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, current_dir)
        import main as main_module  # type: ignore
        main_module.main()  # type: ignore