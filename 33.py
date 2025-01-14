# Complex Python Program #33

```python
import logging
import random
import string
from typing import List, Dict, Tuple

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Person:
    def __init__(self, name: str, age: int, occupation: str):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __str__(self):
        return f'{self.name} is a {self.age} year old {self.occupation}.'

class City:
    def __init__(self, name: str, population: int, mayor: Person):
        self.name = name
        self.population = population
        self.mayor = mayor

    def __str__(self):
        return f'{self.name} has a population of {self.population} and is led by {self.mayor}.'

class Country:
    def __init__(self, name: str, capital: City, cities: List[City], population: int, president: Person):
        self.name = name
        self.capital = capital
        self.cities = cities
        self.population = population
        self.president = president

    def __str__(self):
        return f'{self.name} has a population of {self.population} and is led by {self.president}.'

def generate_random_person(age_range: Tuple[int, int], occupation_list: List[str]) -> Person:
    """Generates a random person with a random name, age, and occupation."""
    try:
        min_age, max_age = age_range
        if min_age > max_age:
            raise ValueError('Minimum age must be less than maximum age.')
        age = random.randint(min_age, max_age)
        occupation = random.choice(occupation_list)
        name = ''.join(random.choices(string.ascii_letters, k=10))
        return Person(name, age, occupation)
    except ValueError as e:
        logging.error(e)
        raise

def generate_random_city(population_range: Tuple[int, int], mayor_list: List[Person]) -> City:
    """Generates a random city with a random name, population, and mayor."""
    try:
        min_population, max_population = population_range
        if min_population > max_population:
            raise ValueError('Minimum population must be less than maximum population.')
        population = random.randint(min_population, max_population)
        mayor = random.choice(mayor_list)
        name = ''.join(random.choices(string.ascii_letters, k=10))
        return City(name, population, mayor)
    except ValueError as e:
        logging.error(e)
        raise

def generate_random_country(population_range: Tuple[int, int], president_list: List[Person], city_count_range: Tuple[int, int], city_population_range: Tuple[int, int], mayor_list: List[Person]) -> Country:
    """Generates a random country with a random name, population, president, and a list of random cities."""
    try:
        min_population, max_population = population_range
        if min_population > max_population:
            raise ValueError('Minimum population must be less than maximum population.')
        population = random.randint(min_population, max_population)
        president = random.choice(president_list)
        min_city_count, max_city_count = city_count_range
        if min_city_count > max_city_count:
            raise ValueError('Minimum city count must be less than maximum city count.')
        city_count = random.randint(min_city_count, max_city_count)
        cities = []
        for _ in range(city_count):
            city = generate_random_city(city_population_range, mayor_list)
            cities.append(city)
        name = ''.join(random.choices(string.ascii_letters, k=10))
        capital = random.choice(cities)
        return Country(name, capital, cities, population, president)
    except ValueError as e:
        logging.error(e)
        raise

def main():
    try:
        age_range = (18, 100)
        occupation_list = ['Doctor', 'Lawyer', 'Engineer', 'Teacher', 'Student']
        mayor_list = [generate_random_person(age_range, occupation_list) for _ in range(10)]
        president_list = [generate_random_person(age_range, occupation_list) for _ in range(10)]
        city_count_range = (1, 10)
        city_population_range = (1000, 1000000)
        population_range = (100000, 100000000)
        country = generate_random_country(population_range, president_list, city_count_range, city_population_range, mayor_list)
        print(country)
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    main()
```