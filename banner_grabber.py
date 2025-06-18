import socket

def grab_banner(host, port):
    print(f"[+] Grabbing banner from {host}:{port}")
    try:
        with socket.socket() as s:
            s.connect((host, port))
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024)
            print("[+] Banner received:")
            print(banner.decode(errors="ignore"))
    except Exception as e:
        print(f"[!] Error: {e}")
