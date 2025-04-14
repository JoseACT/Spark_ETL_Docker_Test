from pyspark.sql import DataFrame
from pyspark.sql.functions import from_json, col, current_timestamp, expr, lit
from pyspark.sql.types import StructType, StringType, FloatType, IntegerType

# Input structure as defined by your generator
schema = StructType() \
    .add("id", IntegerType()) \
    .add("clientId", IntegerType()) \
    .add("value", FloatType()) \
    .add("createdAt", StringType()) \
    .add("typeTransaction", StringType()) \
    .add("sourceId", StringType())

def transform_data(df: DataFrame, batch_id: str = None) -> DataFrame:
    df_json = df.selectExpr("CAST(value AS STRING)") \
                .select(from_json(col("value"), schema).alias("data")) \
                .select("data.*")

    df_transformed = df_json \
        .withColumn("oldId", col("id").cast("string")) \
        .withColumn("processedAt", current_timestamp()) \
        .withColumn("batchId", lit(batch_id or "00000000-0000-0000-0000-000000000000")) \
        .select("clientId", "sourceId", "oldId", "value", "createdAt", "typeTransaction", "processedAt", "batchId")

    return df_transformed
