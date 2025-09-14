#----Import Python Packages----#
import json
import base64
import os
import codecs
import random
import time

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
    BLACK = '\033[38;5;0m'
    RED = '\033[38;5;1m'
    GREEN = '\033[38;5;2m'
    YELLOW = '\033[38;5;3m'
    BLUE = '\033[38;5;4m'
    MAGENTA = '\033[38;5;5m'
    CYAN = '\033[38;5;6m'
    WHITE = '\033[38;5;7m'
    GOLD = '\033[38;5;220m'
    
    BG_RED = '\033[48;5;196m'
    BG_GREEN = '\033[48;5;46m'
    BG_YELLOW = '\033[48;5;226m'
    BG_BLUE = '\033[48;5;21m'
    BG_WHITE = '\033[48;5;15m'
    BG_BLACK = '\033[48;5;0m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    
    RESET = '\033[0m'
#----Colours----#

#----Save File Money----#

def to_binary_str(s):
    '''binary encoder'''
    return ''.join(format(ord(c), '08b') for c in s)

def from_binary_str(b):
    '''binary decoder'''
    # Validate binary string
    if len(b) % 8 != 0:
        raise ValueError("Binary string length must be divisible by 8")
    if not all(c in '01' for c in b):
        raise ValueError("Binary string must only contain 0s and 1s")
    
    chars = [chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8)]
    return ''.join(chars)

def encode_save(json_str):
    '''encodes using method under'''
    # Base64 encode
    b64 = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    # Reverse
    rev = b64[::-1]
    # ROT13 encode
    rot = codecs.encode(rev, 'rot_13')
    # Binary encode
    binary = to_binary_str(rot)
    return binary.encode('utf-8')  # Write as bytes

def decode_save(encoded_bytes):
    '''decodes using method under'''
    # grabs code
    binary_str = encoded_bytes.decode('utf-8')
    # Binary decode
    rot = from_binary_str(binary_str)
    # ROT13 decode
    rev = codecs.decode(rot, 'rot_13')
    # Reverse
    b64 = rev[::-1]
    # Base64 decode
    json_str = base64.b64decode(b64).decode('utf-8')
    return json_str

def load_game(filename="savefile_ridetheduck.json"): # access save file -JSON
    '''loading save file - returns both money and name'''
    try:
        with open(filename, "rb") as f: # reads file and places value "f"
            encoded_bytes = f.read() # convert value string to bytes "f"
            json_str = decode_save(encoded_bytes) # grabs decoded data
            data = json.loads(json_str) # changes value to "data"
            print("Save file loaded") # confirm message
            return (data.get("money", 500), # defaul value
                    data.get("name", None),
                    data.get("games played", 0),
                    data.get("x2 Wins", 0),
                    data.get("x3 Wins", 0),
                    data.get("x4 Wins", 0),
                    data.get("x20 Wins", 0))
    except FileNotFoundError: # New player detection
        print("New player - no save file found") # confirmation message
        return 500, None, 0, 0, 0, 0, 0 # starting items
    except (ValueError, json.JSONDecodeError) as e: # corruption detection
        print(f"Corrupted save file - using defaults. Error: {e}") # confirmation message
        return 500, None, 0, 0, 0, 0, 0 # reset values

def save_game(money=None, name=None, game_played=None, win2=None, win3=None, win4=None, win20=None, filename="savefile_ridetheduck.json"):
    '''saving game data'''
    if money is None:
        money = USER_WALLET
    if name is None:
        name = USER_NAME
    if game_played is None:
        game_played = GAMES_PLAYED
    if win2 is None:
        win2 = WIN_X2
    if win3 is None:
        win3 = WIN_X3
    if win4 is None:
        win4 = WIN_X4
    if win20 is None:
        win20 = WIN_X20
    data = {
        "money": money, 
        "name": name, 
        "games played": game_played, 
        "x2 Wins": win2, 
        "x3 Wins": win3, 
        "x4 Wins": win4, 
        "x20 Wins": win20
    }
    json_str = json.dumps(data) # turns into "data" value
    encoded_bytes = encode_save(json_str) # grabs the encoded data
    with open(filename, "wb") as f: # opens file to prep writing
        f.write(encoded_bytes) # writes
    print(f"Game saved: {name} with ${money}") # confirmation message
