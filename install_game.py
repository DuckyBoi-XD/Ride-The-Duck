#!/usr/bin/env python3
"""
Simple Python installer for Ride The Duck that handles PATH setup automatically.
Run this script to install and configure the game.
"""

import subprocess
import sys
import os
from pathlib import Path

def get_user_bin_path():
    """Get the user's Python bin path."""
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    if sys.platform == "darwin":  # macOS
        return Path.home() / "Library" / "Python" / python_version / "bin"
    elif sys.platform.startswith("linux"):  # Linux
        return Path.home() / ".local" / "bin"
    else:  # Windows
        return Path.home() / "AppData" / "Local" / "Programs" / "Python" / f"Python{python_version.replace('.', '')}" / "Scripts"

def get_shell_config():
    """Get the shell configuration file."""
    shell = os.environ.get("SHELL", "").split("/")[-1]
    home = Path.home()
    
    if shell == "zsh":
        return home / ".zshrc"
    elif shell == "bash":
        bash_profile = home / ".bash_profile"
        return bash_profile if bash_profile.exists() else home / ".bashrc"
    else:
        return home / ".profile"

def install_package():
    """Install the ride-the-duck package."""
    print("📦 Installing ride-the-duck...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--user", "ride-the-duck"], 
                      check=True, capture_output=True, text=True)
        print("✅ Package installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def setup_path():
    """Set up PATH in shell configuration."""
    user_bin = get_user_bin_path()
    shell_config = get_shell_config()
    
    print(f"🔧 Setting up PATH...")
    print(f"User bin path: {user_bin}")
    print(f"Shell config: {shell_config}")
    
    # Check if already configured
    if shell_config.exists():
        content = shell_config.read_text()
        if str(user_bin) in content:
            print("✅ PATH already configured!")
            return True
    
    # Add to PATH
    path_line = f'export PATH="{user_bin}:$PATH"'
    try:
        with shell_config.open("a") as f:
            f.write(f"\n# Added by Ride The Duck installer\n")
            f.write(f"{path_line}\n")
        print("✅ PATH configured in shell config!")
        return True
    except Exception as e:
        print(f"⚠️  Could not modify {shell_config}: {e}")
        return False

def test_installation():
    """Test if the game can be imported."""
    try:
        subprocess.run([sys.executable, "-c", "import ride_the_duck; print('✅ Import test passed!')"], 
                      check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError:
        print("⚠️  Import test failed - package may not be properly installed")
        return False

def main():
    """Main installer function."""
    print("🦆 Ride The Duck Installer")
    print("=" * 30)
    
    # Install package
    if not install_package():
        return 1
    
    # Test import
    test_installation()
    
    # Set up PATH
    setup_path()
    
    user_bin = get_user_bin_path()
    print("\n🎉 Installation complete!")
    print("\nYou can now run the game using:")
    print("  python -m ride_the_duck  (always works)")
    print("  ride-the-duck           (after restarting terminal)")
    print("  RTD                     (after restarting terminal)")
    print(f"\nOr directly: {user_bin}/ride-the-duck")
    print("\n⚠️  Please restart your terminal for PATH changes to take effect!")
    print("Happy gaming! 🦆🎮")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())