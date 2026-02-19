import requests

print("CONFIRMACAO FINAL - PROJETOS HUB")
print("=" * 40)

projetos = {
    "Portfolio": "https://dev-cloud.sstechnologies-cloud.com",
    "AWS Services": "https://aws-services.sstechnologies-cloud.com", 
    "Financas": "https://financaspessoais.sstechnologies-cloud.com",
    "Midiaflow": "https://midiaflow.sstechnologies-cloud.com"
}

online_count = 0

for nome, url in projetos.items():
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"[OK] {nome:12} | ONLINE")
            online_count += 1
        else:
            print(f"[ER] {nome:12} | Status {response.status_code}")
    except:
        print(f"[XX] {nome:12} | ERRO CONEXAO")

print("=" * 40)
print(f"RESULTADO: {online_count}/4 projetos online")

if online_count == 4:
    print("SUCESSO: Todos os projetos principais estao ONLINE!")
    print("AWS Services confirmado funcionando no hub!")
else:
    print(f"ATENCAO: {4-online_count} projetos com problema")