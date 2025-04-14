from pyspark.sql import SparkSession



def extract_from_kafka(spark: SparkSession, partition: int = 0):
    return spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("assign", f"""{{"raw-events":[{partition}]}}""") \
        .option("startingOffsets", "earliest") \
        .load()
