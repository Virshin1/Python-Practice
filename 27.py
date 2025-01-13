# Complex Python Program #27

```python
import logging
import random
import secrets

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("random_program.log"), logging.StreamHandler()]
)

class RandomNumberGenerator:
    def __init__(self, seed=None):
        if seed is None:
            seed = secrets.randbelow(2**32)
        self.seed = seed
        self._state = seed

    def next_int(self, a, b):
        """
        Generate a random integer between `a` and `b` (inclusive).

        :param a: The lower bound of the range.
        :param b: The upper bound of the range.
        :raises ValueError: If `a` > `b`.
        :return: A random integer between `a` and `b`.
        """

        if a > b:
            raise ValueError("The lower bound must be less than or equal to the upper bound.")

        self._state = (self._state * 48271) % 2147483647
        return a + (self._state % (b - a + 1))

class RandomStringGenerator:
    def __init__(self, alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.alphabet = alphabet

    def next_string(self, length):
        """
        Generate a random string of the specified length.

        :param length: The length of the string to generate.
        :return: A random string of the specified length.
        """

        return "".join(random.choices(self.alphabet, k=length))

class RandomGenerator:
    def __init__(self, seed=None):
        self.number_generator = RandomNumberGenerator(seed)
        self.string_generator = RandomStringGenerator()

    def next_random(self):
        """
        Generate a random value of a random type.

        :return: A random value of a random type.
        """

        type = self.number_generator.next_int(0, 2)
        if type == 0:
            return self.number_generator.next_int(-100, 100)
        elif type == 1:
            return self.string_generator.next_string(self.number_generator.next_int(1, 10))
        else:
            return None

def main():
    logging.info("Generating 10 random values:")
    random_generator = RandomGenerator()
    for i in range(10):
        logging.info(random_generator.next_random())

if __name__ == "__main__":
    main()
```