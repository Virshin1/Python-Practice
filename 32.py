# Complex Python Program #32

```python
import random
import logging

logging.basicConfig(filename='polymorphism.log', level=logging.DEBUG)

class Animal:

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

class Dog(Animal):

    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):

    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color

    def speak(self) -> str:
        return "Meow!"

class Parrot(Animal):

    def __init__(self, name: str, language: str):
        super().__init__(name)
        self.language = language

    def speak(self) -> str:
        return f"Polly wants a cracker in {self.language}!"

def main():
    try:
        animals = [Dog("Spot", "Golden Retriever"), Cat("Fluffy", "Orange"), Parrot("Polly", "English")]
        for animal in animals:
            print(animal.speak(), animal)
            logging.info(f'{animal.name} said {animal.speak()}')
    except Exception as e:
        logging.error(f'An error occurred: {e}', exc_info=True)

if __name__ == "__main__":
    main()
```