#!/usr/bin/env python3
"""
Entry point for the ride-the-duck package.
This allows the package to be run with:
- python -m ride_the_duck
- ride-the-duck (after pip install)
- RTD (after pip install)
"""

import sys
import os

# Set up Windows compatibility for Unix-specific modules BEFORE any other imports
if os.name == "nt":
    import types
    
    # Mock termios with all common attributes and functions
    if 'termios' not in sys.modules:
        termios_mock = types.ModuleType('termios')
        
        # Constants
        for attr, value in [
            ('TCSADRAIN', 1), ('TCSAFLUSH', 2), ('TCSANOW', 0),
            ('ECHO', 8), ('ECHOE', 16), ('ECHOK', 32), ('ECHONL', 64),
            ('ICANON', 2), ('IEXTEN', 32768), ('ISIG', 1),
            ('VMIN', 6), ('VTIME', 5), ('VINTR', 0), ('VQUIT', 1),
            ('VERASE', 2), ('VKILL', 3), ('VEOF', 4), ('VSTART', 8),
            ('VSTOP', 9), ('VSUSP', 10), ('INPCK', 16), ('ISTRIP', 32),
            ('INLCR', 64), ('IGNCR', 128), ('ICRNL', 256), ('IXON', 1024)
        ]:
            setattr(termios_mock, attr, value)
        
        # Functions
        termios_mock.tcgetattr = lambda fd: [0, 0, 0, 0, 0, 0, [b'\x03', b'\x1c', b'\x7f', b'\x15', b'\x04', b'\x00', b'\x01', b'\x00']]
        termios_mock.tcsetattr = lambda fd, when, attrs: None
        termios_mock.tcsendbreak = lambda fd, duration: None
        termios_mock.tcdrain = lambda fd: None
        termios_mock.tcflush = lambda fd, queue: None
        termios_mock.tcflow = lambda fd, action: None
        
        sys.modules['termios'] = termios_mock
    
    # Mock tty
    if 'tty' not in sys.modules:
        tty_mock = types.ModuleType('tty')
        tty_mock.setraw = lambda fd, when=2: None
        tty_mock.setcbreak = lambda fd, when=2: None
        sys.modules['tty'] = tty_mock
    
    # Mock other potential Unix modules
    for module_name in ['fcntl', 'select']:
        if module_name not in sys.modules:
            mock_module = types.ModuleType(module_name)
            if module_name == 'fcntl':
                mock_module.fcntl = lambda fd, cmd, arg=0: 0
                mock_module.F_GETFL = 3
                mock_module.F_SETFL = 4
                mock_module.O_NONBLOCK = 2048
            elif module_name == 'select':
                mock_module.select = lambda r, w, x, timeout=None: ([], [], [])
                mock_module.poll = lambda: None
            sys.modules[module_name] = mock_module

def console_entry():
    """Entry point for console commands (ride-the-duck, RTD)."""
    
    if os.name == "nt":
        print("Running on Windows - using compatibility layer for terminal features.")
    
    try:
        from .mainGame import main as game_main
        game_main()
    except ImportError as e:
        error_msg = str(e).lower()
        print(f"Import Error: {e}")
        
        # Provide specific help for common issues
        if "maingame" in error_msg:
            print("\nTroubleshooting:")
            print("1. Ensure mainGame.py exists in the ride_the_duck package")
            print("2. Check that mainGame.py has a 'main' function")
            print("3. Verify package installation: pip list | findstr ride-the-duck")
        elif any(mod in error_msg for mod in ["termios", "tty", "fcntl", "select"]):
            print("\nUnix module compatibility issue detected.")
            print("The mock modules should handle this. Please check your mainGame.py")
            print("for any direct system calls or unsupported operations.")
        
        sys.exit(1)
    except AttributeError as e:
        print(f"Attribute Error: {e}")
        print("This might be due to missing functions in mainGame.py")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("\nFull error details:")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    """Main entry point when called as python -m ride_the_duck."""
    console_entry()

if __name__ == "__main__":
    main()