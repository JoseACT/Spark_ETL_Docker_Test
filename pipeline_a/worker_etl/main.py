import uuid
import os
from pyspark.sql import SparkSession
from extract import extract_from_kafka
from transform import transform_data
from load import load_to_postgres

# Generate a unique batch ID for this ETL run
batch_id = uuid.uuid4()

spark = SparkSession.builder \
    .appName("KafkaSparkETL") \
    .master("spark://spark-master:7077") \
    .config("spark.jars.packages", ",".join([
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0",
        "org.postgresql:postgresql:42.7.2"
    ])) \
    .config("spark.sql.shuffle.partitions", "6") \
    .getOrCreate()

# Pipeline with batch ID passed through
# TODO add alerts for failed jobs

df_stage_1 = extract_from_kafka(spark)
# TODO add logging for each step
df_clean = transform_data(df_stage_1, batch_id=batch_id)

query = load_to_postgres(df_clean)
query.awaitTermination()
