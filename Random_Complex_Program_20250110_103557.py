# Complex Python Program #15

```python
import json
import logging
import random
import string
from dataclasses import dataclass
from typing import List, Dict

# Enable logging
logging.basicConfig(level=logging.INFO)

# Define the deck of cards
DECK = [f"{rank}{suit}" for suit in ["♥", "♦", "♣", "♠"] for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

# Define the player's hand
class Hand:
    def __init__(self):
        self.cards: List[str] = []
    
    def add_card(self, card: str):
        self.cards.append(card)
    
    def get_score(self) -> int:
        score = 0
        for card in self.cards:
            rank = card[:-1]
            if rank.isdigit():
                score += int(rank)
            elif rank in ["J", "Q", "K"]:
                score += 10
            elif rank == "A":
                score += 11
        return score

# Define the game engine
class Game:
    def __init__(self):
        self.deck = DECK.copy()
        self.players: Dict[str, Hand] = {}
    
    def add_player(self, player_name: str):
        self.players[player_name] = Hand()
    
    def deal_cards(self):
        for player in self.players:
            for _ in range(2):
                card = random.choice(self.deck)
                self.deck.remove(card)
                self.players[player].add_card(card)
    
    def play(self):
        while True:
            for player in self.players:
                try:
                    choice = input(f"{player}'s turn (hit/stand): ")
                    if choice.lower() == "hit":
                        card = random.choice(self.deck)
                        self.deck.remove(card)
                        self.players[player].add_card(card)
                        if self.players[player].get_score() > 21:
                            logging.info(f"{player} busts with a score of {self.players[player].get_score()}")
                    elif choice.lower() == "stand":
                        continue
                    else:
                        raise ValueError(f"Invalid choice: {choice}")
                except ValueError as e:
                    logging.error(e)
                    continue
            
            # Check if all players have busted
            if all(player.get_score() > 21 for player in self.players):
                logging.info("All players bust")
                break
            
            # Check if any player has reached 21
            if any(player.get_score() == 21 for player in self.players):
                logging.info(f"{player} wins")
                break


# Main game loop
def main():
    # Create a new game
    game = Game()

    # Add players
    game.add_player("Player 1")
    game.add_player("Player 2")

    # Deal the cards
    game.deal_cards()

    # Play the game
    game.play()

if __name__ == "__main__":
    main()
```