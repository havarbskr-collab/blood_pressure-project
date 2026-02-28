from kafka import KafkaProducer
import json
import time
from generate_fhir import generate_fhir

# Création du producer Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

topic = "test"

print("Envoi en continu des patients...")

while True:
    data = generate_fhir()
    producer.send(topic, value=data)
    print("Message envoyé à Kafka")
    time.sleep(5)

print("Envoi terminé")

producer.flush()
producer.close()