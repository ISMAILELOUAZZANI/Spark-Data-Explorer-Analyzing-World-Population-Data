import pandas as pd

def load_streamed_data(file_path='data/streamed_sales.csv'):
    df = pd.read_csv(file_path, names=['timestamp', 'product', 'units_sold', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def get_sales_summary(df):
    summary = df.groupby('product').agg({'units_sold':'sum', 'price':'mean'})
    return summary

if __name__ == "__main__":
    df = load_streamed_data()
    print(get_sales_summary(df))