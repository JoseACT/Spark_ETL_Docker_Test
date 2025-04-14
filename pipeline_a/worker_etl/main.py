import uuid
import os
from pyspark.sql import SparkSession
from extract import extract_from_kafka
from transform import transform_data
from load import load_to_postgres

# Generate a unique batch ID for this ETL run
batch_id = str(uuid.uuid4())

# Get the partition number from environment variable or default to 0
partition = int(os.getenv("PARTITION", "0"))

# SparkSession with required JARs
spark = SparkSession.builder \
    .appName("KafkaSparkETL") \
    .master("spark://spark-master:7077") \
    .config("spark.jars.packages", ",".join([
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0",
        "org.postgresql:postgresql:42.7.2"
    ])) \
    .getOrCreate()


# Pipeline with batch ID passed through
df_stage_1 = extract_from_kafka(spark)
df_clean = transform_data(df_stage_1, batch_id=batch_id)
query = load_to_postgres(df_clean)
query.awaitTermination()
