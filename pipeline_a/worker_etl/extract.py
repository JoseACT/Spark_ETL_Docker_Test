from pyspark.sql import SparkSession


# Function to extract data from Kafka

# TODO implement usage of topics and paritions from the environment variables
def extract_from_kafka(spark):
    return spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("subscribe", "raw-events") \
        .option("startingOffsets", "earliest") \
        .load()