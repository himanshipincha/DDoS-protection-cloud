import subprocess

def block_ip(ip):
    try:
        subprocess.run(
            ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            check=True
        )
        print(f"Blocked IP: {ip}")
    except subprocess.CalledProcessError:
        print(f"Failed to block {ip}")