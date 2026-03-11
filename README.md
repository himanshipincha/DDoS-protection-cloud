# DDoS-protection-cloud

Automated DDoS detection and mitigation system for cloud-hosted web applications using Nginx log analysis, Python detection scripts, iptables firewall protection, and a Flask monitoring dashboard.

## Project Overview
This project demonstrates a cloud-based security system that detects abnormal traffic patterns targeting a web server and automatically mitigates attacks by blocking malicious IP addresses.

## Components

- **Nginx Web Server**
  - Hosts the web application
  - Generates access logs for traffic monitoring

- **Python Detection Engine**
  - Analyzes Nginx access logs
  - Detects suspicious traffic patterns and request spikes

- **iptables Mitigation Module**
  - Automatically blocks malicious IP addresses
  - Prevents further attack traffic from reaching the server

- **Flask Monitoring Dashboard**
  - Displays blocked IP addresses
  - Provides a real-time monitoring interface for system status

## Architecture

Attacker Traffic  
↓  
Nginx Web Server  
↓  
Access Logs  
↓  
Python Detection Engine  
↓  
iptables Firewall Blocking  
↓  
Flask Monitoring Dashboard
