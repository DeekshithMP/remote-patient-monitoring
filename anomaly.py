from sklearn.ensemble import IsolationForest
import numpy as np

# ---------------- TRAIN MODEL ---------------- #
def train_model():
    data = []
    for _ in range(100):
        hr = np.random.randint(60, 100)
        spo2 = np.random.randint(95, 100)
        temp = np.random.uniform(36.5, 37.5)
        data.append([hr, spo2, temp])

    model = IsolationForest(contamination=0.1)
    model.fit(data)
    return model

model = train_model()

# ---------------- RULE-BASED SYSTEM ---------------- #
def rule_based_check(vitals):
    hr = vitals["heart_rate"]
    spo2 = vitals["spo2"]
    temp = vitals["temperature"]

    if hr < 50 or hr > 120:
        return "Anomaly (HR)"
    if spo2 < 92:
        return "Anomaly (SpO2)"
    if temp < 35 or temp > 38:
        return "Anomaly (Temp)"

    return "Normal"

# ---------------- HYBRID DETECTION ---------------- #
def detect_anomaly(vitals):
    # Rule-based result
    rule_result = rule_based_check(vitals)

    # ML prediction
    values = [[
        vitals["heart_rate"],
        vitals["spo2"],
        vitals["temperature"]
    ]]
    ml_pred = model.predict(values)
    ml_result = "Anomaly" if ml_pred[0] == -1 else "Normal"

    # ---------------- FINAL DECISION ---------------- #
    if "Anomaly" in rule_result:
        return rule_result  # prioritize rules

    if ml_result == "Anomaly":
        return "Anomaly (ML)"

    return "Normal"