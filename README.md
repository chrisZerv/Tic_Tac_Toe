# Tic Tac Toe Game with AI

A simple text-based Tic Tac Toe game implemented in Python, where the player competes against an AI opponent. The AI is programmed to make strategic moves, including attempting to win or block the player from winning.

## Features

- **Player vs. AI Mode**: Play against an AI that makes strategic decisions.
- **Command-line Interface**: The game is played directly in your terminal or command prompt.
- **Error Handling**: The game includes input validation to ensure smooth gameplay.
- **Win and Draw Detection**: The game detects and announces when the player or AI has won, or if the game ends in a draw.

## How to Play

1. **Choose Your Side**: The game will prompt you to choose between "X" and "O". If you choose "X", you will play first; otherwise, the AI will go first.
2. **Making Moves**:
   - The game board is represented by numbers 1-9, as shown below:
     ```
     1 | 2 | 3
     4 | 5 | 6
     7 | 8 | 9
     ```
   - On your turn, enter the number corresponding to the position where you want to place your mark.
3. **Game Progression**: 
   - The game alternates between you and the AI until a win or a draw is detected.
   - The game will print the board after each move and announce the result at the end.

## Installation

To run the game locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/tic-tac-toe-ai.git
    ```
   Replace `yourusername` with your GitHub username.

2. **Navigate to the Project Directory**:
    ```bash
    cd tic-tac-toe-ai
    ```

3. **Run the Game**:
    ```bash
    python3 tic_tac_toe.py
    ```

## Example Gameplay
Do you want to play as X or O? X | |
| |
| | Player X, enter your move (1-9): 5 | |
|X|
| | The AI (O) makes a move: O| |
|X|
| |

## Contributing

Contributions are welcome! Feel free to submit a pull request if you have any improvements or new features to add.


