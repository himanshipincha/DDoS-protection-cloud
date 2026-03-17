# Nginx Server Setup (Local Ubuntu Environment)

## Environment Details
- OS: Ubuntu 22.04.5 LTS (WSL)
- Web Server: Nginx
- Access Method: http://localhost

---

## Installation Steps

### Update System
sudo apt update

### Install Nginx
sudo apt install nginx -y

---

## Starting Nginx (WSL)

sudo service nginx start

---

## Verify Server

Open browser and visit:

http://localhost

Expected output:
"Welcome to nginx!" page confirms server is running.

---

## Log File Location

Nginx stores logs at:

/var/log/nginx/access.log

---

## Monitoring Logs

To monitor real-time traffic:

tail -f /var/log/nginx/access.log

---

## Observations

- Each browser refresh generates a new log entry
- Requests originate from 127.0.0.1 (local machine)
- Status codes:
  - 200 → successful request
  - 304 → cached response

---

## Role in DDoS Detection System

- Nginx acts as the entry point for all incoming traffic
- Access logs are used by the detection script to analyze traffic patterns
- Suspicious IPs identified from logs will be passed to the mitigation module (iptables)

---

## Architecture Flow

Client Request
↓
Nginx Server
↓
Access Logs (/var/log/nginx/access.log)
↓
Detection Engine (Python)
↓
Mitigation (iptables)
↓
Dashboard (Flask)