#----Save File Money----#

#----Variables----#
USER_WALLET, USER_NAME, GAMES_PLAYED, WIN_X2, WIN_X3, WIN_X4, WIN_X20 = load_game()  # Load both money and name from save file
CARD_SUITS = ("♠", "♦", "♥", "♣") # creates suits for card deck creation
USER_NAME_KNOWLEDGE = False
WINS_TOTAL = WIN_X2 + WIN_X3 + WIN_X4 + WIN_X20
Confirm_Redo = ["✅ Confirm", "🔄 Redo"]
Confirm_Redo_Cancel = ["✅ Confirm", "🔄 Redo", "❌ Cancel"]
MULTIPLIER = {"x2" : 1, "x3" : 0, "x4" : 0, "x20" : 0}
user_bet = None
bet_confirm = False
Win = None
game_round = 1
continue_game = False
PlayOption = 0
gc_rank = {}
gc_suit = {}
card_value_1 = {}
card_value_2 = {}
card_value_3 = {}
card_value_4 = {}
game_card = {}
card_output = ""

RedBlackPick = [
    "🟥 Red",
    "⬛ Black"
    ]
PlayOptions = [
    "🔄 Play Again",
    "🎰 Menu"
    ]
Win_Continue = [
    "✅ Continue",
    "💵 Cash Out"
    ]
Lose_Continue = [
    "🔄 Play Again",
    "🎰 Menu"
    ]
OverUnderPick = [
    "⬆️ Over",
    "⬇️ Under"
    ] 
InOutPick = [
    "➡️ ⬅️ Inside",
    "⬅️ ➡️ Outside"
    ]
SuitPick = [
    "♠️ Spades",
    "♦️ Diamonds",
    "♥️ Hearts",
    "♣️ Clubs"
    ]

top = ""
mid_top = ""
top_mid = ""
bottom_mid = ""
mid_bottom = ""
bottom = ""
#----Variables----#

#----Function Variables----#
def LINE():
    ''''creates line spacing'''
    print(f"{Colours.BOLD}{Colours.MAGENTA}======----------================----------======{Colours.RESET}")

def clear_screen():
    ''''clear screen function'''
    os.system('cls' if os.name == 'nt' else 'clear') # function to clear screen

def is_float(variable):
    '''check if value is a float'''
    try:
        float(variable)
        return True
    except ValueError:
        return False

def money_valid(money_value):
    """check if value has 2 decimal or less"""
    if '.' in money_value:
        decimal_part = money_value.split('.')[1]
        return len(decimal_part) <= 2
    else:
        return True

def print_tw(sentence, type_delay=0.01):
    '''creates a type writer effect'''
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()
#----Function Variables----#

#----Card Deck----#
CardDeck = {}

for suit in CARD_SUITS:
    for value_card in range(2, 11):
        CardDeck[f"{value_card}{suit}"] = value_card

for suit in CARD_SUITS:
    CardDeck[f"D{suit}"] = 11
    CardDeck[f"Q{suit}"] = 12
    CardDeck[f"K{suit}"] = 13
    CardDeck[f"A{suit}"] = 14
#----Card Deck----#

#----Single Key Track----#
# Unix key pressing
def key_press(option):
    '''single key tracking'''
    try:
        fd = sys.stdin.fileno() # sets variable for key input
        old_settings = termios.tcgetattr(fd) # saves the old state of the terminal
        if option is 0:
            print(f"{Colours.RED}Press any key to continue{Colours.RESET}")
        elif option is 1:
            print(f"{Colours.RED}Press any key to return to menu{Colours.RESET}")
        try:
            tty.setraw(sys.stdin.fileno()) # sets terminal in "raw mode" for tracking
            key = sys.stdin.read(1) # reads only 1 keyboard input
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # restores to old state
        return key
    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()

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
    try:
        fd = sys.stdin.fileno() # find  keyboard format
        old_settings = termios.tcgetattr(fd) # saves old terminal
        try:
            tty.setraw(sys.stdin.fileno()) # tunrs on "raw mode"
            key = sys.stdin.read(1) # reads first input
            
            # Check for CTRL-C and CTRL-D in raw mode
            if ord(key) == 3:  # CTRL-C
                print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
                exit()
            elif ord(key) == 4:  # CTRL-D
                print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
                exit()
            
            # Check for escape sequence (arrow keys)
            if ord(key) == 27:  # ESC
                key += sys.stdin.read(2)  # Read the next 2 characters (for arrows)
                
            return key
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # restores old settings
    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
