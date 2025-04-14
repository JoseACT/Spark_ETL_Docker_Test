# Spark_ETL_Docker_Test
Project to test Spark and Kafka using containers for each instance.

# Pipeline A (Test)

Random Data Generator (RDG) → Kafka → Spark ETL Workers → PostgreSQL


# Infraestructure

* Postgresql for the final storage
* Python container that acts as the event generator that feeds the Kafka Queue 
* Kafka Queue partitioned into 3 (can be modify in the future), listens to the python random data generator but can change to whaterver other streams of data
* Manager node for spark 
* Worker_ETL for the ETL process:
 1. Extracts the data from Kafka partition 
 2. Transforms into the desired final scheme (not going too deep into the transformation process since it's a PoC for Spark + Kafka)
 3. Loads into a Postgresql DB on a _stage table


 # To Do's
 
 * Modify the Load so it can store wherever it needs to store the info:
    *  Buckets
    *  Other DBs
    *  Parquets 
    *  Any sort of FIles

* Add monitoring
* Add alerting on data delays or failures

* Improve the Kafka usage, can create topics and more partitions 
* Modify the Extract so it can follow the topics and partitions from the same config document



