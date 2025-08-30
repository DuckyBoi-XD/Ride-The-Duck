#!/usr/bin/env python3
"""
Demo of different ways to print colored text in Python
"""

# Method 1: ANSI Escape Codes (works on most terminals)
class Colors:
    # Text colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    
    # Background colors
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    
    # Reset
    RESET = '\033[0m'  # Reset to default

def demo_ansi_colors():
    print("=== ANSI Escape Codes Demo ===")
    print(f"{Colors.RED}This is red text{Colors.RESET}")
    print(f"{Colors.GREEN}This is green text{Colors.RESET}")
    print(f"{Colors.YELLOW}This is yellow text{Colors.RESET}")
    print(f"{Colors.BLUE}This is blue text{Colors.RESET}")
    print(f"{Colors.MAGENTA}This is magenta text{Colors.RESET}")
    print(f"{Colors.CYAN}This is cyan text{Colors.RESET}")
    
    # Combining styles
    print(f"{Colors.BOLD}{Colors.RED}Bold red text{Colors.RESET}")
    print(f"{Colors.UNDERLINE}{Colors.GREEN}Underlined green text{Colors.RESET}")
    print(f"{Colors.BG_YELLOW}{Colors.BLACK}Black text on yellow background{Colors.RESET}")
    print()

def demo_colorama():
    print("=== Colorama Demo ===")
    from colorama import Fore, Back, Style, init
    init(autoreset=True)  # Automatically reset colors after each print
    
    print(Fore.RED + "Red text with colorama")
    print(Fore.GREEN + "Green text with colorama")
    print(Fore.BLUE + Style.BRIGHT + "Bright blue text")
    print(Back.YELLOW + Fore.BLACK + "Black text on yellow background")
    print(Style.DIM + "Dim text")
    print()

def colored_print(text, color='white', bg_color=None, style=None):
    """Helper function to print colored text"""
    color_codes = {
        'black': '\033[90m', 'red': '\033[91m', 'green': '\033[92m',
        'yellow': '\033[93m', 'blue': '\033[94m', 'magenta': '\033[95m',
        'cyan': '\033[96m', 'white': '\033[97m'
    }
    
    bg_codes = {
        'black': '\033[100m', 'red': '\033[101m', 'green': '\033[102m',
        'yellow': '\033[103m', 'blue': '\033[104m', 'magenta': '\033[105m',
        'cyan': '\033[106m', 'white': '\033[107m'
    }
    
    style_codes = {
        'bold': '\033[1m', 'dim': '\033[2m', 'italic': '\033[3m',
        'underline': '\033[4m', 'blink': '\033[5m'
    }
    
    # Build the color string
    color_string = ""
    if style and style in style_codes:
        color_string += style_codes[style]
    if bg_color and bg_color in bg_codes:
        color_string += bg_codes[bg_color]
    if color in color_codes:
        color_string += color_codes[color]
    
    print(f"{color_string}{text}\033[0m")

def demo_helper_function():
    print("=== Helper Function Demo ===")
    colored_print("This is red text", 'red')
    colored_print("This is green text", 'green')
    colored_print("Bold blue text", 'blue', style='bold')
    colored_print("White text on red background", 'white', 'red')
    colored_print("Underlined yellow text", 'yellow', style='underline')
    print()

if __name__ == "__main__":
    demo_ansi_colors()
    demo_colorama()
    demo_helper_function()
    
    # Example for your game
    print("=== Game Examples ===")
    print(f"{Colors.BOLD}{Colors.CYAN}🎰RIDE THE DUCK🎰{Colors.RESET}")
    print(f"{Colors.GREEN}💰 Money: $500{Colors.RESET}")
    print(f"{Colors.RED}♥️ Hearts{Colors.RESET} {Colors.BLACK}♠️ Spades{Colors.RESET}")
    print(f"{Colors.RED}♦️ Diamonds{Colors.RESET} {Colors.BLACK}♣️ Clubs{Colors.RESET}")
