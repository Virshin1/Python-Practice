# Complex Python Program #15

```python
from typing import List, Dict, Any
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RandomGenerator:
    """
    A class that generates random values.

    Attributes:
        min_value (int): The minimum value that can be generated.
        max_value (int): The maximum value that can be generated.
    """

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def generate_int(self) -> int:
        """
        Generates a random integer between the minimum and maximum values.

        Returns:
            int: A random integer.
        """

        try:
            return random.randint(self.min_value, self.max_value)
        except ValueError as e:
            logging.error(f'Invalid range: {e}')
            raise

    def generate_float(self) -> float:
        """
        Generates a random float between the minimum and maximum values.

        Returns:
            float: A random float.
        """

        try:
            return random.uniform(self.min_value, self.max_value)
        except ValueError as e:
            logging.error(f'Invalid range: {e}')
            raise

    def generate_string(self, length: int) -> str:
        """
        Generates a random string of the specified length.

        Args:
            length (int): The length of the string to generate.

        Returns:
            str: A random string.
        """

        try:
            return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length))
        except ValueError as e:
            logging.error(f'Invalid length: {e}')
            raise


class RandomCollection:
    """
    A class that represents a collection of random values.

    Attributes:
        values (List[Any]): The list of random values.
        generator (RandomGenerator): The random generator used to generate the values.
    """

    def __init__(self, generator: RandomGenerator):
        self.values = []
        self.generator = generator

    def generate(self, count: int):
        """
        Generates a specified number of random values and adds them to the collection.

        Args:
            count (int): The number of random values to generate.
        """

        try:
            for _ in range(count):
                self.values.append(self.generator.generate_int())
        except ValueError as e:
            logging.error(f'Invalid count: {e}')
            raise

    def get_average(self) -> float:
        """
        Calculates the average of the random values in the collection.

        Returns:
            float: The average of the random values.
        """

        try:
            return sum(self.values) / len(self.values)
        except ZeroDivisionError as e:
            logging.error(f'Empty collection: {e}')
            raise


class Randomizer:
    """
    A class that generates random collections of values and calculates their averages.

    Attributes:
        generator (RandomGenerator): The random generator used to generate the collections.
        collections (List[RandomCollection]): The list of random collections.
    """

    def __init__(self, generator: RandomGenerator):
        self.generator = generator
        self.collections = []

    def generate_collections(self, count: int):
        """
        Generates a specified number of random collections and adds them to the list.

        Args:
            count (int): The number of random collections to generate.
        """

        try:
            for _ in range(count):
                collection = RandomCollection(self.generator)
                collection.generate(random.randint(1, 10))
                self.collections.append(collection)
        except ValueError as e:
            logging.error(f'Invalid count: {e}')
            raise

    def get_average_of_averages(self) -> float:
        """
        Calculates the average of the averages of the random collections.

        Returns:
            float: The average of the averages of the random collections.
        """

        try:
            return sum(collection.get_average() for collection in self.collections) / len(self.collections)
        except ZeroDivisionError as e:
            logging.error(f'Empty list of collections: {e}')
            raise


def main():
    """
    The main function of the program.
    """

    try:
        generator = RandomGenerator(1, 100)
        randomizer = Randomizer(generator)
        randomizer.generate_collections(10)
        average_of_averages = randomizer.get_average_of_averages()
        print(f'Average of averages: {average_of_averages:.2f}')
    except Exception as e:
        logging.error(f'An error occurred: {e}')


if __name__ == "__main__":
    main()
```