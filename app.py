
import streamlit as st
from modules.investigation import Investigation
from modules.log_loader import LogLoader
from modules.threat_statistics import ThreatStatistics
from modules.ip_analysis import IPAnalysis
from modules.protocol_analysis import ProtocolAnalysis
from modules.threat_scoring import ThreatScoring
from modules.anomaly_detection import AnomalyDetection
from modules.network_visualization import NetworkVisualization
from modules.brute_force_detector import BruteForceDetector
from modules.alert_engine import AlertEngine
from database.db_manager import DBManager
from modules.report_generator import ReportGenerator
from datetime import datetime
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
network_visualizer = NetworkVisualization(logs)
bruteforce_detector = BruteForceDetector(logs)
threat_scoring = ThreatScoring(logs)
investigator = Investigation(logs)
alert_engine = AlertEngine(logs)
db = DBManager()
report_generator = ReportGenerator()
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
high_risk_ips = [
    ip for ip, score in risk_data
]

selected_ip = st.sidebar.selectbox(
    "Investigate High-Risk IP",
    high_risk_ips
)
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
st.subheader("🔍 Investigation Panel")

records = investigator.investigate_ip(
    selected_ip
)

st.metric(
    "Events From Selected IP",
    len(records)
)

st.write("Protocols Used")

st.bar_chart(
    investigator.get_protocols(
        selected_ip
    )
)

st.write("Top Targeted Destinations")

st.bar_chart(
    investigator.get_destinations(
        selected_ip
    )
)

st.write("Recent Activity")

st.dataframe(
    records.head(20)
)
st.metric(
    "Suspicious Events",
    len(
        records[
            records["threat_label"] != "benign"
        ]
    )
)
st.subheader("🌐 Attack Network Graph")

fig = network_visualizer.draw_graph(
    limit=50
)

st.pyplot(fig)
st.subheader("🔐 Potential Brute Force Attacks")

attacks = bruteforce_detector.detect_bruteforce()

st.dataframe(
    attacks.reset_index()
)

st.subheader("🚨 Security Alerts")

alerts = alert_engine.generate_alerts()

for alert in alerts:

    db.insert_alert(
        alert["ip"],
        alert["severity"],
        alert["protocol"],
        alert["action"]
    )

    message = (
        f"{alert['severity']} RISK | "
        f"{alert['ip']} | "
        f"{alert['protocol']} | "
        f"{alert['action']}"
    )

    if alert["severity"] == "HIGH":

        st.error(message)

    else:

        st.warning(message)
st.subheader("📜 Alert History")

history = db.get_alerts()

st.dataframe(history)

# ----------------------------
# INCIDENT REPORT GENERATOR
# ----------------------------


st.subheader("📄 Incident Report Generator")

if st.button(
    "Generate Incident Report"
):

    total_events = len(logs)

    malicious_events = len(
        logs[
            logs["threat_label"] == "malicious"
        ]
    )

    suspicious_events = len(
        logs[
            logs["threat_label"] == "suspicious"
        ]
    )

    anomaly_count = len(anomalies)

    brute_force_count = len(attacks)

    top_risk_ips = [
        ip
        for ip, score in risk_data[:5]
    ]

    report_id = "SOC-2026-001"

    generated_time = datetime.now().strftime(
        "%d-%b-%Y %H:%M"
    )

    report = f"""
SOCSHIELD INCIDENT REPORT

Report ID: {report_id}

Generated On: {generated_time}


EXECUTIVE SUMMARY

Total Security Events: {total_events:,}

Malicious Events: {malicious_events:,}

Suspicious Events: {suspicious_events:,}

Detected Anomalies: {anomaly_count:,}

Potential Brute Force Sources: {brute_force_count:,}


TOP HIGH-RISK IPS

{chr(10).join(top_risk_ips)}


SECURITY RECOMMENDATIONS

1. Investigate high-risk IPs immediately.

2. Review suspicious network activity.

3. Monitor blocked authentication attempts.

4. Continue anomaly monitoring.

5. Review recurring alerts in alert history.
"""

    st.text(report)

    filename = report_generator.generate_report(
        "reports/socshield_report.pdf",
        report
    )

    with open(
        filename,
        "rb"
    ) as pdf_file:

        st.download_button(
            label="📥 Download PDF Report",
            data=pdf_file,
            file_name="socshield_report.pdf",
            mime="application/pdf"
        )
