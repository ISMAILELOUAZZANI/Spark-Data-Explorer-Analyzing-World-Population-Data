# Spark Data Explorer: World Population Analysis

## Overview
A simple PySpark project to analyze and summarize world population data using basic Spark DataFrame operations.

## What It Demonstrates
- Reading CSV data with Spark
- Data cleaning and preprocessing
- Aggregation and sorting
- Saving results to new CSV files

## How to Run

1. **Install Spark & PySpark:**
    ```bash
    pip install pyspark
    ```

2. **Put your CSV file (`world_population.csv`) in the project folder.**
   - You can download a sample dataset from [here](https://github.com/datasets/population/blob/master/data/population.csv).

3. **Run the script:**
    ```bash
    python data_explorer.py
    ```

4. **See Results:**
   - The top 10 countries by recent population are displayed.
   - Output CSV (`top_10_countries_population.csv`) is generated.

## Customization
- Try grouping by continent if your data includes that.
- Add more transformations or visualizations as you learn more Spark skills!

## Certificate Value
This project demonstrates your ability to use Spark for real-world data analysis, fulfilling the objectives of Spark - Level 1.