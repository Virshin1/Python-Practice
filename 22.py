# Complex Python Program #22

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Tuple, Union
import random
import logging
from collections import defaultdict

class PetType(Enum):
    CAT = 1
    DOG = 2
    FISH = 3

class Pet:
    def __init__(self, name: str, type: PetType, age: int):
        self.name = name
        self.type = type
        self.age = age

class PetShelter:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        self.pets.remove(pet)

    def get_pets_by_type(self, pet_type: PetType) -> List[Pet]:
        return [pet for pet in self.pets if pet.type == pet_type]

class PetFinder:
    def __init__(self, shelters: List[PetShelter]):
        self.shelters = shelters

    def find_pet(self, pet_type: PetType, age: int) -> Union[Pet, None]:
        for shelter in self.shelters:
            pets = shelter.get_pets_by_type(pet_type)
            for pet in pets:
                if pet.age == age:
                    return pet
        return None

def main():
    try:
        shelter1 = PetShelter()
        shelter2 = PetShelter()

        shelter1.add_pet(Pet("Fluffy", PetType.CAT, 3))
        shelter1.add_pet(Pet("Whiskers", PetType.CAT, 1))
        shelter2.add_pet(Pet("Spot", PetType.DOG, 5))
        shelter2.add_pet(Pet("Fido", PetType.DOG, 2))

        pet_finder = PetFinder([shelter1, shelter2])

        pet = pet_finder.find_pet(PetType.CAT, 3)
        if pet:
            print(f"Found a {pet.type} named {pet.name} at {pet.age} years old.")
        else:
            print("No pet found.")

    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()
```