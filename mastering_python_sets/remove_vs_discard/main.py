marvel_movies = {
    'Avengers: Endgame',
    'Black Panther',
    'Iron Man',
    'The Dark Knight',
    'Spider-Man: No Way Home',
    'Guardians of the Galaxy',
    'Justice League'
}

# Write your code here
# Does not raise an error if the element is not found; it simply leaves the set unchanged.
marvel_movies.discard("The Dark Knight")
# Raises a keyError if the element is not in the set.
marvel_movies.remove("Justice League")

# Testing
print("Updated set:", marvel_movies)