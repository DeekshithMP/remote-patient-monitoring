from sklearn.ensemble import IsolationForest
import numpy as np

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

def detect_anomaly(vitals):
    values = [[
        vitals["heart_rate"],
        vitals["spo2"],
        vitals["temperature"]
    ]]

    prediction = model.predict(values)

    return "Anomaly" if prediction[0] == -1 else "Normal"
