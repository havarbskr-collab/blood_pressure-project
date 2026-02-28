from faker import Faker
from fhir.resources.observation import Observation
import random
from datetime import datetime, timezone

fake = Faker()

def generate_fhir():

    # Générer données patient
    patient_id = fake.uuid4()
    systolic = random.randint(80, 180)
    diastolic = random.randint(50, 120)

    observation_data = {
        "resourceType": "Observation",
        "status": "final",
        "code": {
            "text": "Blood Pressure"
        },
        "subject": {
            "reference": f"Patient/{patient_id}"
        },
        "effectiveDateTime": datetime.now(timezone.utc).isoformat(),
        "component": [
            {
                "code": {"text": "Systolic Blood Pressure"},
                "valueQuantity": {
                    "value": systolic,
                    "unit": "mmHg"
                }
            },
            {
                "code": {"text": "Diastolic Blood Pressure"},
                "valueQuantity": {
                    "value": diastolic,
                    "unit": "mmHg"
                }
            }
        ]
    }

    observation = Observation(**observation_data)

    return observation.model_dump(mode="json")