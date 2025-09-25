#!/bin/bash
# Automatic setup script for Ride The Duck
# This script will install the game and set up the PATH so commands work

set -e  # Exit on any error

echo "🦆 Setting up Ride The Duck..."

# Detect shell
SHELL_NAME=$(basename "$SHELL")
if [[ "$SHELL_NAME" == "zsh" ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$SHELL_NAME" == "bash" ]]; then
    if [[ -f "$HOME/.bash_profile" ]]; then
        SHELL_RC="$HOME/.bash_profile"
    else
        SHELL_RC="$HOME/.bashrc"
    fi
else
    echo "⚠️  Unknown shell: $SHELL_NAME"
    SHELL_RC="$HOME/.profile"
fi

echo "Detected shell: $SHELL_NAME"
echo "Shell config: $SHELL_RC"

# Install the package
echo "📦 Installing ride-the-duck package..."
python3 -m pip install --user ride-the-duck

# Detect Python version and set up PATH
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
USER_BIN_PATH="$HOME/Library/Python/$PYTHON_VERSION/bin"

echo "Python version: $PYTHON_VERSION"
echo "User bin path: $USER_BIN_PATH"

# Check if PATH is already in shell config
if grep -q "$USER_BIN_PATH" "$SHELL_RC" 2>/dev/null; then
    echo "✅ PATH already configured in $SHELL_RC"
else
    echo "🔧 Adding Python user bin to PATH..."
    echo "" >> "$SHELL_RC"
    echo "# Added by Ride The Duck setup" >> "$SHELL_RC"
    echo "export PATH=\"\$HOME/Library/Python/$PYTHON_VERSION/bin:\$PATH\"" >> "$SHELL_RC"
    echo "✅ PATH updated in $SHELL_RC"
fi

# Source the shell config to update current session
if [[ -f "$SHELL_RC" ]]; then
    echo "🔄 Reloading shell configuration..."
    source "$SHELL_RC" 2>/dev/null || echo "⚠️  Please restart your terminal or run: source $SHELL_RC"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "You can now run the game using any of these commands:"
echo "  ride-the-duck"
echo "  RTD"
echo "  python3 -m ride_the_duck"
echo ""
echo "If the commands don't work immediately, please restart your terminal."
echo "Happy gaming! 🦆🎮"