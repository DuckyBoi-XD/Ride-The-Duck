# Ride-The-Duck

Ride The Duck is a CLI, binary executable game based on the drinking game "Ride The Bus". Ride The Duck incorporates the first stage of Ride The Bus where you need to guess if the next card is, Red or Black, Over or Under (the first card), Inside or Outside (the first 2 card), Spade, Diamonds, Heart, or Clubs.

## Features

Ride The Duck contains many different freature:

- Save file: When exiting the terminal or the game, your data (money, name, stats) will be saved.
- CLI: The game appears and runs on the Command Line Interface for a tech and hacky vibe.
- ASCII: Part of the game's interface is made using ASCII which give's a cool visual effect.
- ANSI escape codes: The game's text is configured with colour to pop out.
- Gambling: You are given money to gamble with, fun.

## Gameplay

[insert gameplay here]

## How Does Ride The Duck Work?

When you play the main game you would first need to insert how much you would want to bet. After you complete the bet stage there are 4 rounds, each round giving you a better multipler for your money.

1. Red or Black x2

2. Over or Under x3

3. Inside or Outside x4

4. Suit x20

After completing each stage, you are able to cash out and collect you bet with the multipler of the round or continue and try collect a higher multiplier.

The first round is guessing if the next/first card is going to be Red or Black. Completing this will give you 2x multipler on your inital bet.
The second round is guessing if the next card is going to be over or under the first cards. Completing this will give you 3x multipler on your inital bet.
The tird round is guessing if the next card is going to be inbetween the first 2 cards or outside them. Completing this will give you 4x multipler on your inital bet.
Lastly, the forth round is guessing the suit of the next/last card. Completing this will give you 20x multipler on your inital bet.

On the last stage you can only cash out, earning the holy 20x multiplier.

## How to play

### Binary Executable (MacOS arm 64 ONLY)

To download the binary exucutable (TERMINAL CRAFT) you can follow these steps:

1. Go to releases page of Ride The Duck

2. Go to the most recent version and download the file: "RTD-G MacOS arm64 tar.gz". This is the file that has the game on it.

3. Bypass the Apple security by:

    Settings>Privicy & Sercurity and under Sercurity select open anyways on the game file name "game".

    or

    Go to your terminal and insert the file directory in where the file is -
    Example:

    ```sh
    cd /Users/MyUserNAME/downloads 
    ```

    Then use this command to Bypass the security -

    ```sh
    xattr -d com.apple.quarantine game
    ```

4. Double click or open the game executable file and have fun c:

If your not comfortable with letting your guard down and bypassing the security you can message me on Slack (Soon to be changed tho) [@DuckyBoi_XD](https://hackclub.slack.com/team/U08TJ79P0G4) or [Email](braedenjairsytan@icloud.com) and I'll try to respond asap to send you the file that shouldn't require any security bypass

### PyPi (COMMING SOON)
