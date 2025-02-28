favorite_movies = ("Inception", "The Dark Knight", "Interstellar", "Memento", "The Prestige", "Dunkirk")

first_movie, *other_movies = favorite_movies
print(first_movie)
print(other_movies)


first_movie, *other_movies, last_movie = favorite_movies

print(first_movie)
print(last_movie)
