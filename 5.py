# Complex Python Program #5

```python
import random
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class RandomGenerator(ABC):
    """Abstract base class for random generators."""

    @abstractmethod
    def generate(self) -> int:
        """Generate a random number."""
        pass


class UniformRandomGenerator(RandomGenerator):
    """Uniform random generator."""

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def generate(self) -> int:
        try:
            return random.randint(self.min_value, self.max_value)
        except ValueError as e:
            logger.error(f"Invalid range: {e}")
            raise


class WeightedRandomGenerator(RandomGenerator):
    """Weighted random generator."""

    def __init__(self, weights: list[int]):
        self.weights = weights
        self.cumulative_weights = self._calculate_cumulative_weights()

    def _calculate_cumulative_weights(self) -> list[int]:
        return [sum(self.weights[:i + 1]) for i in range(len(self.weights))]

    def generate(self) -> int:
        try:
            random_value = random.random() * self.cumulative_weights[-1]
            for i, weight in enumerate(self.cumulative_weights):
                if random_value <= weight:
                    return i
            return len(self.weights) - 1
        except ValueError as e:
            logger.error(f"Invalid weights: {e}")
            raise


class RandomLottery:
    """Random lottery game."""

    def __init__(self, num_balls: int, ball_range: tuple[int, int], num_winners: int):
        self.num_balls = num_balls
        self.ball_range = ball_range
        self.random_generator = UniformRandomGenerator(*ball_range)
        self.num_winners = num_winners

    def play(self) -> list[int]:
        """Play the lottery and return the winning numbers."""
        winning_numbers = []
        for _ in range(self.num_winners):
            winning_numbers.append(self.random_generator.generate())
        return winning_numbers

    def check_winning(self, ticket_numbers: list[int]) -> bool:
        """Check if a ticket has won the lottery."""
        if len(set(ticket_numbers)) < len(set(self.ball_range)):
            return False
        return set(ticket_numbers) == set(winning_numbers)


if __name__ == "__main__":
    lottery = RandomLottery(num_balls=6, ball_range=(1, 49), num_winners=1)
    winning_numbers = lottery.play()
    ticket_numbers = [1, 2, 3, 4, 5, 6]
    is_winner = lottery.check_winning(ticket_numbers)

    if is_winner:
        print("Congratulations! You won the lottery!")
    else:
        print("Better luck next time!")
```