# Daketi Card Game (Stealing Bundles)

## (Requirements)Introduction

Daketi (Stealing Bundles) is a card game designed for 2 to 4 players. The goal is to gather the largest bundle of cards by matching cards from your hand with those in the center of the table or stealing bundles from your opponents. This game helps practice number recognition and matching skills.

## Features

- Supports for now only 4 players.
- Interactive gameplay with a graphical user interface.
- Handles card distribution, matching, and stealing according to game rules.
- Displays current player's turn and updates card positions Automatically.
- Provides a scoreboard at the end of the game to declare the winner.
- Allows players to play multiple rounds with a "Play Again" feature.

## Setup and Installation

1. **Clone the repository** or download the ZIP file and extract it.
2. **Ensure you have Python installed** on your system.
3. **Install required libraries**:
    ```sh
    pip install pillow
    ```
4. **Run the game**:
    ```sh
    python main.py
    ```

## How to Play

1. **Start the game**: Click on the "Start Game" button to begin.
2. **Initial card distribution**: The dealer deals 4 cards to each player and 4 cards face up in the center.
3. **Player turns**: The player1 starts the game. Each player plays one card from their hand:
    - If the card matches the top card of an opponent's bundle, the player steals the opponent's bundle.
    - If the card matches one in the center, the player takes both cards and adds them to their bundle.
    - If the card does not match any in the center or opponent's bundles, it will be added to the center(Screen) Cards.
4. **Card Distribution Condition**: When there is no card in Any of the Players Cards which matches with screen cards or the upper cards other player cards piles, the dealer deals 4 more cards to each player.
5. **Dealer Cards Distributions Actually**: There would be total 3 Distibutions. One distribution in the start when user press Start Game Button and the other 2 when the Upper line condition fulfills and after all done, the dealer will have no more card to distribute, So then now when this condition mets then the game ends with a scoreboard on screen. 
6. **End of game**: The game ends when all cards are dealt and played. The player with the largest bundle wins.
7. **Scoreboard**: The scoreboard displays the scores of each player and the winner. There is a Button of "Play Again" on the screen so the Players can choose to play again or Exit the game by Exit Button.

## Game Rules

- **Card Matching**: Match your card with the center cards or the top card of an opponent's bundle to collect them.
- **Stealing Bundles**: If your card matches the top card of an opponent's bundle, you steal their entire bundle.
- **Card Replenishment**: When no player have matching card, then 4 new cards are dealt to each player until the deck is empty.
- **Winning**: The player with the largest bundle at the end of the game wins.

## Game File and Resources

- `main.py`: Main game script implementing the Daketi card game.
- `bg.png`: Background image for the game interface.
- `card.png`: Image for displaying cards.
- `README.md`: Project documentation.

## Screenshots
![Game Start](https://github.com/HuzaifaSaran0/StealingBundlesCardsGame/assets/138969799/7018d14d-e096-4a01-9034-10430bc7c062)
![Player Turn](https://github.com/HuzaifaSaran0/StealingBundlesCardsGame/assets/138969799/cd648716-2f25-4790-be36-41cca6cf8a09)
![Scoreboard](https://github.com/HuzaifaSaran0/StealingBundlesCardsGame/assets/138969799/ce2ac0f9-74d2-4b35-983f-0508ed4925eb)

## Requirements for running this code on your machine

- Python 3.11
- `tkinter` library (comes pre-installed with Python)
- `pillow` library for image handling

## Contribution

If you have suggestions or find bugs, feel free to open an issue or create a pull request.

