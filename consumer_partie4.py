import json
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from datetime import datetime
# 1. Connexion à Elasticsearch (pour la partie 4 - Traitement)
try:
    es = Elasticsearch(["http://localhost:9200"])
    print("✅ Connecté à Elasticsearch")
except Exception as e:
    print(f"❌ Erreur de connexion Elasticsearch : {e}")

# 2. Configuration du Consumer Kafka
consumer = KafkaConsumer(
    'topic_patients', 
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🚀 Analyse, Archivage et Indexation en cours... (Étape 4 finale)")

for message in consumer:
    fhir_data = message.value
    
    # Extraction des données FHIR [cite: 16]
    patient_id = fhir_data.get('subject', {}).get('reference', 'Inconnu')
    sys = fhir_data['component'][0]['valueQuantity']['value']
    dia = fhir_data['component'][1]['valueQuantity']['value']
    
    # --- LOGIQUE DE TRAITEMENT (SEUILS MÉDICAUX) [cite: 22, 23, 24] ---
    
    # Cas ANORMAL (Hypertension ou Hypotension) [cite: 27]
    if sys > 140 or sys < 90 or dia > 90 or dia < 60:
        anomaly_type = "Hypertension" if (sys > 140 or dia > 90) else "Hypotension"
        print(f"⚠️ ALERTE : {anomaly_type} pour {patient_id} ({sys}/{dia})")
        
        # Action : Indexation dans Elasticsearch [cite: 28, 51, 55]
        doc = {
            "patient_id": patient_id,
            "systolic_pressure": sys,
            "diastolic_pressure": dia,
            "anomaly_type": anomaly_type,
            "status": "ANORMAL"
        }

        es.index(index="patient-anomalies",document={
        'patient_id': doc['patient_id'],
        'systolic_pressure': doc['systolic_pressure'],
        'diastolic_pressure': doc['diastolic_pressure'],
        'anomaly_type': doc['anomaly_type'],
        'timestamp': fhir_data.get('timestamp', datetime.utcnow().isoformat())
     }
    )
        
    # Cas NORMAL [cite: 29]
    else:
        print(f"✅ Pression normale pour {patient_id} ({sys}/{dia})")
        
        # Action : Sauvegarde dans fichier JSON local [cite: 30, 50]
        with open("donnees_normales.json", "a") as f_normal:
            f_normal.write(json.dumps(fhir_data) + "\n")