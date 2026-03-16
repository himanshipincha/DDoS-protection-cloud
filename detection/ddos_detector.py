from mitigation.firewall_blocker import block_ip
from collections import Counter
import time
import os

# Log file location
log_file = "logs/sample_log.log"

# Attack detection threshold
threshold = 5

# Keep track of blocked IPs
blocked_ips = set()

while True:

    # Clear terminal screen
    os.system("clear")

    ips = []

    # Read log file
    with open(log_file, "r") as file:
        for line in file:
            ip = line.split()[0]
            ips.append(ip)

    # Count requests from each IP
    ip_counts = Counter(ips)

    print("========== SECURITY MONITOR ==========")

    for ip, count in ip_counts.items():
        print(f"{ip} -> {count} requests")

    print("======================================")

    print("\nSuspicious IPs:")

    # Detect attackers
    for ip, count in ip_counts.items():

        if count > threshold and ip not in blocked_ips:

            print(f"Possible attacker detected: {ip}")

            # Call mitigation module
            block_ip(ip)

            blocked_ips.add(ip)

    print("\nNext scan in 10 seconds...")

    time.sleep(10)