#----Arrow Key Track----#

#----Arrow Key Menu System----#
def arrow_menu(title, text, options):
    """generic arrow key menu system"""
    try:
        selected = 0
        while True:
            clear_screen()  # Clear screen for smooth animation
            LINE()
            is_win_or_lose = "WinOrLose" in options
            if is_win_or_lose:
                if Win is True:
                    options = Win_Continue
                    if game_round == 1:
                        MULTIPLIER["x2"] = 2
                    elif game_round == 2:
                        MULTIPLIER["x3"] = 2
                    elif game_round == 3:
                        MULTIPLIER["x4"] = 2
                    elif game_round == 4:
                        MULTIPLIER["x20"] = 2
                elif Win is False:
                    options = Lose_Continue
                    if game_round == 1:
                        MULTIPLIER["x2"] = 3
                    elif game_round == 2:
                        MULTIPLIER["x3"] = 3
                    elif game_round == 3:
                        MULTIPLIER["x4"] = 3
                    elif game_round == 4:
                        MULTIPLIER["x20"] = 3
            
            if is_win_or_lose:
                print_tw("And the card is.......", 0.05)
                time.sleep(1)
                clear_screen()
                clear_screen()
                LINE()

            if title == "menu":
                print(f"{Colours.BOLD}{Colours.BLUE}🎰 RIDE THE DUCK - MENU 🎰{Colours.RESET}")
            elif title == "name":
                print(f"{Colours.BOLD}{Colours.BLUE}🏷️  RIDE THE DUCK - NAME 🏷️{Colours.RESET}")
            elif title == "game":
                print(f"{Colours.BOLD}{Colours.BLUE}🏷️  RIDE THE DUCK - GAME 🏷️{Colours.RESET}")
            elif title == "game-main":
                print(f"{Colours.BOLD}{Colours.BLUE}🏷️  RIDE THE DUCK - GAME 🏷️{Colours.RESET}\n")

                x2_print = "ERROR"
                x3_print = "ERROR"
                x4_print = "ERROR"
                x20_print = "ERROR"

                if MULTIPLIER["x2"] == 0:
                    x2_print = "Error"
                elif MULTIPLIER["x2"] == 1:
                    x2_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_YELLOW} x2 {Colours.RESET}]"
                elif MULTIPLIER["x2"] == 2:
                    x2_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_GREEN} x2 {Colours.RESET}]"
                elif MULTIPLIER["x2"] == 3:
                    x2_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_RED} x2 {Colours.RESET}]"

                if MULTIPLIER["x3"] == 0:
                    x3_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_WHITE} x3 {Colours.RESET}]"
                elif MULTIPLIER["x3"] == 1:
                    x3_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_YELLOW} x3 {Colours.RESET}]"
                elif MULTIPLIER["x3"] == 2:
                    x3_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_GREEN} x3 {Colours.RESET}]"
                elif MULTIPLIER["x3"] == 3:
                    x3_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_RED} x3 {Colours.RESET}]"

                if MULTIPLIER["x4"] == 0:
                    x4_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_WHITE} x4 {Colours.RESET}]"
                elif MULTIPLIER["x4"] == 1:
                    x4_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_YELLOW} x4 {Colours.RESET}]"
                elif MULTIPLIER["x4"] == 2:
                    x4_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_GREEN} x4 {Colours.RESET}]"
                elif MULTIPLIER["x4"] == 3:
                    x4_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_RED} x4 {Colours.RESET}]"

                if MULTIPLIER["x20"] == 0:
                    x20_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_WHITE} x20 {Colours.RESET}]"
                elif MULTIPLIER["x20"] == 1:
                    x20_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_YELLOW} x20 {Colours.RESET}]"
                elif MULTIPLIER["x20"] == 2:
                    x20_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_GREEN} x20 {Colours.RESET}]"
                elif MULTIPLIER["x20"] == 3:
                    x20_print = f"[{Colours.BLACK}{Colours.BOLD}{Colours.BG_RED} x20 {Colours.RESET}]"
                
                print(x2_print, x3_print, x4_print, x20_print)
            LINE()

            text_outcome = None
            if is_win_or_lose:
                if Win is True:
                    text_outcome = f"\n{Colours.GREEN}🎉 Congratulations, you picked correct 🎉\n"
                elif Win is False:
                    text_outcome = f"\n{Colours.RED}❌ Hard luck, you picked wrong ❌\n"
                text = text + text_outcome

            if text is not None:
                print(text)
                
            # Display menu options
            for i, option in enumerate(options):
                if i == selected:
                    print(f"{Colours.BOLD}{Colours.YELLOW}► {option}{Colours.RESET}")
                else:
                    print(f"{Colours.WHITE}  {option}{Colours.RESET}")
            LINE()
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
    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
