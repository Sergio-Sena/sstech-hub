import requests
import time

time.sleep(30)

url = "https://hub.sstechnologies-cloud.com/automacao-em-desenvolvimento.html"
response = requests.get(url)

print(f"URL: {url}")
print(f"Status: {response.status_code}")

if response.status_code == 200:
    print("[OK] Pagina Em Desenvolvimento ONLINE!")
else:
    print(f"[ERRO] Status {response.status_code}")
