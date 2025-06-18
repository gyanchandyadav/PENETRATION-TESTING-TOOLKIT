import requests

def dir_brute_force(url, wordlist_path):
    print(f"[+] Starting directory brute force on: {url}")
    with open(wordlist_path, "r") as f:
        paths = f.read().splitlines()
    
    for path in paths:
        full_url = f"{url.rstrip('/')}/{path}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"[+] Found directory: {full_url}")
        except requests.RequestException:
            continue
