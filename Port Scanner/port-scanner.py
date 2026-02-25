import os
import socket
import platform

PORTS_TO_SCAN = {
    21 : "FTP",
    22 : "SSH",
    23 : "Telnet",
    80 : "HTTP",
    443 : "HTTPS",
    3389 : "RDP"
}

IP_TO_SCAN = input("Enter the IP address to scan: ")
print(f"Scanning {IP_TO_SCAN} for open ports...")

def is_reachable(ip):
    if os.name == "nt":
        ping_cmd = f"ping -n 1 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 {ip} > /dev/null 2>&1"

    response = os.system(ping_cmd)
    if response == 0:
        print(f"{ip} is reachable. Starting port scan...")
    else:
        print(f"{ip} is not reachable. Exiting.")
        exit()


def main():
    is_reachable(IP_TO_SCAN)
    for port in PORTS_TO_SCAN:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        status = s.connect_ex((IP_TO_SCAN, port))

        if status == 0:
            print(f"{port} {PORTS_TO_SCAN[port]} is open")

        else:
            print(f"{port} {PORTS_TO_SCAN[port]} is closed")
        s.close()


if __name__ == "__main__":
    main()