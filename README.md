# Blood Pressure Monitoring System

## Description

Ce projet simule un système de surveillance de la pression artérielle en temps réel.

Il permet de :

* Générer des données médicales simulées (patients).
* Envoyer ces données via Kafka.
* Analyser automatiquement les mesures.
* Détecter les anomalies de pression artérielle.
* Séparer les patients normaux des patients à risque.

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

Après exécution, les fichiers suivants sont générés :

donnees_normales.json : contient les patients avec une tension normale.
alertes_hypertension.json : contient les patients présentant des anomalies détectées.
anomalies.json : journal technique des anomalies identifiées.

---

## Logique de Détection

Une alerte est générée si :

* Systolique > 140 mmHg ou < 90 mmHg
* Diastolique > 90 mmHg ou < 60 mmHg

---

## Scripts Principaux

- generate_fhir.py -> Rôle : Génère les données simulées
- producer.py      -> Rôle : Envoie les données vers Kafka
- consumer.py      -> Rôle : Analyse les mesures et classe les patients

---

## Auteurs

Projet réalisé dans le cadre du Master 1 BIDABI:

* Havar — Génération des données & Kafka
* Karissy — Analyse et traitement
* Palla — Documentation & Data Science

---


