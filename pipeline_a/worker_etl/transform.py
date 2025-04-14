from pyspark.sql import DataFrame
from pyspark.sql.functions import from_json, col, current_timestamp, expr, lit, when
from pyspark.sql.types import StructType, StringType, FloatType, IntegerType
import uuid

# Define input schema
schema = StructType() \
    .add("id", IntegerType()) \
    .add("clientId", IntegerType()) \
    .add("value", FloatType()) \
    .add("createdAt", StringType()) \
    .add("typeTransaction", StringType()) \
    .add("sourceId", StringType())

def transform_data(df: DataFrame, batch_id: uuid.UUID = None) -> DataFrame:
    batch_id_str = str(batch_id or uuid.UUID(int=0))
    df_json = df.selectExpr("CAST(value AS STRING)") \
                .select(from_json(col("value"), schema).alias("data")) \
                .select("data.*")

    # Now we have Spark context, define mapping safely
    type_map = when(col("typeTransaction") == "transfer", 1) \
               .when(col("typeTransaction") == "refund", 2) \
               .otherwise(0)

    df_transformed = df_json \
        .withColumn("oldId", col("id").cast("string")) \
        .withColumn("sourceId", col("sourceId").cast("int")) \
        .withColumn("typeTransaction", type_map.cast("int")) \
        .withColumn("createdAt", col("createdAt").cast("timestamp")) \
        .withColumn("processedAt", current_timestamp()) \
        .withColumn("batchid", lit(batch_id_str))\
        .select("clientId", "sourceId", "oldId", "value", "createdAt", "typeTransaction", "processedAt", "batchId")
        
        #.withColumn("batchId", lit(batch_id or "00000000-0000-0000-0000-000000000000").cast("string"))\
        #.withColumn("batchid", lit(batch_id).cast("string").cast("uuid"))\

    return df_transformed