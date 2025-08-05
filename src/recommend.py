from surprise import Dataset, Reader, SVD
import pandas as pd

def recommend_for_user(user_id, df):
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'movie_id', 'rating']], reader)
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)
    movie_ids = df['movie_id'].unique()
    user_movies = df[df['user_id'] == user_id]['movie_id']
    candidates = set(movie_ids) - set(user_movies)
    preds = [(mid, algo.predict(user_id, mid).est) for mid in candidates]
    preds.sort(key=lambda x: x[1], reverse=True)
    return preds[:10]

# Example usage:
# df = pd.read_csv('../data/merged.csv')
# print(recommend_for_user(1, df))