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
print("TESTANDO TODOS OS PROJETOS HUB")
print("="*60)
print("Aguardando 30 segundos para cache CloudFront...")
time.sleep(30)

online = 0
offline = 0

for projeto in PROJETOS:
    try:
        response = requests.get(projeto['url'], timeout=10, allow_redirects=True)
        status = response.status_code
        
        if status == 200:
            print(f"[OK] {projeto['nome']:20} | {status}")
            online += 1
        elif status == 403:
            print(f"[XX] {projeto['nome']:20} | {status} BLOQUEADO")
            offline += 1
        else:
            print(f"[??] {projeto['nome']:20} | {status}")
            offline += 1
            
    except Exception as e:
        print(f"[ER] {projeto['nome']:20} | ERRO: {str(e)[:30]}")
        offline += 1

print("\n" + "="*60)
print(f"RESULTADO: {online}/{len(PROJETOS)} online")
print("="*60)
