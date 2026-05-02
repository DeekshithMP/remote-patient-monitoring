import random

def generate_vitals():
    return {
        "heart_rate": random.randint(60, 100),
        "spo2": random.randint(95, 100),
        "temperature": round(random.uniform(36.5, 37.5), 1)
    }

def generate_abnormal_vitals():
    return {
        "heart_rate": random.randint(40, 140),
        "spo2": random.randint(85, 100),
        "temperature": round(random.uniform(35, 40), 1)
    }
