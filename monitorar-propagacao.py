import requests
import time

PROJETOS = [
    {"nome": "AWS Services", "url": "https://aws-services.sstechnologies-cloud.com"},
    {"nome": "Ritech", "url": "https://ritech-fechaduras-digitais.sstechnologies-cloud.com"},
    {"nome": "AWS Cert", "url": "https://aws-certification-platform.sstechnologies-cloud.com"}
]

print("="*60)
print("MONITORANDO PROPAGACAO CLOUDFRONT")
print("="*60)
print("Verificando a cada 60 segundos...\n")

tentativa = 1
max_tentativas = 10

while tentativa <= max_tentativas:
    print(f"\n[Tentativa {tentativa}/{max_tentativas}] - {time.strftime('%H:%M:%S')}")
    
    todos_online = True
    
    for projeto in PROJETOS:
        try:
            response = requests.get(projeto['url'], timeout=10)
            
            if response.status_code == 200:
                print(f"  [OK] {projeto['nome']:20} | 200 ONLINE")
            else:
                print(f"  [XX] {projeto['nome']:20} | {response.status_code}")
                todos_online = False
                
        except Exception as e:
            print(f"  [ER] {projeto['nome']:20} | ERRO")
            todos_online = False
    
    if todos_online:
        print("\n" + "="*60)
        print("TODOS OS PROJETOS ONLINE!")
        print("="*60)
        break
    
    if tentativa < max_tentativas:
        print("\nAguardando 60 segundos...")
        time.sleep(60)
    
    tentativa += 1

if not todos_online:
    print("\n" + "="*60)
    print("Tempo limite atingido. Alguns projetos ainda offline.")
    print("="*60)
