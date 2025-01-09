# Complex Python Program #2

```python
import random
import logging
from typing import List, Tuple, Dict
from dataclasses import dataclass

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the Movie class
@dataclass
class Movie:
    """
    A class representing a movie.

    Attributes:
        title (str): The title of the movie.
        year (int): The year the movie was released.
        director (str): The director of the movie.
    """
    title: str
    year: int
    director: str

# Define the MovieCollection class
class MovieCollection:
    """
    A class representing a collection of movies.

    Attributes:
        movies (List[Movie]): A list of movies in the collection.
    """
    def __init__(self, movies: List[Movie] = []):
        self.movies = movies

    # Add a movie to the collection
    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    # Remove a movie from the collection
    def remove_movie(self, movie: Movie):
        self.movies.remove(movie)

    # Get a random movie from the collection
    def get_random_movie(self) -> Movie:
        try:
            return random.choice(self.movies)
        except IndexError:
            logging.error("The movie collection is empty.")
            raise

    # Get a list of movies by director
    def get_movies_by_director(self, director: str) -> List[Movie]:
        return [movie for movie in self.movies if movie.director == director]

    # Get a list of movies by year
    def get_movies_by_year(self, year: int) -> List[Movie]:
        return [movie for movie in self.movies if movie.year == year]

    # Get a list of movies by title
    def get_movies_by_title(self, title: str) -> List[Movie]:
        return [movie for movie in self.movies if movie.title == title]

# Define the MovieDatabase class
class MovieDatabase:
    """
    A class representing a database of movies.

    Attributes:
        movies (Dict[str, Movie]): A dictionary of movies, where the keys are the movie titles and the values are the Movie objects.
    """
    def __init__(self, movies: Dict[str, Movie] = {}):
        self.movies = movies

    # Add a movie to the database
    def add_movie(self, movie: Movie):
        self.movies[movie.title] = movie

    # Remove a movie from the database
    def remove_movie(self, title: str):
        del self.movies[title]

    # Get a movie from the database
    def get_movie(self, title: str) -> Movie:
        return self.movies[title]

    # Get a list of movies by director
    def get_movies_by_director(self, director: str) -> List[Movie]:
        return [movie for movie in self.movies.values() if movie.director == director]

    # Get a list of movies by year
    def get_movies_by_year(self, year: int) -> List[Movie]:
        return [movie for movie in self.movies.values() if movie.year == year]

    # Get a list of movies by title
    def get_movies_by_title(self, title: str) -> List[Movie]:
        return [movie for movie in self.movies.values() if movie.title == title]

# Create a movie collection
movies = MovieCollection([
    Movie("The Shawshank Redemption", 1994, "Frank Darabont"),
    Movie("The Godfather", 1972, "Francis Ford Coppola"),
    Movie("The Dark Knight", 2008, "Christopher Nolan"),
    Movie("12 Angry Men", 1957, "Sidney Lumet"),
    Movie("Schindler's List", 1993, "Steven Spielberg")
])

# Create a movie database
database = MovieDatabase()

# Add the movies from the collection to the database
for movie in movies.movies:
    database.add_movie(movie)

# Get a random movie from the database
random_movie = database.get_random_movie()
logging.info(f"Random movie: {random_movie.title}")

# Get a list of movies by director
movies_by_director = database.get_movies_by_director("Steven Spielberg")
logging.info(f"Movies by Steven Spielberg: {movies_by_director}")

# Get a list of movies by year
movies_by_year = database.get_movies_by_year(1994)
logging.info(f"Movies released in 1994: {movies_by_year}")

# Get a list of movies by title
movies_by_title = database.get_movies_by_title("The Shawshank Redemption")
logging.info(f"Movies with the title 'The Shawshank Redemption': {movies_by_title}")
```