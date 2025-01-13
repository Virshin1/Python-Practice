# Complex Python Program #26

```python
import random
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class RandomGenerator:
    """
    Generates random numbers and performs various operations on them.

    Attributes:
        min_value (int): The minimum value that can be generated.
        max_value (int): The maximum value that can be generated.
    """

    def __init__(self, min_value: int, max_value: int):
        """
        Initializes a new RandomGenerator object.

        Args:
            min_value (int): The minimum value that can be generated.
            max_value (int): The maximum value that can be generated.
        """

        self.min_value = min_value
        self.max_value = max_value

    def generate_random_number(self) -> int:
        """
        Generates a random number between the minimum and maximum values.

        Returns:
            int: A random number between the minimum and maximum values.
        """

        return random.randint(self.min_value, self.max_value)

    def generate_random_list(self, size: int) -> List[int]:
        """
        Generates a random list of numbers between the minimum and maximum values.

        Args:
            size (int): The size of the list to generate.

        Returns:
            List[int]: A random list of numbers between the minimum and maximum values.
        """

        return [self.generate_random_number() for _ in range(size)]

    def generate_random_dict(self, size: int) -> Dict[int, int]:
        """
        Generates a random dictionary of numbers between the minimum and maximum values.

        Args:
            size (int): The size of the dictionary to generate.

        Returns:
            Dict[int, int]: A random dictionary of numbers between the minimum and maximum values.
        """

        return {self.generate_random_number(): self.generate_random_number() for _ in range(size)}


class RandomProcessor:
    """
    Performs various operations on a list of numbers.

    Attributes:
        numbers (List[int]): The list of numbers to process.
    """

    def __init__(self, numbers: List[int]):
        """
        Initializes a new RandomProcessor object.

        Args:
            numbers (List[int]): The list of numbers to process.
        """

        self.numbers = numbers

    def sum_numbers(self) -> int:
        """
        Sums all the numbers in the list.

        Returns:
            int: The sum of all the numbers in the list.
        """

        return sum(self.numbers)

    def average_numbers(self) -> float:
        """
        Averages all the numbers in the list.

        Returns:
            float: The average of all the numbers in the list.
        """

        return sum(self.numbers) / len(self.numbers)

    def max_number(self) -> int:
        """
        Finds the maximum number in the list.

        Returns:
            int: The maximum number in the list.
        """

        return max(self.numbers)

    def min_number(self) -> int:
        """
        Finds the minimum number in the list.

        Returns:
            int: The minimum number in the list.
        """

        return min(self.numbers)


class Randomizer:
    """
    Manages the generation and processing of random numbers.

    Attributes:
        generator (RandomGenerator): The random number generator to use.
        processor (RandomProcessor): The random number processor to use.
    """

    def __init__(self, generator: RandomGenerator, processor: RandomProcessor):
        """
        Initializes a new Randomizer object.

        Args:
            generator (RandomGenerator): The random number generator to use.
            processor (RandomProcessor): The random number processor to use.
        """

        self.generator = generator
        self.processor = processor

    def generate_and_process_random_numbers(self, size: int) -> Dict[str, Any]:
        """
        Generates a random list of numbers and processes them.

        Args:
            size (int): The size of the list to generate.

        Returns:
            Dict[str, Any]: A dictionary containing the generated list of numbers and the results of the processing.
        """

        numbers = self.generator.generate_random_list(size)
        results = self.processor.process_numbers(numbers)
        return {'numbers': numbers, 'results': results}


def main():
    try:
        min_value = int(input('Enter the minimum value: '))
        max_value = int(input('Enter the maximum value: '))
        size = int(input('Enter the size of the list: '))

        generator = RandomGenerator(min_value, max_value)
        processor = RandomProcessor([])
        randomizer = Randomizer(generator, processor)

        results = randomizer.generate_and_process_random_numbers(size)
        print(results)
    except ValueError:
        logging.error('Invalid input. Please enter integers.')


if __name__ == '__main__':
    main()
```