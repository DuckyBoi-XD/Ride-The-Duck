#!/bin/bash
# Simple installer for Ride The Duck with PATH setup

set -e  # Exit on any error

echo "🦆 Installing Ride The Duck..."

# Try pipx first, then fallback to pip --user
echo "📦 Trying pipx installation (recommended)..."
if command -v pipx >/dev/null 2>&1; then
    if pipx install ride-the-duck >/dev/null 2>&1; then
        echo "✅ Package installed successfully with pipx!"
        
        # Verify the installation worked and find where pipx installed it
        PIPX_BIN_DIR="$HOME/.local/bin"
        
        # Check common pipx bin locations
        if [[ ! -d "$PIPX_BIN_DIR" ]]; then
            # Try alternative pipx bin directory
            PIPX_BIN_DIR="$(pipx environment --value PIPX_BIN_DIR 2>/dev/null || echo "$HOME/.local/bin")"
        fi
        
        echo "📍 Checking for commands in $PIPX_BIN_DIR"
        if [[ -f "$PIPX_BIN_DIR/RTD" ]]; then
            echo "✅ RTD command found at $PIPX_BIN_DIR/RTD"
        else
            echo "⚠️  RTD command not found in $PIPX_BIN_DIR"
            echo "📍 Available ride-the-duck commands:"
            ls -la "$PIPX_BIN_DIR" 2>/dev/null | grep -E "(ride|RTD)" || echo "   No ride-the-duck commands found"
        fi
        
        # Check if pipx bin directory is in PATH
        if [[ ":$PATH:" != *":$PIPX_BIN_DIR:"* ]]; then
            echo "🔧 Adding pipx bin directory to PATH..."
            export PATH="$PIPX_BIN_DIR:$PATH"
            
            # Add to shell config for persistence
            SHELL_NAME=$(basename "$SHELL")
            if [[ "$SHELL_NAME" == "zsh" ]]; then
                SHELL_RC="$HOME/.zshrc"
            elif [[ "$SHELL_NAME" == "bash" ]]; then
                SHELL_RC="$HOME/.bashrc"
            else
                SHELL_RC="$HOME/.profile"
            fi
            
            if ! grep -q "$PIPX_BIN_DIR" "$SHELL_RC" 2>/dev/null; then
                if echo "export PATH=\"$PIPX_BIN_DIR:\$PATH\"" >> "$SHELL_RC" 2>/dev/null; then
                    echo "✅ Added pipx PATH to $SHELL_RC"
                fi
            fi
        else
            echo "✅ pipx bin directory already in PATH"
        fi
        
        echo ""
        echo "You can now run the game with:"
        echo "  ride-the-duck"
        echo "  RTD" 
        echo "  python3 -m ride_the_duck"
        echo ""
        echo "Happy gaming! 🦆"
        exit 0
    else
        echo "⚠️  pipx install from local directory failed, trying pip --user..."
    fi
else
    echo "⚠️  pipx not found, trying pip --user..."
fi

# Install the package with pip --user
python3 -m pip install --user ride-the-duck

# Set up PATH
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
USER_BIN_PATH="$HOME/Library/Python/$PYTHON_VERSION/bin"

# Add to current session
export PATH="$USER_BIN_PATH:$PATH"

# Add to shell config for persistence
SHELL_NAME=$(basename "$SHELL")
if [[ "$SHELL_NAME" == "zsh" ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$SHELL_NAME" == "bash" ]]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.profile"
fi

if ! grep -q "$USER_BIN_PATH" "$SHELL_RC" 2>/dev/null; then
    if echo "export PATH=\"$USER_BIN_PATH:\$PATH\"" >> "$SHELL_RC" 2>/dev/null; then
        echo "✅ Added to $SHELL_RC for future sessions"
    else
        echo "⚠️  Could not modify $SHELL_RC - you may need to add manually:"
        echo "export PATH=\"$USER_BIN_PATH:\$PATH\""
    fi
else
    echo "✅ PATH already configured in $SHELL_RC"
fi

echo "✅ Installation complete!"
echo ""
echo "You can now run the game with:"
echo "  ride-the-duck"
echo "  RTD"
echo "  python3 -m ride_the_duck"
echo ""
echo "Happy gaming! 🦆"