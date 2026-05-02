import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from anomaly import detect_anomaly

st.set_page_config(page_title="Patient Monitoring", layout="wide")

st.title("🏥 Remote Patient Monitoring Dashboard")

# ---------------- SESSION STATE ---------------- #
if "data_log" not in st.session_state:
    st.session_state.data_log = []

# ---------------- SIDEBAR INPUT ---------------- #
st.sidebar.header("Enter Patient Vitals")

heart_rate = st.sidebar.number_input("Heart Rate (bpm)", 30, 200, 75)
spo2 = st.sidebar.number_input("SpO2 (%)", 70, 100, 98)
temperature = st.sidebar.number_input("Temperature (°C)", 30.0, 45.0, 36.8)

if st.sidebar.button("Add Reading"):
    vitals = {
        "heart_rate": heart_rate,
        "spo2": spo2,
        "temperature": temperature
    }

    status = detect_anomaly(vitals)
    vitals["status"] = status

    st.session_state.data_log.append(vitals)

# ---------------- DATAFRAME ---------------- #
if st.session_state.data_log:
    df = pd.DataFrame(st.session_state.data_log)

    # ---------------- METRICS ---------------- #
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Readings", len(df))
    col2.metric("Anomalies", (df["status"] == "Anomaly").sum())
    col3.metric("Normal", (df["status"] == "Normal").sum())

    st.divider()

    # ---------------- LATEST STATUS ---------------- #
    latest = df.iloc[-1]

    st.subheader("Latest Reading")
    st.write(latest)

    if latest["status"] == "Anomaly":
        st.error("⚠️ Critical Condition Detected")
    else:
        st.success("✅ Patient Stable")

    st.divider()

    # ---------------- CHARTS ---------------- #
    st.subheader("Vitals Trend")

    fig, ax = plt.subplots()
    ax.plot(df["heart_rate"], label="Heart Rate")
    ax.plot(df["spo2"], label="SpO2")
    ax.plot(df["temperature"], label="Temperature")
    ax.legend()

    st.pyplot(fig)

    # ---------------- DATA TABLE ---------------- #
    st.subheader("Full Monitoring Data")

    def highlight_anomaly(row):
        return ["background-color: #ffcccc" if row.status == "Anomaly" else "" for _ in row]

    st.dataframe(df.style.apply(highlight_anomaly, axis=1))

else:
    st.info("Enter patient vitals from the sidebar to begin monitoring.")