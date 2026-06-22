
import streamlit as st

from modules.log_loader import LogLoader
from modules.threat_statistics import ThreatStatistics
from modules.ip_analysis import IPAnalysis
from modules.protocol_analysis import ProtocolAnalysis
from modules.threat_scoring import ThreatScoring
from modules.anomaly_detection import AnomalyDetection

st.set_page_config(
    page_title="SOCShield",
    layout="wide"
)

st.title("🛡️ SOCShield Dashboard")

# Load Data
loader = LogLoader(
    "data/cybersecurity_threat_detection_logs.csv"
)

logs = loader.load_logs()

# Analysis Modules
stats = ThreatStatistics(logs)
ip_analysis = IPAnalysis(logs)
protocol_analysis = ProtocolAnalysis(logs)
threat_scoring = ThreatScoring(logs)
anomaly_detector = AnomalyDetection(logs)

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Events",
    f"{len(logs):,}"
)

col2.metric(
    "Malicious Events",
    f"{len(logs[logs['threat_label'] == 'malicious']):,}"
)

col3.metric(
    "Suspicious Events",
    f"{len(logs[logs['threat_label'] == 'suspicious']):,}"
)

# Threat Distribution
st.subheader("Threat Distribution")
st.bar_chart(
    stats.threat_distribution()
)

# Top Source IPs
st.subheader("Top Source IPs")
st.bar_chart(
    ip_analysis.top_source_ips()
)

# Top Destination IPs
st.subheader("Top Targeted Destination IPs")
st.bar_chart(
    ip_analysis.top_destination_ips()
)

# Protocol Distribution
st.subheader("Protocol Distribution")
st.bar_chart(
    protocol_analysis.protocol_distribution()
)

# High Risk IPs
st.subheader("Top High-Risk IPs")

risk_data = threat_scoring.calculate_ip_risk()

for ip, score in risk_data:
    st.write(
        f"🚨 {ip} — Risk Score: {score}"
    )

# Anomaly Detection
st.subheader("🚨 Detected Anomalies")

anomalies = anomaly_detector.detect_anomalies()

st.write(
    "Anomaly count:",
    len(anomalies)
)

st.dataframe(
    anomalies[
        [
            "source_ip",
            "dest_ip",
            "bytes_transferred",
            "protocol",
            "threat_label"
        ]
    ]
)

