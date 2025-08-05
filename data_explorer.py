from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

# 1. Create Spark session
spark = SparkSession.builder.appName("WorldPopulationAnalysis").getOrCreate()

# 2. Load world population dataset
df = spark.read.csv("world_population.csv", header=True, inferSchema=True)

# 3. Basic cleaning: drop rows with null values in key columns
df_clean = df.dropna(subset=["Year", "Value", "Country Name"])

# 4. Aggregate: total population by country for the most recent year
latest_year = df_clean.agg({"Year": "max"}).collect()[0][0]
df_latest = df_clean.filter(col("Year") == latest_year)

# 5. Top 10 countries by population
top_countries = df_latest.orderBy(col("Value").desc()).select("Country Name", "Value").limit(10)
print("Top 10 Countries by Population in", latest_year)
top_countries.show()

# 6. (Optional) Save results to CSV
top_countries.coalesce(1).write.csv("top_10_countries_population.csv", header=True, mode="overwrite")

spark.stop()