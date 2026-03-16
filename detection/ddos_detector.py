import time
from collections import defaultdict
from mitigation.firewall_blocker import block_ip

# Nginx access log location
LOG_FILE = "/var/log/nginx/access.log"

# Request threshold to detect attack
THRESHOLD = 100

# Store blocked IPs to avoid blocking multiple times
blocked_ips = set()

def detect_ddos():

    ip_count = defaultdict(int)

    with open(LOG_FILE, "r") as log:

        for line in log:
            ip = line.split()[0]
            ip_count[ip] += 1

    for ip, count in ip_count.items():

        if count > THRESHOLD and ip not in blocked_ips:

            print(f"[ALERT] Suspicious IP detected: {ip} ({count} requests)")

            block_ip(ip)

            blocked_ips.add(ip)


if __name__ == "__main__":

    while True:
        detect_ddos()
        time.sleep(10)
