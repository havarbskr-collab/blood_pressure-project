from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer démarré...")

for message in consumer:
    data = message.value
    
    print("\nMessage reçu :")
    print(data)
    
    # Exemple détection simple
    systolic = data["component"][0]["valueQuantity"]["value"]
    diastolic = data["component"][1]["valueQuantity"]["value"]

    if systolic > 140 or diastolic > 90:
        print("⚠️ Hypertension détectée")
    elif systolic < 90 or diastolic < 60:
        print("⚠️ Hypotension détectée")
    else:
        print("Pression normale")

# Détection avec variable anomaly
if systolic > 140 or diastolic > 90:
    anomaly = "Hypertension"
    print("⚠️ Hypertension détectée")
elif systolic < 90 or diastolic < 60:
    anomaly = "Hypotension"
    print("⚠️ Hypotension détectée")
else:
    anomaly = "Normal"
    print("Pression normale")

# =========================
# Sauvegarde des normaux
# =========================

if anomaly == "Normal":
    with open("normal_data.json", "a") as f:
        f.write(json.dumps(data) + "\n")

