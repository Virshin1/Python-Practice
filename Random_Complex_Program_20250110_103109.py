# Complex Python Program #15

```python
import logging
import random
import string
from dataclasses import dataclass, field
from typing import List, Dict, Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define dataclasses for data persistence
@dataclass
class Book:
    title: str
    author: str
    pages: int

@dataclass
class Library:
    books: List[Book] = field(default_factory=list)
    genres: List[str] = field(default_factory=list)
    location: str

# Define the Recommender class
class Recommender:

    def __init__(self, libraries: List[Library]):
        self.libraries = libraries
        self.genre_counts = self._calculate_genre_counts()

    def _calculate_genre_counts(self) -> Dict[str, int]:
        """Calculates the count of each genre across all libraries."""
        genre_counts = {}
        for library in self.libraries:
            for genre in library.genres:
                if genre not in genre_counts:
                    genre_counts[genre] = 0
                genre_counts[genre] += 1
        return genre_counts

    def recommend_library(self, user_genres: List[str]) -> Library:
        """Recommends a library based on the user's preferred genres."""
        if not user_genres:
            logging.error('No genres provided for recommendation.')
            return None

        # Calculate the score for each library
        scores = {}
        for library in self.libraries:
            score = 0
            for user_genre in user_genres:
                if user_genre in library.genres:
                    score += self.genre_counts[user_genre]
            scores[library] = score

        # Get the library with the highest score
        best_library = max(scores, key=scores.get)
        return best_library

# Generate random data for testing
def generate_random_data(num_libraries: int, num_books: int, num_genres: int):
    """Generates random data for libraries, books, and genres."""
    libraries = []
    genres = [''.join(random.choice(string.ascii_lowercase) for _ in range(10)) for _ in range(num_genres)]
    for _ in range(num_libraries):
        location = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        library = Library(location=location)
        for _ in range(random.randint(1, num_books)):
            title = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
            author = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
            pages = random.randint(100, 1000)
            book = Book(title=title, author=author, pages=pages)
            library.books.append(book)
            for _ in range(random.randint(1, num_genres)):
                genre = random.choice(genres)
                library.genres.append(genre)
        libraries.append(library)
    return libraries

# Main function
def main():
    # Generate random data
    libraries = generate_random_data(num_libraries=10, num_books=100, num_genres=10)

    # Create a recommender object
    recommender = Recommender(libraries)

    # Get user input for preferred genres
    user_genres = input('Enter your preferred genres (comma-separated): ').split(',')

    # Get the recommended library
    recommended_library = recommender.recommend_library(user_genres)

    # Print the recommended library
    if recommended_library:
        print(f'Recommended library: {recommended_library.location}')
    else:
        print('No suitable library found.')

if __name__ == '__main__':
    main()
```