#----Arrow Key Menu System----#

#----Start Game----#
def start_game():
    '''start of game info'''
    try:
        LINE()
        print(f"{Colours.BOLD}{Colours.BLUE}🎰 RIDE THE DUCK 🎰{Colours.RESET}\n"
            f"{Colours.GREEN}💰 Your Money: ${USER_WALLET}{Colours.RESET}\n"
            f"{Colours.CYAN}🎉 Welcome to Ride the Duck, a gambling game 🎉{Colours.RESET}")
        if USER_NAME is None:
            print(f"{Colours.YELLOW}🏷️  Your  Name:{Colours.RESET}{Colours.RED} -UNKNOWN-{Colours.RESET}")
        else:
            print(f"{Colours.YELLOW}🏷️  Your  Name:{Colours.RESET} {USER_NAME}")
        LINE()
        key_press(1)
        clear_screen()
    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    
#----Start Game----#

#----Betting Check Function----#
def bet_check():
    '''betting check'''
    clear_screen()
    try:
        global user_bet
        global USER_WALLET
        global bet_confirm
        bet_error = 0
        user_bet = None
        bet_confirm = False
        while True:
            LINE()
            print(f"{Colours.BOLD}{Colours.BLUE}🎰 RIDE THE DUCK - MAIN GAME - BET 🎰{Colours.RESET}")
            LINE()

            if bet_error == 1:
                print(f"{Colours.RED}⚠️ Invalid bet: {user_bet} - Please use a number ⚠️{Colours.RESET}")
            elif bet_error == 2:
                print(f"{Colours.RED}⚠️ Invalid bet: {user_bet} - Please a number equal or bigger than 0.01 ⚠️{Colours.RESET}")
            elif bet_error == 3:
                print(f"{Colours.RED}⚠️ Invalid bet: {user_bet} - You are betting more money than you have in your wallet ⚠️{Colours.RESET}")

            print(f"{Colours.GREEN}💰 Your Money: ${USER_WALLET}{Colours.RESET}\n"
                  f"{Colours.CYAN}💵  How much do you want to bet? (Min $0.01) 💵{Colours.RESET}")
            bet_error = 0
            user_bet = input(f"{Colours.BOLD}❯ {Colours.RESET}").strip().lower()
            if is_float(user_bet):
                if money_valid(user_bet):
                    if float(user_bet) <= USER_WALLET:
                        clear_screen()
                        choices = arrow_menu("menu",
                            f"{Colours.GREEN}💵 You are betting: {Colours.WHITE}${user_bet}{Colours.RESET}\n{Colours.CYAN}✅ Please confirm bet amount ✅{Colours.RESET}\n",
                            Confirm_Redo_Cancel)
                        if choices == 0:
                            clear_screen()
                            bet_confirm = True
                            USER_WALLET -= float(user_bet)
                            break
                        elif choices == 1:
                            clear_screen()
                        elif choices == 2:
                            clear_screen()
                            break
                    else:
                        bet_error = 3
                        clear_screen()
                else:
                    bet_error = 2
                    clear_screen()
            else:
                bet_error = 1
                clear_screen()
    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()

