# Complex Python Program #15

```python
import random
import logging
import sys

logging.basicConfig(filename='game.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Board:
    def __init__(self, size: int):
        """
        Initializes a new game board with the given size.

        Args:
            size: The size of the board.
        """
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def place_piece(self, x: int, y: int, player: int):
        """
        Places a piece on the board at the given coordinates.

        Args:
            x: The x coordinate of the piece.
            y: The y coordinate of the piece.
            player: The player who is placing the piece.
        """
        if self.board[x][y] != 0:
            raise ValueError("Invalid move: the given coordinates are already occupied.")
        self.board[x][y] = player

    def check_winner(self) -> int:
        """
        Checks if there is a winner on the board.

        Returns:
            The player who won, or 0 if there is no winner.
        """
        # Check for horizontal wins
        for i in range(self.size):
            if all(self.board[i][j] == self.board[i][0] and self.board[i][0] != 0 for j in range(self.size)):
                return self.board[i][0]

        # Check for vertical wins
        for j in range(self.size):
            if all(self.board[i][j] == self.board[0][j] and self.board[0][j] != 0 for i in range(self.size)):
                return self.board[0][j]

        # Check for diagonal wins
        if all(self.board[i][i] == self.board[0][0] and self.board[0][0] != 0 for i in range(self.size)):
            return self.board[0][0]
        if all(self.board[i][self.size - 1 - i] == self.board[0][self.size - 1] and self.board[0][self.size - 1] != 0
                for i in range(self.size)):
            return self.board[0][self.size - 1]

        # Check for a tie
        if all(all(self.board[i][j] != 0 for j in range(self.size)) for i in range(self.size)):
            return 0

        # No winner yet
        return -1


class Player:
    def __init__(self, name: str, player_number: int):
        """
        Initializes a new player.

        Args:
            name: The name of the player.
            player_number: The player's number (1 or 2).
        """
        self.name = name
        self.player_number = player_number

    def make_move(self, board: Board):
        """
        Makes a move on the board.

        Args:
            board: The board to make the move on.
        """
        while True:
            try:
                x, y = map(int, input("Enter your move (x, y): ").split())
                board.place_piece(x, y, self.player_number)
                break
            except ValueError:
                print("Invalid move. Please try again.")


class Game:
    def __init__(self, size: int, players: list[Player]):
        """
        Initializes a new game.

        Args:
            size: The size of the board.
            players: The list of players.
        """
        self.board = Board(size)
        self.players = players
        self.current_player = 0

    def play(self):
        """
        Plays the game.
        """
        while True:
            player = self.players[self.current_player]
            player.make_move(self.board)
            winner = self.board.check_winner()
            if winner != -1:
                print(f"{player.name} wins!")
                break
            self.current_player = (self.current_player + 1) % len(self.players)


if __name__ == "__main__":
    try:
        size = int(input("Enter the size of the board: "))
        player1 = Player(input("Enter the name of player 1: "), 1)
        player2 = Player(input("Enter the name of player 2: "), 2)
        game = Game(size, [player1, player2])
        game.play()
    except ValueError:
        print("Invalid input. Please try again.")
    except Exception as e:
        logging.exception(e)
        print("An error occurred. Please try again.")
```