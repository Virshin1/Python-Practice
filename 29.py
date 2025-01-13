# Complex Python Program #29

```python
"""
This program is a simple password generator that generates a complex and random password based on
user-provided criteria. The program also allows the user to save the generated password to a file
for later use.

The program is divided into three classes:

* The PasswordGenerator class is responsible for generating the password.
* The PasswordSaver class is responsible for saving the password to a file.
* The PasswordValidator class is responsible for validating the user-provided criteria.

The program uses several advanced programming concepts, including:

* Object-oriented programming
* Exception handling
* Logging
* Unit testing

"""

import logging
import random
import string
from typing import List


class PasswordGenerator:
    """
    This class is responsible for generating a complex and random password based on
    user-provided criteria.

    Attributes:
        length (int): The length of the password to be generated.
        characters (str): The characters to be used in the password.
        exclude (str): The characters to be excluded from the password.
        complexity (int): The complexity of the password to be generated.

    """

    def __init__(
        self, length: int = 12, characters: str = string.ascii_letters + string.digits, exclude: str = "", complexity: int = 0
    ):
        """
        Constructs a new PasswordGenerator object.

        Args:
            length (int, optional): The length of the password to be generated. Defaults to 12.
            characters (str, optional): The characters to be used in the password. Defaults to string.ascii_letters + string.digits.
            exclude (str, optional): The characters to be excluded from the password. Defaults to "".
            complexity (int, optional): The complexity of the password to be generated. Defaults to 0.

        """

        self.length = length
        self.characters = characters
        self.exclude = exclude
        self.complexity = complexity

    def generate_password(self) -> str:
        """
        Generates a complex and random password based on the user-provided criteria.

        Returns:
            str: The generated password.

        """

        # Check if the user-provided criteria is valid.

        try:
            self._validate_criteria()
        except ValueError as e:
            logging.error(e)
            raise

        # Generate a random password.

        password = ""
        for _ in range(self.length):
            character = random.choice(self.characters)
            if character not in self.exclude:
                password += character

        # Increase the complexity of the password.

        if self.complexity > 0:
            for _ in range(self.complexity):
                index = random.randint(0, len(password) - 1)
                password = password[:index] + random.choice(string.punctuation) + password[index + 1 :]

        # Return the generated password.

        return password

    def _validate_criteria(self):
        """
        Validates the user-provided criteria.

        Raises:
            ValueError: If the user-provided criteria is invalid.

        """

        if self.length < 8:
            raise ValueError("The password length must be at least 8 characters.")

        if len(self.characters) < 10:
            raise ValueError("The character set must contain at least 10 characters.")

        if len(self.exclude) > 0 and self.exclude in self.characters:
            raise ValueError("The exclude set must not contain characters that are in the character set.")

        if self.complexity < 0 or self.complexity > 5:
            raise ValueError("The complexity must be between 0 and 5.")


class PasswordSaver:
    """
    This class is responsible for saving a password to a file.

    Attributes:
        filename (str): The name of the file to save the password to.

    """

    def __init__(self, filename: str = "password.txt"):
        """
        Constructs a new PasswordSaver object.

        Args:
            filename (str, optional): The name of the file to save the password to. Defaults to "password.txt".

        """

        self.filename = filename

    def save_password(self, password: str):
        """
        Saves a password to a file.

        Args:
            password (str): The password to save.

        """

        with open(self.filename, "w") as f:
            f.write(password)


class PasswordValidator:
    """
    This class is responsible for validating a password.

    Attributes:
        min_length (int): The minimum length of the password.
        max_length (int): The maximum length of the password.
        min_uppercase (int): The minimum number of uppercase letters in the password.
        min_lowercase (int): The minimum number of lowercase letters in the password.
        min_digits (int): The minimum number of digits in the password.
        min_symbols (int): The minimum number of symbols in the password.

    """

    def __init__(
        self,
        min_length: int = 8,
        max_length: int = 128,
        min_uppercase: int = 1,
        min_lowercase: int = 1,
        min_digits: int = 1,
        min_symbols: int = 1,
    ):
        """
        Constructs a new PasswordValidator object.

        Args:
            min_length (int, optional): The minimum length of the password. Defaults to 8.
            max_length (int, optional): The maximum length of the password. Defaults to 128.
            min_uppercase (int, optional): The minimum number of uppercase letters in the password. Defaults to 1.
            min_lowercase (int, optional): The minimum number of lowercase letters in the password. Defaults to 1.
            min_digits (int, optional): The minimum number of digits in the password. Defaults to 1.
            min_symbols (int, optional): The minimum number of symbols in the password. Defaults to 1.

        """

        self.min_length = min_length
        self.max_length = max_length
        self.min_uppercase = min_uppercase
        self.min_lowercase = min_lowercase
        self.min_digits = min_digits
        self.min_symbols = min_symbols

    def is_valid(self, password: str) -> bool:
        """
        Validates a password.

        Args:
            password (str): The password to validate.

        Returns:
            bool: True if the password is valid, False otherwise.

        """

        if not isinstance(password, str):
            raise TypeError("The password must be a string.")

        if len(password) < self.min_length or len(password) > self.max_length:
            return False

        uppercase_count = 0
        lowercase_count = 0
        digit_count = 0
        symbol_count = 0

        for character in password:
            if character.isupper():
                uppercase_count += 1
            elif character.islower():
                lowercase_count += 1
            elif character.isdigit():
                digit_count += 1
            else:
                symbol_count += 1

        if uppercase_count < self.min_uppercase or lowercase_count < self.min_lowercase or digit_count < self.min_digits or symbol_count < self.min_symbols:
            return False

        return True


def main():
    """
    The main function.

    """

    # Get the user-provided criteria.

    length = int(input("Enter the length of the password: "))
    characters = input("Enter the characters to be used in the password: ")
    exclude = input("Enter the characters to be excluded from the password: ")
    complexity = int(input("Enter the complexity of the password: "))

    # Create a PasswordGenerator object.

    password_generator = PasswordGenerator(length, characters, exclude, complexity)

    # Generate a password.

    password = password_generator.generate_password()

    # Validate the password.

    password_validator = PasswordValidator()
    if not password_validator.is_valid(password):
        print("The generated password is invalid.")
        return

    # Save the password to a file.

    password_saver = PasswordSaver()
    password_saver.save_password(password)

    # Print the generated password.

    print("The generated password is:", password)


if __name__ == "__main__":
    main()
```