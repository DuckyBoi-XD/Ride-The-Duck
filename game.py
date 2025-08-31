#----Import Python Packages----#
import json
import base64
import os

#linux + macos
import sys
import tty
import termios

'''windows
import msvcrt
'''
#----Import Python Packages----#

#----Colours----#
class Colours:
    '''colours for texts'''
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    
    RESET = '\033[0m'
#----Colours----#

#----Save File Money----#
def load_game(filename="savefile.json"): # access save file -JSON
    '''loading save file - returns both money and name'''
    try:
        with open(filename, "rb") as f: # reads file and places value "f"
            encoded_bytes = f.read() # convert value string to bytes "f"
            json_str = base64.b64decode(encoded_bytes).decode('utf-8') # decodes
            data = json.loads(json_str) # changes value to "data"
            print("Save file loaded") # confirm message
            return data.get("money", 500), data.get("name", None) # normal value
    except FileNotFoundError: # New player detection
        print("New player - no save file found") # confirmation message
        return 500, None # starting items (money, name)
    except (ValueError, json.JSONDecodeError, base64.binascii.Error): # corupt detection
        print("Corrupted save file - using defaults") # confirmation message
        return 500, None # reset values (money, name)

def save_game(money, name, filename="savefile.json"): # access save file + values (money, name)
    '''saving game money and name'''
    data = {"money": money, "name": name} # creates dictionary
    json_str = json.dumps(data) # turns into "data" value
    encoded_bytes = base64.b64encode(json_str.encode('utf-8')) # encodes
    with open(filename, "wb") as f: # opens file to prep writing
        f.write(encoded_bytes) # writes
    print(f"Game saved: {name} with ${money}") # confirmation message
#----Save File Money----#

#----Variables----#
USER_WALLET, USER_NAME = load_game()  # Load both money and name from save file
CARD_SUITS = ("S", "D", "H", "C") # creates suits for card deck creation
SUIT_SYMBOLS = {'S': '♠','D': '♦', 'H': '♥', 'C': '♣'}
#----Variables----#

#----Function Variables----#
def LINE():
    ''''creates line spacing'''
    print(f"{Colours.BOLD}{Colours.MAGENTA}======----------================----------======")

def clear_screen():
    ''''clear screen function'''
    os.system('cls' if os.name == 'nt' else 'clear') # function to clear screen

#----Function Variables----#

#----Card Deck----#
CardDeck = {}

for suit in CARD_SUITS:
    for value in range(2, 11):
        CardDeck[f"{suit}{value}"] = value

for suit in CARD_SUITS:
    CardDeck[f"{suit}D"] = 11
    CardDeck[f"{suit}Q"] = 12
    CardDeck[f"{suit}K"] = 13
    CardDeck[f"{suit}A"] = 14
#----Card Deck----#

#----Start Game----#
def start_game():
    LINE()
    print(f"{Colours.BOLD}{Colours.CYAN}🎰 RIDE THE DUCK 🎰{Colours.RESET}\n"
        f"{Colours.GREEN}💰 Your Money: ${USER_WALLET}{Colours.RESET}\n"
        f"{Colours.BLUE}🎉 Welcome to Ride the Duck, a gambling game 🎉")
    if USER_NAME is None:
        print(f"{Colours.YELLOW}🏷️  Your  Name:{Colours.RESET}{Colours.RED} -UNKNOWN-{Colours.RESET}")
    else:
        print(f"{Colours.YELLOW}🏷️  Your  Name:{Colours.RESET}{USER_NAME}")
        
    
#----Start Game----#

#----Main Game Function----#
def main_game():
    '''Ride the Bus game'''
    pass

#----Main Game Function----#

#----Single Key Track----#
# Unix key pressing
def key_press():
    '''single key tracking'''
    fd = sys.stdin.fileno() # sets variable for key input
    old_settings = termios.tcgetattr(fd) # saves the old state of the terminal
    try:
        tty.setraw(sys.stdin.fileno()) # sets terminal in "raw mode" for tracking
        key = sys.stdin.read(1) # reads only 1 keyboard input
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # restores to old state
    return key

'''windows key pressing
def get_keypress():
    if msvcrt.kbhit():
        key = msvcrt.getch()
        return key.decode('utf-8')
    return None
'''
#----Single Key Track----#

#----Arrow Key Track----#
def arrow_key():
    '''reads and looks for arrow press'''
    fd = sys.stdin.fileno() # find  keyboard format
    old_settings = termios.tcgetattr(fd) # saves old terminal
    try:
        tty.setraw(sys.stdin.fileno()) # tunrs on "raw mode"
        key = sys.stdin.read(1) # reads first input
        
        # Check for escape sequence (arrow keys)
        if ord(key) == 27:  # ESC
            key += sys.stdin.read(2)  # Read the next 2 characters (for arrows)
            
        return key
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # restores old settings
#----Arrow Key Track----#