#----Betting check Function----#

#----Red Black/Round 1----#
def RedBlack_game():
    '''Red black / round one'''
    try:
        global game_round
        global bet_confirm
        global Win
        global USER_WALLET
        global user_bet
        global continue_game
        global PlayOption
        global game_card_deck
        global top, mid_top, top_mid, bottom_mid, mid_bottom, bottom
        global gc_rank, gc_suit, card_value_1
        global card_output

        game_round = 1
        Win = None

        choices = arrow_menu("game-main", (f"{Colours.CYAN}Pick a card colour{Colours.RESET}\n"), RedBlackPick)
        if choices == 0:
            user_colour = 1
        elif choices == 1:
            user_colour = 2
        else:
            user_colour = 3
        clear_screen()

        game_card_deck = CardDeck

        card_key, card_value_1 = random.choice(list(game_card_deck.items()))
        game_card[card_key] = card_value_1
        game_card_deck.pop(card_key)

        gc_rank = card_key[:-1]
        gc_suit = card_key[-1]

        card_colour = Colours.RED if gc_suit in ("♦", "♥") else Colours.BLACK if gc_suit in ("♠", "♣") else {Colours.BLACK}


        rb_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╭──────╮{Colours.RESET}  "
        rb_mid_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│ {gc_rank}{gc_suit}   │{Colours.RESET}  "
        rb_top_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
        rb_bottom_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
        rb_mid_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│   {gc_suit}{gc_rank} │{Colours.RESET}  "
        rb_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╰──────╯{Colours.RESET}  "
            
        if card_value_1 == 10:
            rb_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╭──────╮{Colours.RESET}  "
            rb_mid_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│ {gc_rank}{gc_suit}  │{Colours.RESET}  "
            rb_top_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
            rb_bottom_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
            rb_mid_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│  {gc_suit}{gc_rank} │{Colours.RESET}  "
            rb_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╰──────╯{Colours.RESET}  "

        top = rb_top
        mid_top = rb_mid_top
        top_mid = rb_top_mid
        bottom_mid = rb_bottom_mid
        mid_bottom = rb_mid_bottom
        bottom = rb_bottom

        card_output = (top, mid_top, top_mid, bottom_mid, mid_bottom, bottom, "")

        if user_colour == 1 and gc_suit in ("♦", "♥") or user_colour == 2 and gc_suit in ("♠", "♣"):
            Win = True
        else:
            Win = False

        choices = arrow_menu("game-main", "\n".join(card_output), ["WinOrLose"])

        if Win is True:
            if choices == 0:
                continue_game = True
            elif choices == 1:
                user_bet = float(user_bet) * 2
                USER_WALLET += float(user_bet)
                save_game()
                clear_screen()

                choices = arrow_menu("game-main", f"{Colours.GREEN}💰 YOU WON ${user_bet} 💰{Colours.RESET}\n", PlayOptions)
                if choices == 0:
                    PlayOption = 1
                elif choices == 1:
                    PlayOption = 2

        elif Win is False:
            if choices == 0:
                PlayOption = 1
            elif choices == 1:
                PlayOption = 2
        
    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
#----Red Black/Round 1----#

