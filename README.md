# 🦆 Ride The Duck

A terminal-based gambling card game inspired by "Ride The Bus"!

## 🚀 Quick Setup (Recommended)

### Option 1: Automatic Setup
```bash
curl -sSL https://raw.githubusercontent.com/DuckyBoi-XD/Ride-The-Duck/main/setup_game.sh | bash
```

### Option 2: Manual Installation
```bash
pip install ride-the-duck
```

⚠️ **If commands don't work after installation**, add Python's user bin to your PATH:

**For macOS/Linux:**
```bash
echo 'export PATH="$HOME/Library/Python/$(python3 -c "import sys; print(f\"{sys.version_info.major}.{sys.version_info.minor}\")")/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## 🎮 How to Play

After installation, start the game with any of these commands:

```bash
ride-the-duck    # Main command
RTD              # Short alias  
python -m ride_the_duck  # Module execution (always works)
```

## 🎯 Game Rules

Ride The Duck is a card-based gambling game where you:
1. Make predictions about upcoming cards
2. Bet virtual chips on your guesses
3. Try to "ride the bus" without losing all your chips!

## 🛠️ Development

To contribute to the project:

```bash
git clone https://github.com/DuckyBoi-XD/Ride-The-Duck.git
cd Ride-The-Duck
pip install -e .
```

## 📝 License

MIT License - feel free to modify and share!
