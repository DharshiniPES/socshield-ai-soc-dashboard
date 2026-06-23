# 🛡️ SOCShield - AI-Powered Security Operations Center Dashboard

## Overview

SOCShield is an AI-powered Security Operations Center (SOC) dashboard developed using Python and Streamlit. The platform analyzes cybersecurity logs, detects threats, identifies suspicious activity, generates security alerts, and assists analysts during investigations.

The system integrates threat analytics, anomaly detection, risk scoring, network visualization, incident reporting, and alert management into a single dashboard.

---

## Key Features

### Threat Analytics

* Threat distribution analysis
* Malicious and suspicious event monitoring
* Threat trend visualization

### Risk Assessment

* High-risk IP identification
* IP risk scoring engine
* Threat severity classification

### Detection Modules

* Anomaly detection
* Brute force attack detection
* Security alert generation

### Investigation Tools

* Investigation panel
* IP activity analysis
* Protocol analysis
* Destination analysis
* Analyst notes

### Visualization

* Network attack graph
* Threat trend analysis
* Interactive dashboard metrics

### Reporting

* Incident report generation
* PDF report export
* Alert history storage using SQLite

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

## Project Architecture

Cybersecurity Logs Dataset
↓
Log Loader
↓
Threat Analysis Engine
↓
SOCShield Dashboard
↓
Alerts + Investigation + Reporting
↓
SQLite Storage + PDF Reports

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

screenshots/

---

## Dashboard Screenshots

### Dashboard Overview

![Dashboard Overview](screenshots/dashboard_overview.png)

### High-Risk IP Analysis

![High Risk IP Analysis](screenshots/high_risk_ips.png)

### Investigation Panel

![Investigation Panel](screenshots/investigation_panel.png)

### Security Alerts

![Security Alerts](screenshots/security_alerts.png)

### Threat Trends

![Threat Trends](screenshots/threat_trends.png)

### Analyst Notes

![Analyst Notes](screenshots/analyst_notes.png)

### Network Graph

![Network Graph](screenshots/network_graph.png)

---

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

* Real-time threat monitoring
* Threat intelligence integration
* SIEM integration
* Cloud deployment
* Advanced attack correlation

## Author

Dharshini
PES University
Cybersecurity & AI Forensics Internship Project





