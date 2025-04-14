from pyspark.sql import SparkSession

def get_spark_session(app_name="SparkPipeline"):
    return (
        SparkSession.builder
        .appName(app_name)
        .getOrCreate()
    )