import requests
from datetime import datetime

print("TESTE LINKS DIRECIONAMENTO HUB")
print("=" * 50)

# Links do hub principal
hub_url = "https://sstechnologies-cloud.com"
links = {
    "Hub Principal": hub_url,
    "Portfolio": "https://dev-cloud.sstechnologies-cloud.com",
    "AWS Services": "https://aws-services.sstechnologies-cloud.com", 
    "Financas": "https://financaspessoais.sstechnologies-cloud.com",
    "Midiaflow": "https://midiaflow.sstechnologies-cloud.com",
    "Ritech": "https://ritech-fechaduras.sstechnologies-cloud.com",
    "Gestao Trafego": "https://ssgestaodetrafego.sstechnologies-cloud.com",
    "AWS Dashboard": "https://aws-dashboard.sstechnologies-cloud.com"
}

online = 0
total = len(links)

for nome, url in links.items():
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        status = response.status_code
        
        if status == 200:
            print(f"[OK] {nome:15} | {status} | ONLINE")
            online += 1
        elif status in [301, 302, 307, 308]:
            print(f"[>>] {nome:15} | {status} | REDIRECT")
            online += 1
        elif status == 403:
            print(f"[!!] {nome:15} | {status} | BLOQUEADO")
        else:
            print(f"[XX] {nome:15} | {status} | ERRO")
            
    except requests.exceptions.ConnectionError:
        print(f"[NC] {nome:15} | --- | SEM CONEXAO")
    except Exception as e:
        print(f"[ER] {nome:15} | --- | {str(e)[:20]}")

print("=" * 50)
print(f"RESULTADO: {online}/{total} links funcionando")
print(f"Data: {datetime.now().strftime('%H:%M:%S')}")