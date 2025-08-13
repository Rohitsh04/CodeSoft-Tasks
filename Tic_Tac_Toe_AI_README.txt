Tic-Tac-Toe AI Game

A PyQt5-based Tic-Tac-Toe game where the player (X) competes against an AI (O) that uses the minimax algorithm.

------------------------------------------------------------
Features
------------------------------------------------------------
- Interactive GUI built using PyQt5
- Player vs AI mode
- AI opponent powered by the minimax algorithm
- Automatic win/draw detection
- Game reset after each match

------------------------------------------------------------
Requirements
------------------------------------------------------------
Install the required dependency:
    pip install PyQt5

------------------------------------------------------------
How to Run
------------------------------------------------------------
1. Save the script as Tic_Tac_toe.py.
2. Run it using:
       python Tic_Tac_toe.py
3. The game window will open.
4. Click on any empty square to make your move (X).
5. The AI will respond with its move (O).
6. The game announces the winner or a draw and resets automatically.

------------------------------------------------------------
How It Works
------------------------------------------------------------
- The board is represented as a list of 9 elements.
- Player always plays as 'X', AI plays as 'O'.
- On the player's turn, they click a button to place an 'X'.
- On the AI's turn, the minimax algorithm evaluates all possible moves and chooses the best one.
- The game checks for win conditions or a draw after each move.

------------------------------------------------------------
Example Gameplay
------------------------------------------------------------
[Player] Clicks center -> X appears
[AI] Chooses a corner -> O appears
... game continues ...
If Player wins: "You win!" popup
If AI wins: "AI wins!" popup
If draw: "It's a draw!" popup

------------------------------------------------------------
License
------------------------------------------------------------
This project is open-source and free to use for learning and personal projects.
