from kafka import KafkaProducer
import json
import time
from generate_fhir import generate_fhir

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
)

while True:
    data = generate_fhir()
    producer.send('topic', value=data)
    print("Message envoyé à Kafka")
    time.sleep(5)