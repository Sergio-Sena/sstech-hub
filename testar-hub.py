import requests

print("="*60)
print("TESTANDO ACESSO AO HUB")
print("="*60)

url = "https://hub.sstechnologies-cloud.com"

try:
    response = requests.get(url, timeout=10)
    print(f"\nURL: {url}")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        print("\n[OK] HUB ESTA ONLINE!")
        print(f"Tamanho: {len(response.content)} bytes")
        
        # Verificar se tem o conteúdo esperado
        if "SStech" in response.text and "Hub" in response.text:
            print("[OK] Conteudo correto detectado")
        else:
            print("[AVISO] Conteudo pode estar incorreto")
    else:
        print(f"\n[ERRO] Status {response.status_code}")
        
except Exception as e:
    print(f"\n[ERRO] {str(e)}")

print("\n" + "="*60)
