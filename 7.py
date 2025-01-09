# Complex Python Program #7

```python
import logging
import random
from dataclasses import dataclass
from typing import List, Tuple

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

@dataclass
class Item:
    name: str
    value: int
    weight: int

@dataclass
class Bag:
    items: List[Item]
    capacity: int

def knapsack(items: List[Item], capacity: int) -> int:
    """
    Finds the maximum total value of items that can be placed into a knapsack of a given capacity.

    Parameters:
        items (List[Item]): List of items, each with a name, value, and weight.
        capacity (int): Capacity of the knapsack.

    Returns:
        int: Maximum total value of items that can be placed into the knapsack.
    """

    # Create a matrix to store the maximum total value for each item and capacity.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    # Iterate over the items and capacities.
    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            # If the current item's weight is greater than the current capacity, then it cannot be included in the knapsack.
            if items[i - 1].weight > j:
                dp[i][j] = dp[i - 1][j]
            # Otherwise, the maximum total value is the maximum of the value with the current item and the value without the current item.
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1].weight] + items[i - 1].value)

    # Return the maximum total value.
    return dp[len(items)][capacity]

def generate_random_items(num_items: int, max_value: int, max_weight: int) -> List[Item]:
    """
    Generates a list of random items with random values and weights.

    Parameters:
        num_items (int): Number of items to generate.
        max_value (int): Maximum value of an item.
        max_weight (int): Maximum weight of an item.

    Returns:
        List[Item]: List of randomly generated items.
    """

    items = []
    for _ in range(num_items):
        items.append(Item(str(random.randint(1, num_items)), random.randint(1, max_value), random.randint(1, max_weight)))

    return items

def generate_random_bag(capacity: int) -> Bag:
    """
    Generates a random bag with a random capacity.

    Parameters:
        capacity (int): Capacity of the bag.

    Returns:
        Bag: Randomly generated bag.
    """

    return Bag([], capacity)

def main():
    # Generate a random list of items and a random bag.
    items = generate_random_items(10, 100, 100)
    bag = generate_random_bag(100)

    # Find the maximum total value of items that can be placed into the bag.
    max_value = knapsack(items, bag.capacity)

    # Log the result.
    logger.info(f"Maximum total value: {max_value}")

if __name__ == "__main__":
    main()
```