#!/bin/bash
# One-time installer for Ride The Duck
# After running this, just type: RTD

set -e

echo "🦆 Installing Ride The Duck..."

# Function to add directory to PATH
add_to_path() {
    local dir="$1"
    local shell_rc
    
    # Add to current session
    export PATH="$dir:$PATH"
    
    # Add to shell config for future sessions
    case "$(basename "$SHELL")" in
        zsh) shell_rc="$HOME/.zshrc" ;;
        bash) shell_rc="$HOME/.bashrc" ;;
        *) shell_rc="$HOME/.profile" ;;
    esac
    
    if ! grep -q "$dir" "$shell_rc" 2>/dev/null; then
        echo "export PATH=\"$dir:\$PATH\"" >> "$shell_rc" 2>/dev/null
    fi
}

# Try pipx first (best option)
if command -v pipx >/dev/null 2>&1; then
    pipx install ride-the-duck >/dev/null 2>&1 || true
    add_to_path "$HOME/.local/bin"
    echo "✅ Installed! You can now run: RTD"
    exit 0
fi

# Fallback to pip --user
python3 -m pip install --user ride-the-duck >/dev/null 2>&1
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
add_to_path "$HOME/Library/Python/$python_version/bin"

echo "✅ Installed! You can now run: RTD"
echo "💡 You may need to restart your terminal first"