#----Over Under/Round 2----#
def OverUnder_game():
    '''Over Under / round one'''
    try:
        global game_round
        global bet_confirm
        global Win
        global USER_WALLET
        global user_bet
        global continue_game
        global PlayOption
        global game_card_deck
        global top, mid_top, top_mid, bottom_mid, mid_bottom, bottom
        global gc_rank, gc_suit, card_value_2
        global card_output

        game_round = 2
        MULTIPLIER["x3"] = 1
        Win = None
        choices = arrow_menu("game-main", "\n".join(card_output) + (f"\n{Colours.CYAN}Pick over or under{Colours.RESET}\n"), OverUnderPick)
        if choices == 0:
            ou_pick = "over"
        elif choices == 1:
            ou_pick = "under"
        else:
            ou_pick = "error"
        clear_screen()

        game_card_deck = CardDeck

        card_key, card_value_2 = random.choice(list(game_card_deck.items()))
        game_card[card_key] = card_value_2
        game_card_deck.pop(card_key)

        gc_rank = card_key[:-1]
        gc_suit = card_key[-1]

        card_colour = Colours.RED if gc_suit in ("♦", "♥") else Colours.BLACK if gc_suit in ("♠", "♣") else {Colours.BLACK}


        ou_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╭──────╮{Colours.RESET}  "
        ou_mid_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│ {gc_rank}{gc_suit}   │{Colours.RESET}  "
        ou_top_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
        ou_bottom_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
        ou_mid_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│   {gc_suit}{gc_rank} │{Colours.RESET}  "
        ou_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╰──────╯{Colours.RESET}  "
            
        if card_value_2 == 10:
            ou_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╭──────╮{Colours.RESET}  "
            ou_mid_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│ {gc_rank}{gc_suit}  │{Colours.RESET}  "
            ou_top_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
            ou_bottom_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
            ou_mid_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│  {gc_suit}{gc_rank} │{Colours.RESET}  "
            ou_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╰──────╯{Colours.RESET}  "

        top += ou_top #+ io_top + s_top
        mid_top += ou_mid_top #+ io_mid_top + s_mid_top
        top_mid += ou_top_mid #+ io_top_mid + s_top_mid
        bottom_mid += ou_bottom_mid #+ io_bottom_mid + s_bottom_mid
        mid_bottom += ou_mid_bottom #+ io_mid_bottom + s_mid_bottom
        bottom += ou_bottom #+ io_bottom + s_bottom

        card_output = (top, mid_top, top_mid, bottom_mid, mid_bottom, bottom, "")

        if int(card_value_2) > int(card_value_1):
            ou_output = "over"
        elif int(card_value_2) < int(card_value_1):
            ou_output = "under"
        elif int(card_value_1) == int(card_value_2):
            ou_output = "equal"
        else:
            ou_output = "error"

        if ou_output == ou_pick:
            Win = True
        else:
            Win = False
        choices = arrow_menu("game-main", "\n".join(card_output), ["WinOrLose"])

        if Win is True:
            if choices == 0:
                continue_game = True
            elif choices == 1:
                user_bet = float(user_bet) * 3
                USER_WALLET += float(user_bet)
                save_game()
                clear_screen()

                choices = arrow_menu("game-main", f"{Colours.GREEN}💰 YOU WON ${user_bet} 💰{Colours.RESET}\n", PlayOptions)
                if choices == 0:
                    PlayOption = 1
                elif choices == 1:
                    PlayOption = 2

        elif Win is False:
            if choices == 0:
                PlayOption = 1
            elif choices == 1:
                PlayOption = 2

    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
#----Over Under/Round 2----#

