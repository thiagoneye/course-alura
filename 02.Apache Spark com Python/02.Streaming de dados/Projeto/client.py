"""
Formação Apache Spark
Streaming de Dados
"""

# Imports

from pyspark.sql import SparkSession


# Main

spark = SparkSession.builder.appName('sparkStreaming').getOrCreate()

lines = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9009)\
    .load()

query = lines.writeStream\
    .outputMode('append')\
    .format('console')\
    .start()

query.awaitTermination()

spark.stop()
