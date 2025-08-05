import streamlit as st
import pandas as pd
from process_stream import load_streamed_data, get_sales_summary
from forecasting import train_forecast_model

st.title("📈 Real-Time Sales Dashboard")

df = load_streamed_data()
st.subheader("Raw Sales Data")
st.dataframe(df.tail(20))

st.subheader("Sales Summary")
summary = get_sales_summary(df)
st.table(summary)

st.subheader("Sales Forecast (Next 7 Days)")
forecast = train_forecast_model(df)
st.line_chart(forecast.set_index('ds')['yhat'])