#----In Out/Round 3----#
def InOut_game():
    '''Over Under / round one'''
    try:
        global game_round
        global bet_confirm
        global Win
        global USER_WALLET
        global user_bet
        global continue_game
        global PlayOption
        global game_card_deck
        global top, mid_top, top_mid, bottom_mid, mid_bottom, bottom
        global gc_rank, gc_suit, card_value_3
        global card_output

        io_output = ""
        game_round = 3
        MULTIPLIER["x4"] = 1
        Win = None
        choices = arrow_menu("game-main", "\n".join(card_output) + (f"\n{Colours.CYAN}Pick inside or outsite{Colours.RESET}\n"), InOutPick)
        if choices == 0:
            io_pick = "inside"
        elif choices == 1:
            io_pick = "outside"
        else:
            io_pick = "error"
        clear_screen()

        game_card_deck = CardDeck

        card_key, card_value_3 = random.choice(list(game_card_deck.items()))
        game_card[card_key] = card_value_3
        game_card_deck.pop(card_key)

        gc_rank = card_key[:-1]
        gc_suit = card_key[-1]

        card_colour = Colours.RED if gc_suit in ("♦", "♥") else Colours.BLACK if gc_suit in ("♠", "♣") else {Colours.BLACK}


        io_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╭──────╮{Colours.RESET}  "
        io_mid_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│ {gc_rank}{gc_suit}   │{Colours.RESET}  "
        io_top_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
        io_bottom_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
        io_mid_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│   {gc_suit}{gc_rank} │{Colours.RESET}  "
        io_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╰──────╯{Colours.RESET}  "
            
        if card_value_2 == 10:
            io_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╭──────╮{Colours.RESET}  "
            io_mid_top = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│ {gc_rank}{gc_suit}  │{Colours.RESET}  "
            io_top_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
            io_bottom_mid = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│      │{Colours.RESET}  "
            io_mid_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}│  {gc_suit}{gc_rank} │{Colours.RESET}  "
            io_bottom = f"{Colours.BG_WHITE}{Colours.BOLD}{card_colour}╰──────╯{Colours.RESET}  "

        top += io_top #+ s_top
        mid_top += io_mid_top #+ s_mid_top
        top_mid += io_top_mid #+ s_top_mid
        bottom_mid += io_bottom_mid #+ s_bottom_mid
        mid_bottom += io_mid_bottom #+ s_mid_bottom
        bottom += io_bottom #+ s_bottom

        card_output = (top, mid_top, top_mid, bottom_mid, mid_bottom, bottom, "")

        if int(card_value_1) > int(card_value_2):
            if int(card_value_3) < int(card_value_1) and int(card_value_3) > int(card_value_2):
                io_output = "inside"
            elif int(card_value_3) > int(card_value_1) or int(card_value_3) < int(card_value_2):
                io_output = "outside"
            elif int(card_value_3) == int(card_value_1) or int(card_value_3) == int(card_value_2):
                io_output = "equal"
            else:
                io_output = "error"

        if int(card_value_1) < int(card_value_2):
            if int(card_value_3) < int(card_value_2) and int(card_value_3) > int(card_value_1):
                io_output = "inside"
            elif int(card_value_3) < int(card_value_1) or int(card_value_3) > int(card_value_2):
                io_output = "outside"
            elif int(card_value_3) == int(card_value_1) or int(card_value_3) == int(card_value_2):
                io_output = "equal"
            else:
                io_output = "error"

        if io_output == io_pick:
            Win = True
        else:
            Win = False
        choices = arrow_menu("game-main", "\n".join(card_output), ["WinOrLose"])

        if Win is True:
            if choices == 0:
                continue_game = True
            elif choices == 1:
                user_bet = float(user_bet) * 4
                USER_WALLET += float(user_bet)
                save_game()
                clear_screen()

                choices = arrow_menu("game-main", f"{Colours.GREEN}💰 YOU WON ${user_bet} 💰{Colours.RESET}\n", PlayOptions)
                if choices == 0:
                    PlayOption = 1
                elif choices == 1:
                    PlayOption = 2

        elif Win is False:
            if choices == 0:
                PlayOption = 1
            elif choices == 1:
                PlayOption = 2

    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
#----In Out/Round 3----#

#----Main Menu----#
def main_menu():
    """Main game menu with arrow navigation"""
    try:
        options = [
            "🎮 Play Ride the Duck",
            "📊 View Statistics",
            "❓ Help", 
            "✏️  Change Name",
            "💾 Save Game",
            "🚪 Quit Game"
        ] 
        while True:
            clear_screen()  # Clear screen for smooth menu display
            
            choice = arrow_menu("menu", None, options)
            
            if choice == 0:  # Play Game
                clear_screen()
                main_game()
            elif choice == 1:  # View Stats
                show_stats()
            elif choice == 2:  # tips
                clear_screen()
                pass ### NOT DONEEEEEEEEE
                save_game(USER_WALLET, USER_NAME, GAMES_PLAYED, WIN_X2, WIN_X3, WIN_X4, WIN_X20)
            elif choice == 3:  # CHange name
                clear_screen()
                name_pick()
            elif choice == 4:
                save_game(USER_WALLET, USER_NAME, GAMES_PLAYED, WIN_X2, WIN_X3, WIN_X4, WIN_X20)
            elif choice == 5 or choice == -1:  # Quit
                clear_screen()
                print(f"{Colours.RED}Thanks for playing! Goodbye!{Colours.RESET}")
                exit()
    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
