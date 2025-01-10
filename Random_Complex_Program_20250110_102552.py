# Complex Python Program #15

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Tuple
import logging
import random

# Setup logging
logging.basicConfig(
    filename='unique_program.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Unique Functionality: Generating a random crossword puzzle
# Advanced Concepts: Object-Oriented Programming, Composition, Iteration, Error Handling

class Grid:
    """
    Represents the grid of the crossword puzzle.

    Attributes:
        width (int): The width of the grid.
        height (int): The height of the grid.
        cells (Dict[Tuple[int, int], Cell]): A dictionary of cells, where the keys are tuples of (row, column) and the values are the corresponding cells.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes a new Grid object.

        Args:
            width (int): The width of the grid.
            height (int): The height of the grid.
        """
        self.width = width
        self.height = height
        self.cells = {(row, column): Cell() for row in range(self.height) for column in range(self.width)}

    def get_cell(self, row: int, column: int) -> Cell:
        """
        Gets the cell at the specified row and column.

        Args:
            row (int): The row of the cell to get.
            column (int): The column of the cell to get.

        Returns:
            Cell: The cell at the specified row and column.
        """
        try:
            return self.cells[(row, column)]
        except KeyError:
            logging.error("Invalid cell coordinates: ({}, {})".format(row, column))
            raise ValueError("Invalid cell coordinates")

    def __str__(self) -> str:
        """
        Returns a string representation of the grid.

        Returns:
            str: A string representation of the grid.
        """
        return "\n".join(" ".join(cell.get_character() for cell in row) for row in self.cells)

class Cell:
    """
    Represents a cell in the crossword puzzle.

    Attributes:
        is_black (bool): True if the cell is black, False otherwise.
        character (str): The character in the cell.
    """

    def __init__(self) -> None:
        """
        Initializes a new Cell object.
        """
        self.is_black = False
        self.character = " "

    def set_black(self) -> None:
        """
        Sets the cell to be black.
        """
        self.is_black = True

    def set_character(self, character: str) -> None:
        """
        Sets the character in the cell.

        Args:
            character (str): The character to set in the cell.
        """
        self.character = character

    def get_character(self) -> str:
        """
        Gets the character in the cell.

        Returns:
            str: The character in the cell.
        """
        return self.character

class Word:
    """
    Represents a word in the crossword puzzle.

    Attributes:
        word (str): The word.
        row (int): The row of the word.
        column (int): The column of the word.
        direction (str): The direction of the word (either "across" or "down").
    """

    def __init__(self, word: str, row: int, column: int, direction: str) -> None:
        """
        Initializes a new Word object.

        Args:
            word (str): The word.
            row (int): The row of the word.
            column (int): The column of the word.
            direction (str): The direction of the word (either "across" or "down").
        """
        self.word = word
        self.row = row
        self.column = column
        self.direction = direction

    def get_cells(self, grid: Grid) -> List[Cell]:
        """
        Gets the cells that the word occupies in the grid.

        Args:
            grid (Grid): The grid to get the cells from.

        Returns:
            List[Cell]: The cells that the word occupies in the grid.
        """
        cells = []
        for i in range(len(self.word)):
            if self.direction == "across":
                cell = grid.get_cell(self.row, self.column + i)
            elif self.direction == "down":
                cell = grid.get_cell(self.row + i, self.column)
            else:
                raise ValueError("Invalid direction: {}".format(self.direction))
            cells.append(cell)
        return cells

    def __str__(self) -> str:
        """
        Returns a string representation of the word.

        Returns:
            str: A string representation of the word.
        """
        return "{} ({}, {}, {})".format(self.word, self.row, self.column, self.direction)

class CrosswordPuzzle:
    """
    Represents a crossword puzzle.

    Attributes:
        grid (Grid): The grid of the crossword puzzle.
        words (List[Word]): The words in the crossword puzzle.
    """

    def __init__(self, grid: Grid, words: List[Word]) -> None:
        """
        Initializes a new CrosswordPuzzle object.

        Args:
            grid (Grid): The grid of the crossword puzzle.
            words (List[Word]): The words in the crossword puzzle.
        """
        self.grid = grid
        self.words = words

    def generate_puzzle(self) -> None:
        """
        Generates the crossword puzzle.
        """
        # First, place the black cells in the grid
        for i in range(self.grid.width):
            for j in range(self.grid.height):
                if random.random() < 0.25:
                    self.grid.cells[(i, j)].set_black()

        # Then, place the words in the grid
        for word in self.words:
            while True:
                # Choose a random cell to start the word
                row = random.randint(0, self.grid.height - 1)
                column = random.randint(0, self.grid.width - 1)

                # Check if the cell is black or already occupied
                if self.grid.cells[(row, column)].is_black or self.grid.cells[(row, column)].character != " ":
                    continue

                # Check if the word fits in the grid
                if word.direction == "across" and column + len(word.word) > self.grid.width:
                    continue
                elif word.direction == "down" and row + len(word.word) > self.grid.height:
                    continue

                # Check if the word intersects any other words
                intersects = False
                for other_word in self.words:
                    if word == other_word:
                        continue
                    for cell in other_word.get_cells(self.grid):
                        if cell.character != " ":
                            intersects = True
                            break
                    if intersects:
                        break

                if intersects:
                    continue

                # If all checks pass, place the word in the grid
                for i in range(len(word.word)):
                    if word.direction == "across":
                        self.grid.cells[(row, column + i)].set_character(word.word[i])
                    elif word.direction == "down":
                        self.grid.cells[(row + i, column)].set_character(word.word[i])

                break

    def __str__(self) -> str:
        """
        Returns a string representation of the crossword puzzle.

        Returns:
            str: A string representation of the crossword puzzle.
        """
        return str(self.grid)

# Test the program
grid = Grid(10, 10)
words = [
    Word("CAT", 0, 0, "across"),
    Word("DOG", 3, 3, "down"),
    Word("HAT", 6, 2, "across"),
    Word("MAN", 1, 5, "down"),
    Word("SUN", 4, 7, "across"),
]
crossword_puzzle = CrosswordPuzzle(grid, words)
crossword_puzzle.generate_puzzle()
print(crossword_puzzle)
```