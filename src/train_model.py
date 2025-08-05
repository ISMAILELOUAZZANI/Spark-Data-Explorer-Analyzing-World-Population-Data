from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate
import pandas as pd

def train_model(data_path):
    df = pd.read_csv(data_path)
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'movie_id', 'rating']], reader)
    algo = SVD()
    results = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    return results

if __name__ == "__main__":
    merged = pd.read_csv('../data/merged.csv')
    train_model(merged)