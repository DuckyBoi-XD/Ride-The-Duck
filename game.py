#----Import Python Packages----#
import json
import base64
import os
import sys
import tty
import termios
#----Import Python Packages----#

#----Save File Money----#
def load_game(filename="savefile.json"): # access save file -JSON
    '''loading save file - returns both money and name'''
    try:
        with open(filename, "rb") as f: # reads file and places value "f"
            encoded_bytes = f.read() # convert value string to bytes "f"
            json_str = base64.b64decode(encoded_bytes).decode('utf-8') # decodes
            data = json.loads(json_str) # changes value to "data"
            print(f"Save file loaded") # confirm message
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

def LINE():
    print(f"{Colors.BOLD}{Colors.MAGENTA}======----------================----------======")

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # function to clear screen
#----Variables----#

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

def start_game():
    LINE()
    print(f"{Colors.BOLD}{Colors.CYAN}🎰 RIDE THE DUCK 🎰{Colors.RESET}\n"
        f"{Colors.GREEN}💰 Your Money: ${USER_WALLET}{Colors.RESET}\n"
        f"{Colors.YELLOW}🏷️  Your  Name: {USER_NAME}{Colors.RESET}"
    )

def main_game():
    '''Ride the Bus game'''
    pass

#----Name Function----#
def name_pick():
    global USER_NAME
    LINE()
    print(f"{Colors.YELLOW}✏️ What would you like your name to be? ✏️{Colors.RESET}\n"
          f"{Colors.BOLD}(You can change this later)"
    )
    USER_NAME = input(f"{Colors.BOLD}> {Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}YOU HAVE SELECTED: {Colors.RESET}{USER_NAME}")
#----Name Function----#

# Test the functions
if __name__ == "__main__":
    start_game()
    if USER_NAME is None:
        name_pick()
        save_game(USER_WALLET, USER_NAME)