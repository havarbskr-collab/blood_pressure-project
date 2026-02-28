# Blood Pressure Monitoring System

---
## Description

Le système génère des observations médicales (système de surveillance de la pression artérielle), les envoie dans Kafka, puis les analyse automatiquement pour détecter les anomalies.

Il permet de :

* Générer des données médicales simulées (patients).
* Envoyer ces données via Kafka.
* Analyser automatiquement les mesures.
* Détecter les anomalies de pression artérielle.
* Séparer les patients normaux des patients à risque.

Il sépare ensuite les patients :
normaux → stockés dans un fichier JSON
anormaux → enregistrés dans un fichier d’alertes

---
## Objectif du projet

Ce projet simule un système complet de surveillance en temps réel.

Il permet de démontrer les points suivants :

- Kafka fonctionne correctement
- Le Producer envoie bien les messages FHIR
- Le Consumer reçoit et traite les messages
- La détection d’anomalies fonctionne
- Les données normales sont sauvegardées en JSON

---

## Architecture du Pipeline

```
generate_fhir.py → producer.py → Kafka → consumer.py → Stockage JSON
```

---

## Prérequis

* Python 3.x
* Docker & Docker Compose
* Kafka (lancé via Docker)

---

## Installation

Cloner le projet :

```bash
git clone https://github.com/havarbskr-collab/blood_pressure-project.git
cd blood_pressure-project
```

---

## Lancement du système

### 1. Démarrer Kafka

```bash
docker-compose up -d
```

---

### 2. Générer les données patients

```bash
python generate_fhir.py
```

---

### 3. Lancer le Producer (envoi vers Kafka)

```bash
python producer.py
```

---

### 4. Lancer le Consumer (analyse des données)

```bash
python consumer.py
```

Le consumer analyse chaque mesure et classe automatiquement les patients.

---

## Fichiers de Résultat

Dans le fichier on aura alors :
- donnees_normales.json, où y'aura les patients avec tension normale
-  alertes_hypertension.json, où y'aura les patients avec anomalies détectées
- anomalies.json, où y'aura le journal technique des anomalies

---

## Logique de Détection

Une alerte est générée si :

* Systolique > 140 mmHg ou < 90 mmHg
* Diastolique > 90 mmHg ou < 60 mmHg

---

## Scripts Principaux
On nom les scripts et leur différents rôles :
- generate_fhir.py, qui va génèrer les données simulées  
- producer.py, qui va envoyer les données vers Kafka 
- consumer.py, qui va analyser et classer les patients

---

## Auteurs

Projet réalisé dans le cadre du Master 1 BIDABI:

* Havar — Génération des données & Kafka
* Karissy — Analyse et traitement
* Palla — Documentation & Data Science

---

