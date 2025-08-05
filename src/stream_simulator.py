import pandas as pd
import time
import random
from datetime import datetime

def generate_sales_record():
    return {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'product': random.choice(['A', 'B', 'C', 'D']),
        'units_sold': random.randint(1, 10),
        'price': random.uniform(10, 100)
    }

def stream_sales_data(output_file='data/streamed_sales.csv', interval=2):
    with open(output_file, 'a') as f:
        while True:
            record = generate_sales_record()
            f.write(f"{record['timestamp']},{record['product']},{record['units_sold']},{record['price']:.2f}\n")
            f.flush()
            print(f"Streamed: {record}")
            time.sleep(interval)

if __name__ == "__main__":
    stream_sales_data()