import pyspark

df = spark.read.csv("cdc.csv", header=True, inferSchema=True)