import requests

links = [
    "https://ritech-fechaduras-digitais.sstechnologies-cloud.com/",
    "https://aws-services.sstechnologies-cloud.com/"
]

print("="*60)
print("VERIFICANDO LINKS EXATOS")
print("="*60)

for url in links:
    try:
        response = requests.get(url, timeout=10)
        print(f"\n{url}")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 403:
            print("BLOQUEADO - Erro 403")
        elif response.status_code == 200:
            print("ONLINE - Funcionando")
            
    except Exception as e:
        print(f"ERRO: {str(e)}")

print("\n" + "="*60)
print("AUTOMACAO DE SISTEMAS")
print("="*60)
print("Status: EM DESENVOLVIMENTO (85%)")
print("Nao tem CloudFront/dominio configurado ainda")
print("Precisa criar pagina 'Em Desenvolvimento' no Hub")
print("="*60)