#----Main Menu----#

#----Stats----#
def show_stats():
    """Display player statistics"""
    global WINS_TOTAL
    WINS_TOTAL = WIN_X2 + WIN_X3 + WIN_X4 + WIN_X20
    try:
        clear_screen()
        LINE()
        print(f"{Colours.BOLD}{Colours.CYAN}📊 PLAYER STATISTICS 📊{Colours.RESET}")
        LINE()
        print(f"{Colours.GREEN}💰 Money: ${USER_WALLET}{Colours.RESET}\n"
            f"{Colours.YELLOW}🏷️  Name: {USER_NAME}{Colours.RESET}\n"
            f"{Colours.CYAN}🎮 Games Played: {GAMES_PLAYED}{Colours.RESET}\n"
            f"{Colours.GOLD}🏆 Wins Toal: {WINS_TOTAL}{Colours.RESET}\n"
            f"{Colours.GOLD}🏆 x2 Wins: {WIN_X2}{Colours.RESET}\n"
            f"{Colours.GOLD}🏆 x3 Wins: {WIN_X3}{Colours.RESET}\n"
            f"{Colours.GOLD}🏆 x4 Wins: {WIN_X4}{Colours.RESET}\n"
            f"{Colours.GOLD}🏆 x20 Wins: {WIN_X20}{Colours.RESET}"

        )
        LINE()
        key_press(1)
    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
#----Stats----#

#----Name Function----#
def name_pick():
    '''Lets user pick a name'''
    try:
        global USER_NAME
        global USER_NAME_KNOWLEDGE
        clear_screen()
        LINE()
        print(f"{Colours.BOLD}{Colours.BLUE}🏷️  RIDE THE DUCK - NAME 🏷️{Colours.RESET}")
        LINE()
        print(f"{Colours.YELLOW}✏️  What would you like your name to be? ✏️{Colours.RESET}")
        if USER_NAME_KNOWLEDGE is False:
            print(f"{Colours.RED}(You can change this later){Colours.RESET}")
        elif USER_NAME_KNOWLEDGE is True:
            pass
        USER_NAME = input(f"{Colours.BOLD}❯ {Colours.RESET}")
        clear_screen()
        choice = arrow_menu("name", (f"{Colours.BOLD}{Colours.YELLOW}YOU HAVE SELECTED: {Colours.RESET}{USER_NAME}\n"), Confirm_Redo)
        if choice == 0:
            USER_NAME_KNOWLEDGE = True
            clear_screen()
            pass
        elif choice == 1:
            name_pick()
    except KeyboardInterrupt:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
    except EOFError:
        print(f"{Colours.RED}Thanks for playing Ride The Duck{Colours.RESET}")
        exit()
#----Name Function----#

#----Main Game----#

def main_game():
    '''ride the duck main game'''

    global continue_game
    global MULTIPLIER
    global bet_confirm
    while True:
        MULTIPLIER = {"x2" : 1, "x3" : 0, "x4" : 0, "x20" : 0}
        bet_check()
        if bet_confirm is True:
            bet_confirm = False
            RedBlack_game()
            if continue_game is True:
                continue_game = False
                OverUnder_game()
                if continue_game is True:
                    continue_game = False
                    InOut_game()
                    if continue_game is True:
                        continue_game = False
                        # continue game
                    elif PlayOption is not None:
                        save_game()
                        if PlayOption == 1:
                            continue
                        elif PlayOption == 2:
                            break
                elif PlayOption is not None:
                    save_game()
                    if PlayOption == 1:
                        continue
                    elif PlayOption == 2:
                        break
            elif PlayOption is not None:
                save_game()
                if PlayOption == 1:
                    continue
                elif PlayOption == 2:
                    break
        else:
            break
        

#----Main Game----#

if __name__ == "__main__":
    clear_screen()
    start_game()
    if USER_NAME is None:
        name_pick()
    save_game(USER_WALLET, USER_NAME, GAMES_PLAYED, WIN_X2, WIN_X3, WIN_X4, WIN_X20)
    
    main_menu()