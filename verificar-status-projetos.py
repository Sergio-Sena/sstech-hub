import requests
import json
from datetime import datetime

# Projetos do Hub
projetos = {
    "Portfolio": "https://dev-cloud.sstechnologies-cloud.com",
    "AWS Services": "https://aws-services.sstechnologies-cloud.com",
    "Finanças": "https://financaspessoais.sstechnologies-cloud.com",
    "Mídiaflow": "https://midiaflow.sstechnologies-cloud.com",
    "Ritech": "https://ritech-fechaduras.sstechnologies-cloud.com",
    "Gestão Tráfego": "https://ssgestaodetrafego.sstechnologies-cloud.com",
    "AWS Dashboard": "https://aws-dashboard.sstechnologies-cloud.com"
}

print("=" * 60)
print("VERIFICACAO DE STATUS - PROJETOS HUB")
print("=" * 60)
print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

resultados = {}

for nome, url in projetos.items():
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        status = response.status_code
        
        if status == 200:
            emoji = "[OK]"
            status_text = "ONLINE"
        elif status in [301, 302, 307, 308]:
            emoji = "[>>]"
            status_text = f"REDIRECT ({status})"
        elif status == 403:
            emoji = "[!!]"
            status_text = "BLOQUEADO"
        elif status == 404:
            emoji = "[XX]"
            status_text = "NAO ENCONTRADO"
        else:
            emoji = "[??]"
            status_text = f"ERRO ({status})"
            
        resultados[nome] = {
            "status": status,
            "online": status == 200,
            "url": url
        }
        
        print(f"{emoji} {nome:20} | Status: {status:3} | {status_text}")
        
    except requests.exceptions.Timeout:
        print(f"[TT] {nome:20} | TIMEOUT")
        resultados[nome] = {"status": "timeout", "online": False, "url": url}
    except requests.exceptions.ConnectionError:
        print(f"[NC] {nome:20} | SEM CONEXAO")
        resultados[nome] = {"status": "connection_error", "online": False, "url": url}
    except Exception as e:
        print(f"[ER] {nome:20} | ERRO: {str(e)[:30]}")
        resultados[nome] = {"status": "error", "online": False, "url": url}

print("\n" + "=" * 60)
print("RESUMO")
print("=" * 60)

online = sum(1 for r in resultados.values() if r.get("online"))
total = len(resultados)

print(f"[OK] Online: {online}/{total}")
print(f"[XX] Offline: {total - online}/{total}")

# Salvar resultados
with open("status-projetos-hub.json", "w", encoding="utf-8") as f:
    json.dump({
        "timestamp": datetime.now().isoformat(),
        "resultados": resultados
    }, f, indent=2, ensure_ascii=False)

print(f"\nResultados salvos em: status-projetos-hub.json")
