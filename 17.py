# Complex Python Program #17

```python
import random
import string
import logging
from typing import List, Tuple, Dict
from dataclasses import dataclass, field

class Generator:
    """
    Class to generate random data.

    Args:
        length (int): The length of the data to generate.
    """
    def __init__(self, length: int) -> None:
        self.length = length

    def generate_random_string(self) -> str:
        """
        Generates a random string of characters.

        Returns:
            str: The generated random string.
        """
        return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(self.length))

    def generate_random_number(self) -> int:
        """
        Generates a random number.

        Returns:
            int: The generated random number.
        """
        return random.randint(0, self.length)

    def generate_random_list(self) -> List[int]:
        """
        Generates a random list of numbers.

        Returns:
            List[int]: The generated random list.
        """
        return random.sample(range(0, self.length), self.length)

    def generate_random_tuple(self) -> Tuple[int, str]:
        """
        Generates a random tuple of a number and a string.

        Returns:
            Tuple[int, str]: The generated random tuple.
        """
        return (self.generate_random_number(), self.generate_random_string())

    def generate_random_dict(self) -> Dict[str, int]:
        """
        Generates a random dictionary of strings and numbers.

        Returns:
            Dict[str, int]: The generated random dictionary.
        """
        return {self.generate_random_string(): self.generate_random_number() for _ in range(self.length)}

class Modifier:
    """
    Class to modify random data.

    Args:
        data (Union[str, int, List[int], Tuple[int, str], Dict[str, int]]): The data to modify.
    """
    def __init__(self, data: object) -> None:
        self.data = data

    def modify_string(self) -> str:
        """
        Modifies a string by reversing it.

        Returns:
            str: The modified string.
        """
        return self.data[::-1]

    def modify_number(self) -> int:
        """
        Modifies a number by adding 1 to it.

        Returns:
            int: The modified number.
        """
        return self.data + 1

    def modify_list(self) -> List[int]:
        """
        Modifies a list by sorting it.

        Returns:
            List[int]: The modified list.
        """
        return sorted(self.data)

    def modify_tuple(self) -> Tuple[int, str]:
        """
        Modifies a tuple by swapping the order of the elements.

        Returns:
            Tuple[int, str]: The modified tuple.
        """
        return (self.data[1], self.data[0])

    def modify_dict(self) -> Dict[str, int]:
        """
        Modifies a dictionary by reversing the keys and values.

        Returns:
            Dict[str, int]: The modified dictionary.
        """
        return {v: k for k, v in self.data.items()}

@dataclass
class Data:
    """
    Data class to store the generated and modified data.

    Args:
        original_data (Union[str, int, List[int], Tuple[int, str], Dict[str, int]]): The original data.
        modified_data (Union[str, int, List[int], Tuple[int, str], Dict[str, int]]): The modified data.
    """
    original_data: object = field(default=None)
    modified_data: object = field(default=None)

def main():
    try:
        # Set up logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Generate random data
        generator = Generator(10)
        random_string = generator.generate_random_string()
        random_number = generator.generate_random_number()
        random_list = generator.generate_random_list()
        random_tuple = generator.generate_random_tuple()
        random_dict = generator.generate_random_dict()

        logging.info(f"Random string: {random_string}")
        logging.info(f"Random number: {random_number}")
        logging.info(f"Random list: {random_list}")
        logging.info(f"Random tuple: {random_tuple}")
        logging.info(f"Random dictionary: {random_dict}")

        # Modify random data
        modifier = Modifier(random_string)
        modified_string = modifier.modify_string()
        modifier = Modifier(random_number)
        modified_number = modifier.modify_number()
        modifier = Modifier(random_list)
        modified_list = modifier.modify_list()
        modifier = Modifier(random_tuple)
        modified_tuple = modifier.modify_tuple()
        modifier = Modifier(random_dict)
        modified_dict = modifier.modify_dict()

        logging.info(f"Modified string: {modified_string}")
        logging.info(f"Modified number: {modified_number}")
        logging.info(f"Modified list: {modified_list}")
        logging.info(f"Modified tuple: {modified_tuple}")
        logging.info(f"Modified dictionary: {modified_dict}")

        # Store data in Data class
        data = Data(random_string, modified_string)
        data.modified_data = modified_number
        data.original_data = random_list
        data.modified_data = modified_list
        data.original_data = random_tuple
        data.modified_data = modified_tuple
        data.original_data = random_dict
        data.modified_data = modified_dict

        # Print data
        print(data)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```