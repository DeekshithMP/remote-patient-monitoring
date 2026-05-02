import streamlit as st
import pandas as pd
from simulator import generate_vitals, generate_abnormal_vitals
from anomaly import detect_anomaly
import time

st.title("🏥 Remote Patient Monitoring")

data_log = []

run = st.checkbox("Start Monitoring")

while run:
    if st.button("Generate Abnormal Data"):
        vitals = generate_abnormal_vitals()
    else:
        vitals = generate_vitals()

    status = detect_anomaly(vitals)

    vitals["status"] = status
    data_log.append(vitals)

    df = pd.DataFrame(data_log)

    st.write("### Latest Vitals")
    st.write(vitals)

    st.write("### Monitoring Data")
    st.dataframe(df)

    if status == "Anomaly":
        st.error("⚠️ Anomaly Detected!")
    else:
        st.success("✅ Normal")

    time.sleep(2)
    st.rerun()