#----Arrow Key Menu System----#
def arrow_menu(options):
    """generic arrow key menu system"""
    selected = 0
    
    while True:
        clear_screen()  # Clear screen for smooth animation
        LINE()
        
        # Display menu options
        for i, option in enumerate(options):
            if i == selected:
                print(f"{Colours.BOLD}{Colours.YELLOW}► {option}{Colours.RESET}")
            else:
                print(f"{Colours.WHITE}  {option}{Colours.RESET}")
        
        LINE()
        print(f"{Colours.MAGENTA}Use ↑↓ arrows, Enter to select, ESC to cancel{Colours.RESET}")
        
        key = arrow_key()
        
        if key == '\x1b[A':  # Up arrow
            clear_screen()
            selected = (selected - 1) % len(options)
            # Screen will clear on next loop iteration
        elif key == '\x1b[B':  # Down arrow
            clear_screen()
            selected = (selected + 1) % len(options)
            # Screen will clear on next loop iteration
        elif ord(key[0]) == 13:  # Enter
            return selected
        elif len(key) == 1 and ord(key) == 27:  # ESC alone
            return -1
#----Arrow Key Menu System----#

#----Main Menu----#
def main_menu():
    """Main game menu with arrow navigation"""
    
    options = [
        "🎮 Play Ride the Duck",
        "📊 View Statistics", 
        "✏️  Change Name",
        "💾 Save Game",
        "🚪 Quit Game"
    ]
    
    while True:
        clear_screen()  # Clear screen for smooth menu display
        LINE()
        print(f"{Colours.BOLD}{Colours.CYAN}🎰 RIDE THE DUCK - MAIN MENU 🎰{Colours.RESET}")
        LINE()
        
        choice = arrow_menu(options)
        
        if choice == 0:  # Play Game
            clear_screen()
            main_game()
        elif choice == 1:  # View Stats
            show_stats()
        elif choice == 2:  # Change Name
            clear_screen()
            name_pick()
            save_game(USER_WALLET, USER_NAME)
        elif choice == 3:  # Save Game
            clear_screen()
            save_game(USER_WALLET, USER_NAME)
            print(f"{Colours.GREEN}Game saved successfully!{Colours.RESET}")
            input("Press Enter to continue...")
        elif choice == 4 or choice == -1:  # Quit
            clear_screen()
            print(f"{Colours.RED}Thanks for playing! Goodbye!{Colours.RESET}")
            exit()
#----Main Menu----#

#----Stats----#
def show_stats():
    """Display player statistics"""
    clear_screen()
    LINE()
    print(f"{Colours.BOLD}{Colours.CYAN}📊 PLAYER STATISTICS 📊{Colours.RESET}")
    LINE()
    print(f"{Colours.GREEN}💰 Money: ${USER_WALLET}{Colours.RESET}")
    print(f"{Colours.YELLOW}🏷️  Name: {USER_NAME}{Colours.RESET}")
    print(f"{Colours.BLUE}🎮 Games Played: Coming Soon{Colours.RESET}")
    print(f"{Colours.MAGENTA}🏆 Wins: Coming Soon{Colours.RESET}")
    LINE()
    print(f"{Colours.BOLD}Press any key to return to menu...{Colours.RESET}")
    key_press()
#----Stats----#

#----Name Function----#
def name_pick():
    '''Lets user pick a name'''
    global USER_NAME
    LINE()
    print(f"{Colours.YELLOW}✏️ What would you like your name to be? ✏️{Colours.RESET}")
    if USER_NAME is None:
        print(f"{Colours.BOLD}(You can change this later)")
    USER_NAME = input(f"{Colours.BOLD}> {Colours.RESET}")
    clear_screen()
    LINE()
    print(f"{Colours.BOLD}{Colours.RED}YOU HAVE SELECTED: {Colours.RESET}{USER_NAME}")
    LINE()
    CONFIRMATION()
#----Name Function----#

#----Confirmation----#
def CONFIRMATION():
    '''confirming previous statement'''
    clear_screen()
    LINE()
    print(f"{Colours.BOLD}Selected name: {Colours.YELLOW}{USER_NAME}{Colours.RESET}")
    choice = arrow_menu(["✅ Confirm", "❌ Redo"])
    if choice == 0:
        clear_screen()
        main_menu()
    elif choice == 1:
        name_pick()
#----Confirmation----#

# Test the functions
if __name__ == "__main__":
    clear_screen()
    start_game()
    if USER_NAME is None:
        name_pick()
        save_game(USER_WALLET, USER_NAME)
    
    # Start the main menu system
    main_menu()