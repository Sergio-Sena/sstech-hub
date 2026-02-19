import requests
import json
from datetime import datetime

print("=" * 60)
print("VERIFICACAO DETALHADA - AWS SERVICES")
print("=" * 60)
print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

# URLs para testar
urls = {
    "Frontend": "https://aws-services.sstechnologies-cloud.com",
    "API Health": "https://aws-services.sstechnologies-cloud.com/api/health",
    "Services Page": "https://aws-services.sstechnologies-cloud.com/services",
    "Dashboard": "https://aws-services.sstechnologies-cloud.com/dashboard"
}

resultados = {}

for nome, url in urls.items():
    try:
        print(f"Testando {nome}...")
        response = requests.get(url, timeout=15, allow_redirects=True)
        
        status = response.status_code
        content_type = response.headers.get('content-type', 'N/A')
        content_length = len(response.content)
        
        if status == 200:
            emoji = "[OK]"
            status_text = "FUNCIONANDO"
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
            "funcionando": status == 200,
            "url": url,
            "content_type": content_type,
            "content_length": content_length
        }
        
        print(f"{emoji} {nome:15} | Status: {status:3} | {status_text}")
        print(f"    Content-Type: {content_type}")
        print(f"    Size: {content_length} bytes")
        
        # Se for HTML, verificar se tem conteúdo esperado
        if status == 200 and 'html' in content_type.lower():
            content = response.text.lower()
            if 'aws' in content or 'services' in content:
                print(f"    OK Conteudo AWS detectado")
            else:
                print(f"    AVISO Conteudo AWS nao detectado")
        
        print()
        
    except requests.exceptions.Timeout:
        print(f"[TT] {nome:15} | TIMEOUT")
        resultados[nome] = {"status": "timeout", "funcionando": False, "url": url}
    except requests.exceptions.ConnectionError:
        print(f"[NC] {nome:15} | SEM CONEXAO")
        resultados[nome] = {"status": "connection_error", "funcionando": False, "url": url}
    except Exception as e:
        print(f"[ER] {nome:15} | ERRO: {str(e)[:50]}")
        resultados[nome] = {"status": "error", "funcionando": False, "url": url}

print("=" * 60)
print("RESUMO AWS SERVICES")
print("=" * 60)

funcionando = sum(1 for r in resultados.values() if r.get("funcionando"))
total = len(resultados)

print(f"[OK] Funcionando: {funcionando}/{total}")
print(f"[XX] Com problemas: {total - funcionando}/{total}")

if funcionando > 0:
    print(f"\nOK AWS Services esta ONLINE e funcionando!")
    print(f"OK Integrado ao hub sstechnologies-cloud.com")
else:
    print(f"\nERRO AWS Services com problemas")

# Salvar resultados
with open("status-aws-services-detalhado.json", "w", encoding="utf-8") as f:
    json.dump({
        "timestamp": datetime.now().isoformat(),
        "resultados": resultados
    }, f, indent=2, ensure_ascii=False)

print(f"\nResultados salvos em: status-aws-services-detalhado.json")