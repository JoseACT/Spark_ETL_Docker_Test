import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

names = ["Alice", "Bob", "Charlie", "Diana"]

print("Starting random data generation...")


sources_names = [f"source{x}" for x in range(1, 101)]

sources_ids_sequences = { x : 0 for x in range(1, 101) } # 100 sources

random_unused_fields = ['cashier', 'weekday','comment','country']
while True:
    # Generate random data
    # data to genereate are: transactions, will have id, name, value, createdAt, typeTransaction, soruceId, sourceName
    # keep sequencial ids for each sourceId
    # and sourceName, but random for the rest of the data
    source_id =  random.randint(1, 100)
    
    data = {
        "id": sources_ids_sequences[source_id] + 1,
        "clientId": random.randint(1, 100000),
        "value": random.uniform(10.0, 100.0),
        "createdAt": datetime.now().isoformat(),
        "typeTransaction": random.choice(["charge", "refund", "transfer"]),
        "sourceId": source_id,
        "currency": random.choice(["USD", "EUR", "GBP"]),
        "sourceName": random.choice(sources_names),
    }
    # add random unused fields randomly
    for field in random_unused_fields:
        if random.random() > 0.5: # 50% chance to add the field
            data[field] = random.choice(["value1", "value2", "value3"])

    sources_ids_sequences[source_id] += 1
    # TODO add topic and partition from the environment variables
    # Kafka will contain 3 partitions assing at random 
    partion_id = random.randint(0, 2)
    producer.send("raw-events", value=data, partition=partion_id)
    print("Sent:", data)
    time.sleep(1)
