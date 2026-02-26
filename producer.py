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

print("Envoi de 5 patients...")

# Envoi de seulement 5 patients
for i in range(5):
    data = generate_fhir()
    producer.send(topic, value=data)
    print(f"Patient {i+1} envoyé")
    time.sleep(2)

print("Envoi terminé")

producer.flush()
producer.close()