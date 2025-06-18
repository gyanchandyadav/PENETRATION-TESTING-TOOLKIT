import requests

def enumerate_subdomains(domain, wordlist_path):
    print(f"[+] Enumerating subdomains for: {domain}")
    with open(wordlist_path, "r") as f:
        subdomains = f.read().splitlines()
    
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code < 400:
                print(f"[+] Found subdomain: {url}")
        except requests.RequestException:
            pass
