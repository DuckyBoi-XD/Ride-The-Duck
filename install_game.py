#!/usr/bin/env python3
"""Simple installer for Ride The Duck with PATH setup."""

import subprocess
import sys
import os
from pathlib import Path

def main():
    print("🦆 Installing Ride The Duck...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--user", "ride-the-duck"], 
                      check=True)
        print("✅ Package installed successfully!")
        
        # Set up PATH persistence
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        user_bin = Path.home() / "Library" / "Python" / python_version / "bin"
        
        # Determine shell config file
        shell = os.environ.get("SHELL", "").split("/")[-1]
        home = Path.home()
        
        if shell == "zsh":
            shell_config = home / ".zshrc"
        elif shell == "bash":
            bash_profile = home / ".bash_profile"
            shell_config = bash_profile if bash_profile.exists() else home / ".bashrc"
        else:
            shell_config = home / ".profile"
        
        # Check if PATH is already configured
        path_line = f'export PATH="{user_bin}:$PATH"'
        try:
            if shell_config.exists():
                content = shell_config.read_text()
                if str(user_bin) not in content:
                    with shell_config.open("a") as f:
                        f.write("\n# Added by Ride The Duck installer\n")
                        f.write(f"{path_line}\n")
                    print(f"✅ PATH added to {shell_config}")
                else:
                    print("✅ PATH already configured")
            else:
                # Create the config file
                with shell_config.open("w") as f:
                    f.write("# Added by Ride The Duck installer\n")
                    f.write(f"{path_line}\n")
                print(f"✅ Created {shell_config} with PATH")
        except (OSError, PermissionError) as e:
            print(f"⚠️  Could not modify shell config: {e}")
            print("You can manually add this to your shell config:")
            print(f"  {path_line}")
        
        print("\nYou can now run the game with:")
        print("  python -m ride_the_duck  (works immediately)")
        print("  ride-the-duck           (after restarting terminal)")
        print("  RTD                     (after restarting terminal)")
        print("\n⚠️  Please restart your terminal for PATH changes to take effect!")
        print("Happy gaming! 🦆")
        return 0
    except subprocess.CalledProcessError:
        print("❌ Installation failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())