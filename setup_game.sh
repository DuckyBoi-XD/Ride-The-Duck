#!/bin/bash
# Simple installer for Ride The Duck with PATH setup

set -e  # Exit on any error

echo "🦆 Installing Ride The Duck..."

# Install the package
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