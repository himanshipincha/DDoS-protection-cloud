from firewall_blocker import block_ip
import time
import os
from collections import Counter

log_file = "logs/sample_log.log"
output_file = "output/alerts.txt"
threshold = 5

blocked_ips = set()

while True:

    # Clear terminal screen for live dashboard
    os.system("clear")

    ips = []

    # Read traffic log
    with open(log_file, "r") as file:
        for line in file:
            ip = line.split()[0]
            ips.append(ip)

    ip_counts = Counter(ips)

    # Security statistics
    total_requests = sum(ip_counts.values())
    unique_ips = len(ip_counts)
    active_attacks = len([ip for ip, count in ip_counts.items() if count > threshold])

    print("========== SECURITY MONITOR ==========")
    print(f"Total Requests: {total_requests}")
    print(f"Unique IPs: {unique_ips}")
    print(f"Blocked IPs: {len(blocked_ips)}")
    print(f"Active Attacks: {active_attacks}")
    print("======================================")

    print("\nTraffic Summary:\n")

    for ip, count in ip_counts.items():
        print(f"{ip} -> {count} requests")

    alerts = []

    print("\nSuspicious IPs:")

    for ip, count in ip_counts.items():
        if count > threshold and ip not in blocked_ips:

            alert = f"Possible attacker detected: {ip}"
            print(alert)

            alerts.append(alert)

            block_ip(ip)

            blocked_ips.add(ip)

    # Save alerts to file
    with open(output_file, "w") as file:
        for alert in alerts:
            file.write(alert + "\n")

    print("\nNext scan in 10 seconds...")

    time.sleep(10)