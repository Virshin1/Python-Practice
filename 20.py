# Complex Python Program #20

```python
from dataclasses import dataclass
from enum import Enum
from functools import reduce
from typing import List, Dict, Tuple, Optional, Any
import logging
import random

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.DEBUG)

class Animal(Enum):
    """ An enum representing all the possible animals. """
    DOG = 1
    CAT = 2
    FISH = 3

@dataclass
class Pet:
    """ A class representing a pet. """
    name: str
    age: int
    animal: Animal

def find_oldest_pet_by_animal(pets: List[Pet]) -> Dict[Animal, Optional[Pet]]:
    """
    Finds the oldest pet of each animal type.

    Args:
        pets: The list of pets to search through.
    
    Returns:
        A dictionary mapping animal types to their oldest pet, or None if there are no pets of that type.
    """

    oldest_pets_by_animal: Dict[Animal, Optional[Pet]] = {}

    for pet in pets:
        if pet.animal not in oldest_pets_by_animal or pet.age > oldest_pets_by_animal[pet.animal].age:
            oldest_pets_by_animal[pet.animal] = pet

    return oldest_pets_by_animal

def find_most_common_animal_pair(pets: List[Pet]) -> Tuple[Animal, Animal]:
    """
    Finds the pair of animal types that appear most frequently together.

    Args:
        pets: The list of pets to search through.
    
    Returns:
        A tuple of the two animal types that appear most frequently together.
    """

    animal_pairs_counts: Dict[Tuple[Animal, Animal], int] = {}

    for pet1 in pets:
        for pet2 in pets:
            if pet1 is pet2:
                continue
            
            animal_pair = tuple(sorted((pet1.animal, pet2.animal)))
            if animal_pair not in animal_pairs_counts:
                animal_pairs_counts[animal_pair] = 0
            
            animal_pairs_counts[animal_pair] += 1

    most_common_animal_pair = max(animal_pairs_counts, key=animal_pairs_counts.get)
    return most_common_animal_pair
    
def find_average_age_of_pets(pets: List[Pet]) -> float:
    """
    Calculates the average age of all the pets.

    Args:
        pets: The list of pets to calculate the average age of.
    
    Returns:
        The average age of all the pets.
    """

    total_age = sum(pet.age for pet in pets)
    return total_age / len(pets)

def find_pet_with_most_unique_characteristics(pets: List[Pet]) -> Optional[Pet]:
    """
    Finds the pet with the most unique characteristics.

    Args:
        pets: The list of pets to search through.
    
    Returns:
        The pet with the most unique characteristics, or None if there are no pets with any unique characteristics.
    """

    def get_unique_characteristics(pet: Pet) -> int:
        """
        Gets the number of unique characteristics a pet has.

        Args:
            pet: The pet to get the number of unique characteristics of.
        
        Returns:
            The number of unique characteristics the pet has.
        """

        unique_characteristics = set()
        unique_characteristics.add(pet.name)
        unique_characteristics.add(pet.age)
        unique_characteristics.add(pet.animal)

        return len(unique_characteristics)

    pets_with_unique_characteristics = [(pet, get_unique_characteristics(pet)) for pet in pets]
    most_unique_characteristics = max(pets_with_unique_characteristics, key=lambda x: x[1])

    if most_unique_characteristics[1] == 0:
        return None
    else:
        return most_unique_characteristics[0]

def main():
    """
    The main function.
    """

    pets = [
        Pet("Buddy", 5, Animal.DOG),
        Pet("Kitty", 3, Animal.CAT),
        Pet("Nemo", 1, Animal.FISH),
        Pet("Max", 7, Animal.DOG),
        Pet("Whiskers", 2, Animal.CAT),
        Pet("Goldie", 4, Animal.FISH),
        Pet("Rover", 6, Animal.DOG),
        Pet("Mittens", 5, Animal.CAT),
        Pet("Bubbles", 3, Animal.FISH),
        Pet("Lucky", 8, Animal.DOG),
    ]

    oldest_pets_by_animal = find_oldest_pet_by_animal(pets)
    logging.info(f"Oldest pets by animal: {oldest_pets_by_animal}")

    most_common_animal_pair = find_most_common_animal_pair(pets)
    logging.info(f"Most common animal pair: {most_common_animal_pair}")

    average_age = find_average_age_of_pets(pets)
    logging.info(f"Average age of pets: {average_age}")

    pet_with_most_unique_characteristics = find_pet_with_most_unique_characteristics(pets)
    logging.info(f"Pet with most unique characteristics: {pet_with_most_unique_characteristics}")

if __name__ == "__main__":
    main()
```