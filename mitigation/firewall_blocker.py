import subprocess


# Store already blocked IPs
blocked_ips = set()

def block_ip(ip):

    # Prevent blocking same IP again
    if ip in blocked_ips:
        print(f"[INFO] {ip} already blocked")
        return

    # Prevent blocking localhost
    if ip == "127.0.0.1":
        print("[WARNING] Skipping localhost")
        return

    try:
        # Apply iptables rule
        subprocess.run([
            "sudo",
            "iptables",
            "-A",
            "INPUT",
            "-s",
            ip,
            "-j",
            "DROP"
        ], check=True)

        blocked_ips.add(ip)

        print(f"[BLOCKED] {ip} blocked successfully")

        # Save to file (for dashboard later)
        with open("logs/blocked_ips.txt", "a") as f:
            f.write(f"{ip} blocked\n")

    except Exception as e:
        print(f"[ERROR] Could not block {ip}: {e}")

def block_ip(ip):
    try:
        subprocess.run(
            ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            check=True
        )
        print(f"Blocked IP: {ip}")
    except subprocess.CalledProcessError:
        print(f"Failed to block {ip}")
