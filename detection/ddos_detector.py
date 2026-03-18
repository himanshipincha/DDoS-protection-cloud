
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from collections import defaultdict
from mitigation.firewall_blocker import block_ip


LOG_FILE = "/var/log/nginx/access.log"
THRESHOLD = 50  # lower for testing

blocked_ips = set()
last_position = 0  # track file position


def detect_ddos():
    global last_position

# Nginx access log location
LOG_FILE = "/var/log/nginx/access.log"

# Request threshold to detect attack
THRESHOLD = 100

# Store blocked IPs to avoid blocking multiple times
blocked_ips = set()

def detect_ddos():

    ip_count = defaultdict(int)

    with open(LOG_FILE, "r") as log:

        log.seek(last_position)  # read only new logs

        for line in log:
            ip = line.split()[0]

            # skip local IP
            #if ip == "127.0.0.1":
             #   continue

            ip_count[ip] += 1

        last_position = log.tell()



        for line in log:
            ip = line.split()[0]
            ip_count[ip] += 1

    for ip, count in ip_count.items():

        if count > THRESHOLD and ip not in blocked_ips:

            print(f"[ALERT] Suspicious IP detected: {ip} ({count} requests)")

            block_ip(ip)

            blocked_ips.add(ip)


            # log to file
            with open("logs/blocked_ips.txt", "a") as f:
                f.write(f"{ip} blocked ({count} requests)\n")



if __name__ == "__main__":

    while True:
        detect_ddos()
        time.sleep(10)
