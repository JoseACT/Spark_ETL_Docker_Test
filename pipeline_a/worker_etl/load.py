import yaml
from pyspark.sql import DataFrame
from pyspark.sql.streaming import StreamingQuery

def load_config(path="config.yaml") -> dict:
    with open(path, "r") as file:
        return yaml.safe_load(file)

# TODO implement other sinks like S3, HDFS, etc.
def load_to_postgres(df: DataFrame, config_path: str = "config.yaml") -> StreamingQuery:
    config = load_config(config_path)
    db = config["postgres"]

    def write_to_postgres(batch_df: DataFrame, batch_id: int):
        if not batch_df.rdd.isEmpty():
            batch_df.write \
                .format("jdbc") \
                .option("url", f"jdbc:postgresql://{db['host']}:{db['port']}/{db['database']}") \
                .option("dbtable", db["table"]) \
                .option("user", db["user"]) \
                .option("password", db["password"]) \
                .option("driver", "org.postgresql.Driver") \
                .mode("append") \
                .save()

    return df.writeStream \
             .foreachBatch(write_to_postgres) \
             .outputMode("append") \
             .option("checkpointLocation", config["checkpoint"]) \
             .start()