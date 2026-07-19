from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Intro").master("local[*]").getOrCreate()

data = [
    ("Ada", "Engineering", 95000),
    ("Zain", "Data", 88000),
    ("Musa", "Engineering", 72000),
    ("Bola", "Data", 91000),
]
columns = ["name", "department", "salary"]

df = spark.createDataFrame(data, columns)

# This does NOT execute anything yet -- it just builds a plan
filtered = df.filter(df.salary > 80000)

print("Nothing has run yet!")

# THIS triggers execution
filtered.show()