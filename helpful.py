# Make matrixes of user-item and make vector of [number in sequence, movie Id].
import pandas as pd
import numpy as np


def load_matrix():
    # Load data.
    movieLens = pd.read_csv('movieLens/ratings.csv')
    movieLens = movieLens.drop('timestamp', axis=1)

    # Vector of users.
    users = list(set(movieLens['userId']))
    # Vector of movies.
    films = list(pd.read_csv('movieLens/movies.csv')['movieId'])
    films = np.array([*zip(list(range(len(films) + 2))[1:], [0] + films)])
    # Make zero-matrix of user-movie.
    matrix = np.zeros((len(users) + 1, films[-1, 0] + 1))
    # For each user.
    for user in users:
        # What movie he rated.
        movie = list(set(movieLens[(movieLens['userId'] == user)]['movieId']))
        for film in movie:
            tmp = films[np.where(films[:, 1] == film)][:, 0] - 1
            # Add mark to matrix.
            matrix[user, films[tmp, 0]] = float(movieLens[((movieLens['userId'] == user) and (movieLens['movieId'] == film))]['rating'])
    return matrix
