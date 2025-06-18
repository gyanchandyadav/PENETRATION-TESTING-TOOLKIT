import socket

def scan_ports(host, ports=[21, 22, 23, 80, 443, 8080]):
    print(f"[+] Scanning {host} on ports {ports}")
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"[+] Port {port} is open.")
                    open_ports.append(port)
        except socket.error as err:
            print(f"[!] Socket error: {err}")
    return open_ports
    