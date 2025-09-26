#!/bin/bash
# Simple installer for Ride The Duck with pipx/pip support

set -e

echo "🦆 Installing Ride The Duck..."

# Function to add directory to PATH
add_to_path() {
    local dir="$1"
    local shell_rc
    
    # Add to current session
    export PATH="$dir:$PATH"
    
    # Add to shell config
    case "$(basename "$SHELL")" in
        zsh) shell_rc="$HOME/.zshrc" ;;
        bash) shell_rc="$HOME/.bashrc" ;;
        *) shell_rc="$HOME/.profile" ;;
    esac
    
    if ! grep -q "$dir" "$shell_rc" 2>/dev/null; then
        echo "export PATH=\"$dir:\$PATH\"" >> "$shell_rc" 2>/dev/null && \
            echo "✅ Added $dir to $shell_rc" || \
            echo "⚠️  Could not modify $shell_rc"
    fi
}

# Try pipx first
if command -v pipx >/dev/null 2>&1 && pipx install ride-the-duck >/dev/null 2>&1; then
    echo "✅ Installed with pipx!"
    
    # Find where pipx put the commands
    for dir in "$HOME/.local/bin" "$HOME/.local/share/man"; do
        if [[ -f "$dir/RTD" ]]; then
            echo "✅ Found RTD at $dir/RTD"
            add_to_path "$dir"
            echo -e "\nRun: RTD or ride-the-duck or python3 -m ride_the_duck"
            echo "Happy gaming! 🦆"
            exit 0
        fi
    done
fi

# Fallback to pip --user
echo "📦 Installing with pip --user..."
python3 -m pip install --user ride-the-duck

# Set up PATH for pip --user
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
user_bin="$HOME/Library/Python/$python_version/bin"
add_to_path "$user_bin"

echo -e "\n✅ Installation complete!"
echo "Run: RTD or ride-the-duck or python3 -m ride_the_duck"
echo "Happy gaming! 🦆"