# Complex Python Program #3

```python
from abc import ABC, abstractmethod
import random
import logging
import dataclasses
import asyncio

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Person:
    name: str
    age: int


class RandomGenerator(ABC):
    @abstractmethod
    def generate(self) -> int:
        pass


class Dice(RandomGenerator):
    def __init__(self, sides: int):
        self._sides = sides

    def generate(self) -> int:
        return random.randint(1, self._sides)


class Coin(RandomGenerator):
    def generate(self) -> int:
        return random.randint(0, 1)


class RandomNameGenerator:
    def __init__(self, first_names: list[str], last_names: list[str]):
        self._first_names = first_names
        self._last_names = last_names

    def generate(self) -> str:
        first_name = random.choice(self._first_names)
        last_name = random.choice(self._last_names)
        return f"{first_name} {last_name}"


class Game(ABC):
    @abstractmethod
    def play(self) -> None:
        pass


class DiceGame(Game):
    def __init__(self, dice: Dice, num_players: int):
        self._dice = dice
        self._num_players = num_players

    def play(self) -> None:
        for i in range(self._num_players):
            try:
                name = input(f"Player {i+1}, enter your name: ")
                age = int(input(f"{name}, enter your age: "))
            except ValueError:
                logging.error("Invalid age entered.", exc_info=True)
                continue

            person = Person(name, age)
            roll = self._dice.generate()
            logging.info(f"{person.name} rolled a {roll}")


class CoinFlipGame(Game):
    def __init__(self, coin: Coin, num_flips: int):
        self._coin = coin
        self._num_flips = num_flips

    async def play(self) -> None:
        heads = 0
        tails = 0

        for _ in range(self._num_flips):
            result = self._coin.generate()
            if result == 0:
                heads += 1
            else:
                tails += 1

        logging.info(f"Heads: {heads}, Tails: {tails}")


async def main():
    dice_game = DiceGame(Dice(6), 2)
    await dice_game.play()

    coin_game = CoinFlipGame(Coin(), 100)
    await coin_game.play()

asyncio.run(main())
```