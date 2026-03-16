# Ubuntu Server Setup

## 1. AWS EC2 Instance Creation
An AWS EC2 instance was created using Ubuntu 22.04.

## 2. Security Group Configuration
The following ports were opened:

22 - SSH  
80 - HTTP

## 3. Install Nginx

sudo apt update
sudo apt install nginx

## 4. Verify Nginx Installation
Open the EC2 public IP in browser.

Example:
http://<EC2_PUBLIC_IP>

## 5. Nginx Log File Location

/var/log/nginx/access.log

## 6. Role in Project

The Python detection script monitors this log file.
If an IP generates too many requests, it is blocked using firewall rules.



