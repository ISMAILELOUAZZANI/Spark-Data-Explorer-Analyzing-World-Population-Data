import pandas as pd
from prophet import Prophet

def train_forecast_model(df):
    # Aggregate sales per day
    daily = df.resample('D', on='timestamp').sum().reset_index()
    prophet_df = daily.rename(columns={'timestamp':'ds', 'units_sold':'y'})
    m = Prophet()
    m.fit(prophet_df)
    future = m.make_future_dataframe(periods=7)
    forecast = m.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

if __name__ == "__main__":
    df = pd.read_csv('data/streamed_sales.csv', names=['timestamp', 'product', 'units_sold', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    forecast = train_forecast_model(df)
    print(forecast.tail())