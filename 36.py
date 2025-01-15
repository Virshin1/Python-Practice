# Complex Python Program #36

```python
import logging
import random
import typing as t

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the core class
class RandomGenerator:

    def __init__(self, seed: int) -> None:
        """
        Initializes the random generator with the given seed.

        :param seed: The seed to use for the random generator.
        """
        random.seed(seed)

    def generate(self, length: int, range: t.Tuple[int, int]) -> str:
        """
        Generates a random string of the given length within the given range.

        :param length: The length of the string to generate.
        :param range: The range of characters to use in the string.
        :return: The generated string.
        """
        try:
            if length <= 0:
                raise ValueError("Length must be positive")
            if range[1] - range[0] < length:
                raise ValueError("Range is too small")
            return ''.join(random.choice(range(range[0], range[1] + 1)) for _ in range(length))
        except Exception as e:
            logging.error(f"Error generating random string: {e}")
            raise

# Define a subclass that inherits from the core class
class SecureRandomGenerator(RandomGenerator):

    def __init__(self, seed: int) -> None:
        """
        Initializes the random generator with the given seed.

        :param seed: The seed to use for the random generator.
        """
        super().__init__(seed)

    def generate(self, length: int, range: t.Tuple[int, int], strength: int = 1) -> str:
        """
        Generates a secure random string of the given length within the given range.

        The strength parameter specifies how strong the random string should be.
        The higher the strength, the more secure the string will be, but also the slower it will be to generate.

        :param length: The length of the string to generate.
        :param range: The range of characters to use in the string.
        :param strength: The strength of the random string.
        :return: The generated string.
        """
        try:
            if length <= 0:
                raise ValueError("Length must be positive")
            if range[1] - range[0] < length:
                raise ValueError("Range is too small")
            if strength < 1:
                raise ValueError("Strength must be at least 1")
            return ''.join(random.choice(range(range[0], range[1] + 1)) for _ in range(length * strength))
        except Exception as e:
            logging.error(f"Error generating secure random string: {e}")
            raise

# Define a class that uses the random generator
class PasswordManager:

    def __init__(self, seed: int) -> None:
        """
        Initializes the password manager with the given seed.

        :param seed: The seed to use for the random generator.
        """
        self.generator = SecureRandomGenerator(seed)

    def generate_password(self, length: int = 16) -> str:
        """
        Generates a secure random password of the given length.

        :param length: The length of the password to generate.
        :return: The generated password.
        """
        try:
            return self.generator.generate(length, range(33, 127), strength=4)
        except Exception as e:
            logging.error(f"Error generating password: {e}")
            raise

# Test the program
if __name__ == "__main__":
    try:
        # Create a random generator
        generator = RandomGenerator(42)

        # Generate a random string
        string = generator.generate(10, range(ord('a'), ord('z') + 1))
        print(f"Generated string: {string}")

        # Create a secure random generator
        secure_generator = SecureRandomGenerator(42)

        # Generate a secure random string
        secure_string = secure_generator.generate(10, range(ord('a'), ord('z') + 1), strength=4)
        print(f"Generated secure string: {secure_string}")

        # Create a password manager
        manager = PasswordManager(42)

        # Generate a password
        password = manager.generate_password()
        print(f"Generated password: {password}")
    except Exception as e:
        logging.error(f"Error: {e}")
```