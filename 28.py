# Complex Python Program #28

```python
import random
import logging
from typing import List, Tuple, Dict
from enum import Enum

# Enable logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Define a custom exception
class InvalidMoveError(Exception):
    pass

# Define an enum for the different types of moves
class MoveType(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

# Define a class for a player
class Player:
    def __init__(self, name: str, move_type: MoveType):
        self.name = name
        self.move_type = move_type

    def get_move(self) -> MoveType:
        return self.move_type

# Define a class for a game of Rock, Paper, Scissors
class RPSGame:
    def __init__(self, players: List[Player]):
        self.players = players
        self.current_round = 0

    def play_round(self) -> Tuple[Player, MoveType]:
        winner = None
        winning_move = None

        # Get the moves from each player
        moves = [player.get_move() for player in self.players]

        # Check if there is a tie
        if all(move == moves[0] for move in moves):
            logger.info("Tie!")
            return None, None

        # Determine the winner
        for player, move in zip(self.players, moves):
            if move == MoveType.ROCK:
                if moves.count(MoveType.PAPER) > 0:
                    winner = [player for player in self.players if player.get_move() == MoveType.PAPER][0]
                    winning_move = MoveType.PAPER
                elif moves.count(MoveType.SCISSORS) > 0:
                    winner = player
                    winning_move = MoveType.ROCK
            elif move == MoveType.PAPER:
                if moves.count(MoveType.SCISSORS) > 0:
                    winner = [player for player in self.players if player.get_move() == MoveType.SCISSORS][0]
                    winning_move = MoveType.SCISSORS
                elif moves.count(MoveType.ROCK) > 0:
                    winner = player
                    winning_move = MoveType.PAPER
            elif move == MoveType.SCISSORS:
                if moves.count(MoveType.ROCK) > 0:
                    winner = [player for player in self.players if player.get_move() == MoveType.ROCK][0]
                    winning_move = MoveType.ROCK
                elif moves.count(MoveType.PAPER) > 0:
                    winner = player
                    winning_move = MoveType.SCISSORS

        # Log the winner and the winning move
        logger.info(f"{winner.name} wins with {winning_move.name}!")

        # Increment the current round
        self.current_round += 1

        return winner, winning_move

    def play_game(self) -> Dict[Player, int]:
        # Initialize the scores
        scores = {player: 0 for player in self.players}

        # Play the game until there is a winner
        while True:
            # Play a round
            winner, winning_move = self.play_round()

            # If there is a winner, increment their score
            if winner is not None:
                scores[winner] += 1

            # Check if there is a winner
            if any(score >= 3 for score in scores.values()):
                break

        # Return the scores
        return scores

# Generate random player names
player_names = [f"Player {i}" for i in range(1, 6)]

# Create a list of players
players = [Player(name, random.choice(list(MoveType))) for name in player_names]

# Create a game
game = RPSGame(players)

# Play the game
scores = game.play_game()

# Print the scores
for player, score in scores.items():
    print(f"{player.name}: {score}")
```