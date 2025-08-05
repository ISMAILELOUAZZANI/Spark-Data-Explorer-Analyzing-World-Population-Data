import pandas as pd

def load_data(ratings_path, movies_path):
    ratings = pd.read_csv(ratings_path, sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
    movies = pd.read_csv(movies_path, sep='|', encoding='latin-1', header=None, usecols=[0,1], names=['movie_id', 'title'])
    return pd.merge(ratings, movies, on='movie_id')