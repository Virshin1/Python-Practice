# Complex Python Program #16

```python
import random
import logging
from typing import List, Tuple, Dict
from dataclasses import dataclass

# Define custom logging configuration
logging.basicConfig(
    filename='unique_program.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Custom exception classes
class InvalidInputError(Exception):
    pass

class CalculationError(Exception):
    pass

# Dataclass to represent a game state
@dataclass
class GameState:
    board: List[List[int]]
    score: int
    moves: int

# Game class encapsulates the game logic
class Game:

    def __init__(self, size: int):
        self.size = size
        self.reset()

    # Initialize game state
    def reset(self):
        self.board = [[0] * self.size for _ in range(self.size)]
        self.score = 0
        self.moves = 0

    # Make a move on the board (places a tile)
    def make_move(self, row: int, col: int, value: int):
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise InvalidInputError(f"Invalid move: ({row}, {col})")
        if self.board[row][col] != 0:
            raise InvalidInputError(f"Cell already occupied: ({row}, {col})")
        self.board[row][col] = value
        self.moves += 1
        self.score += value

    # Check if there are any adjacent tiles with the same value
    def check_adjacent(self) -> bool:
        for row in range(self.size):
            for col in range(self.size):
                value = self.board[row][col]
                if value == 0:
                    continue
                # Check adjacent tiles
                for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if 0 <= row+i < self.size and 0 <= col+j < self.size and self.board[row+i][col+j] == value:
                        return True
        return False

    # Remove adjacent tiles with the same value and update score
    def remove_adjacent(self):
        removed_count = 0
        for row in range(self.size):
            for col in range(self.size):
                value = self.board[row][col]
                if value == 0:
                    continue
                # Check adjacent tiles
                tile_group = [(row, col)]
                for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if 0 <= row+i < self.size and 0 <= col+j < self.size and self.board[row+i][col+j] == value:
                        tile_group.append((row+i, col+j))
                if len(tile_group) > 1:
                    # Remove the tiles and update score
                    for i, j in tile_group:
                        self.board[i][j] = 0
                    removed_count += 1
                    self.score += len(tile_group) ** 2
        logging.debug(f"Removed {removed_count} groups of adjacent tiles.")

    # Generate a random tile and place it on the board
    def generate_tile(self):
        while True:
            row = random.randint(0, self.size-1)
            col = random.randint(0, self.size-1)
            if self.board[row][col] == 0:
                self.board[row][col] = random.randint(1, 9)
                logging.debug(f"Generated tile at ({row}, {col}) with value {self.board[row][col]}")
                break

    # Check if the game is over
    def is_over(self) -> bool:
        return not self.check_adjacent() and all(value != 0 for row in self.board for value in row)

    # Get game state as a string
    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.board])

# Main game loop
def main():
    try:
        size = int(input("Enter the board size (e.g. 4 for a 4x4 board): "))
        game = Game(size)
        print(f"Game started on a {size}x{size} board.")

        while not game.is_over():
            print(f"\nCurrent board:\n{game}")
            print(f"Score: {game.score}, Moves: {game.moves}")
            try:
                row, col, value = map(int, input("Enter your move (row, col, value): ").split())
                game.make_move(row, col, value)
            except InvalidInputError as e:
                print(f"Error: {e}")
            game.remove_adjacent()
            game.generate_tile()

        print("\nGame over!")
        print(f"Final board:\n{game}")
        print(f"Final score: {game.score}, Total moves: {game.moves}")
    except CalculationError as e:
        print(f"Calculation error: {e}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
```