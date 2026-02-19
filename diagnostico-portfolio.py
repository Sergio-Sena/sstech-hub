import requests

print("="*60)
print("DIAGNOSTICO - PORTFOLIO")
print("="*60)

# Testar acesso
url = "https://dev-cloud.sstechnologies-cloud.com/"
print(f"\n[1] Testando: {url}")

try:
    response = requests.get(url, timeout=10)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 403:
        print("[ERRO] Acesso negado (403 Forbidden)")
        print("Causa: Bucket policy ou OAC incorreto")
    elif response.status_code == 200:
        print("[OK] Acesso permitido")
    else:
        print(f"[AVISO] Status inesperado: {response.status_code}")
        
except Exception as e:
    print(f"[ERRO] {str(e)}")

# Verificar projeto local
import os
local_path = r"C:\Projetos Git\dev-cloud"
print(f"\n[2] Verificando projeto local: {local_path}")

if os.path.exists(local_path):
    print("[OK] Diretorio existe")
    
    # Verificar index.html
    index_path = os.path.join(local_path, "index.html")
    if os.path.exists(index_path):
        print("[OK] index.html encontrado")
    else:
        print("[AVISO] index.html nao encontrado")
else:
    print("[ERRO] Diretorio nao existe")

print("\n" + "="*60)
print("SOLUCAO:")
print("1. Verificar bucket policy do S3")
print("2. Sincronizar conteudo local com S3")
print("3. Atualizar link no Hub")
print("="*60)
