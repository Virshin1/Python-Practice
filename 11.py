# Complex Python Program #11

```python
import random
import string
import logging
from typing import List, Dict, Tuple

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define the main class
class GameBoard:
    """
    A class representing a game board.

    Attributes:
        size: The size of the board (number of rows and columns).
        grid: A 2D list representing the board.
    """

    def __init__(self, size: int):
        """
        Initializes the game board.

        Args:
            size: The size of the board (number of rows and columns).
        """

        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    def __str__(self) -> str:
        """
        Returns a string representation of the game board.

        Returns:
            A string representation of the game board.
        """

        return '\n'.join([' '.join(row) for row in self.grid])

    def place_piece(self, piece: str, row: int, col: int) -> bool:
        """
        Places a piece on the game board.

        Args:
            piece: The piece to place.
            row: The row to place the piece in.
            col: The column to place the piece in.

        Returns:
            True if the piece was placed successfully, False otherwise.
        """

        if row < 0 or row >= self.size or col < 0 or col >= self.size or self.grid[row][col] != ' ':
            return False

        self.grid[row][col] = piece
        return True

    def check_winner(self) -> str:
        """
        Checks if there is a winner on the game board.

        Returns:
            The winning piece ('X' or 'O'), or ' ' if there is no winner.
        """

        # Check rows
        for row in self.grid:
            if len(set(row)) == 1 and row[0] != ' ':
                return row[0]

        # Check columns
        for col in range(self.size):
            column = [row[col] for row in self.grid]
            if len(set(column)) == 1 and column[0] != ' ':
                return column[0]

        # Check diagonals
        diagonal1 = [self.grid[i][i] for i in range(self.size)]
        if len(set(diagonal1)) == 1 and diagonal1[0] != ' ':
            return diagonal1[0]

        diagonal2 = [self.grid[i][self.size - i - 1] for i in range(self.size)]
        if len(set(diagonal2)) == 1 and diagonal2[0] != ' ':
            return diagonal2[0]

        return ' '


# Define the player class
class Player:
    """
    A class representing a player in the game.

    Attributes:
        name: The name of the player.
        piece: The piece that the player uses.
    """

    def __init__(self, name: str, piece: str):
        """
        Initializes the player.

        Args:
            name: The name of the player.
            piece: The piece that the player uses.
        """

        self.name = name
        self.piece = piece


# Define the game class
class TicTacToe:
    """
    A class representing a game of Tic-Tac-Toe.

    Attributes:
        board: The game board.
        players: The players in the game.
        current_player: The player who is currently taking their turn.
    """

    def __init__(self, size: int):
        """
        Initializes the game.

        Args:
            size: The size of the game board.
        """

        self.board = GameBoard(size)
        self.players = [Player('Player 1', 'X'), Player('Player 2', 'O')]
        self.current_player = self.players[0]

    def start(self):
        """
        Starts the game.
        """

        while True:
            # Get the player's move
            move = self.get_move()

            # Place the piece on the board
            if not self.board.place_piece(self.current_player.piece, move[0], move[1]):
                logging.error("Invalid move")
                continue

            # Check if there is a winner
            winner = self.board.check_winner()
            if winner != ' ':
                logging.info(f"{winner} wins!")
                break

            # Switch to the other player
            self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]

    def get_move(self) -> Tuple[int, int]:
        """
        Gets the player's move.

        Returns:
            A tuple of the row and column of the player's move.
        """

        while True:
            try:
                move = input(f"{self.current_player.name}'s turn: ")
                row, col = map(int, move.split())
                if 0 <= row < self.board.size and 0 <= col < self.board.size:
                    return row, col
                else:
                    logging.error("Invalid move")
            except ValueError:
                logging.error("Invalid move")


# Create a new game
game = TicTacToe(3)

# Start the game
game.start()
```