import time
import random

log_file = "logs/sample_log.log"

attacker_ip = "192.168.1.100"

normal_ips = [
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4"
]

print("Starting traffic simulation...\n")

while True:

    with open(log_file, "a") as file:

        # normal traffic
        ip = random.choice(normal_ips)
        file.write(f"{ip} GET /home\n")

        # attack traffic
        for _ in range(10):
            file.write(f"{attacker_ip} GET /login\n")

    print("Traffic generated...")

    time.sleep(3)