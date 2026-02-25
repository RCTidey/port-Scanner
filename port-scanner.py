import socket

PORTS_TO_SCAN = {
    21 : "FTP",
    22 : "SSH",
    23 : "Telnet",
    80 : "HTTP",
    443 : "HTTPS",
    3389 : "RDP"
}

for port in PORTS_TO_SCAN:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    status = s.connect_ex(("127.0.0.1", port))

    if status == 0:
        print(f"{port} {PORTS_TO_SCAN[port]} is open")

    else:
        print(f"{port} {PORTS_TO_SCAN[port]} is closed")
    s.close()