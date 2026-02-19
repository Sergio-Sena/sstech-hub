import requests
import time

print("TESTE DETALHADO HUB PRINCIPAL")
print("=" * 40)

urls_teste = [
    "https://sstechnologies-cloud.com",
    "http://sstechnologies-cloud.com", 
    "https://www.sstechnologies-cloud.com",
    "https://sstech-hub.sstechnologies-cloud.com"
]

for url in urls_teste:
    try:
        print(f"Testando: {url}")
        response = requests.get(url, timeout=15, allow_redirects=True)
        print(f"  Status: {response.status_code}")
        print(f"  Final URL: {response.url}")
        if response.status_code == 200:
            print(f"  ✓ FUNCIONANDO")
        print()
    except Exception as e:
        print(f"  ✗ ERRO: {str(e)[:50]}")
        print()

# Teste direto dos projetos online
print("CONFIRMACAO PROJETOS ONLINE:")
print("-" * 30)

projetos_online = [
    "https://dev-cloud.sstechnologies-cloud.com",
    "https://aws-services.sstechnologies-cloud.com", 
    "https://financaspessoais.sstechnologies-cloud.com",
    "https://midiaflow.sstechnologies-cloud.com"
]

for url in projetos_online:
    try:
        response = requests.get(url, timeout=10)
        nome = url.split('//')[1].split('.')[0]
        if response.status_code == 200:
            print(f"✓ {nome:12} | ONLINE")
        else:
            print(f"✗ {nome:12} | {response.status_code}")
    except:
        print(f"✗ {nome:12} | ERRO")