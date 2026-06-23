# SOCShield - AI Powered Security Operations Center Dashboard

## Overview

SOCShield is an AI-powered Security Operations Center (SOC) Dashboard developed using Python and Streamlit for cybersecurity threat monitoring, investigation, and incident reporting.

The system processes cybersecurity log data and provides threat analytics, anomaly detection, risk scoring, alert management, network visualization, and investigation capabilities through an interactive dashboard.

---

## Features

### Threat Analytics

* Threat distribution analysis
* Malicious event monitoring
* Suspicious activity tracking

### IP Intelligence

* Top source IP analysis
* Top destination IP analysis
* High-risk IP identification

### Protocol Analysis

* HTTP
* HTTPS
* TCP
* UDP
* SSH
* FTP
* ICMP monitoring

### Threat Detection

* Risk scoring engine
* Anomaly detection
* Brute force attack detection

### Security Operations

* Investigation panel
* Security alerts
* Alert history management
* Analyst notes

### Visualization

* Attack network graph
* Threat trend analysis
* Interactive dashboard metrics

### Reporting

* Incident report generation
* PDF export

---

## Technology Stack

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* SQLite
* NetworkX
* Matplotlib
* ReportLab

---

## Dataset

Cybersecurity Threat Detection Logs Dataset

Dataset Size:

* Original Dataset: ~6,000,000 records
* Dashboard Working Dataset: ~100,000 records

---

## Project Structure

socshield-ai-soc-dashboard/

* app.py
* requirements.txt

data/

* cybersecurity_threat_detection_logs.csv

modules/

* log_loader.py
* threat_statistics.py
* ip_analysis.py
* protocol_analysis.py
* threat_scoring.py
* anomaly_detection.py
* investigation.py
* brute_force_detector.py
* network_visualization.py
* alert_engine.py
* threat_trends.py
* analyst_notes.py
* report_generator.py

database/

* alerts.db
* db_manager.py

reports/

* socshield_report.pdf

---

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Future Improvements

* Threat intelligence integration
* Real-time alert streaming
* SIEM integration
* User authentication
* Advanced attack correlation
* Cloud deployment

---

## Author

Dharshini
PES University
Cybersecurity & AI Forensics Internship Project

## Dashboard Screenshots

### Dashboard Overview

![Dashboard Overview](screenshots/dashboard_overview.png)

### High-Risk IP Analysis

![High Risk IP Analysis](screenshots/high_risk_ips.png)

### Investigation Panel

![Investigation Panel](screenshots/investigation_panel.png)

### Anomaly Detection

![Anomaly Detection](screenshots/anomaly_detection.png)

### Brute Force Detection

![Brute Force Detection](screenshots/bruteforce_detection.png)

### Security Alerts

![Security Alerts](screenshots/security_alerts.png)

### Alert History

![Alert History](screenshots/alert_history.png)

### Network Visualization

![Network Graph](screenshots/network_graph.png)

### Threat Trends

![Threat Trends](screenshots/threat_trends.png)

### Analyst Notes

![Analyst Notes](screenshots/analyst_notes.png)

### Incident Report Generator

![Incident Report Generator](screenshots/incident_report_generator.png)


