import requests
import time

PROJETOS = [
    {"nome": "Hub Principal", "url": "https://hub.sstechnologies-cloud.com"},
    {"nome": "Portfolio", "url": "https://dev-cloud.sstechnologies-cloud.com/"},
    {"nome": "AWS Services", "url": "https://aws-services.sstechnologies-cloud.com"},
    {"nome": "Financas", "url": "https://financaspessoais.sstechnologies-cloud.com"},
    {"nome": "Midiaflow", "url": "https://midiaflow.sstechnologies-cloud.com/"},
    {"nome": "Ritech", "url": "https://ritech-fechaduras-digitais.sstechnologies-cloud.com"},
    {"nome": "Gestao Trafego", "url": "https://sstrafegopago.sstechnologies-cloud.com"},
    {"nome": "AWS Cert", "url": "https://aws-certification-platform.sstechnologies-cloud.com"}
]

print("="*60)
print("VERIFICANDO STATUS 200 - TODOS OS PROJETOS HUB")
print("="*60)

bloqueados = []

for projeto in PROJETOS:
    try:
        response = requests.get(projeto['url'], timeout=10, allow_redirects=True)
        status = response.status_code
        
        if status == 200:
            print(f"[OK] {projeto['nome']:20} | 200")
        else:
            print(f"[XX] {projeto['nome']:20} | {status}")
            if status == 403:
                bloqueados.append(projeto)
            
    except Exception as e:
        print(f"[ER] {projeto['nome']:20} | ERRO")
        bloqueados.append(projeto)

print("\n" + "="*60)
if bloqueados:
    print(f"PROJETOS BLOQUEADOS: {len(bloqueados)}")
    for p in bloqueados:
        print(f"  - {p['nome']}: {p['url']}")
else:
    print("TODOS OS PROJETOS ONLINE!")
print("="*60)
