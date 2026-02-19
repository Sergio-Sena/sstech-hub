# Script de Sincronizacao - Projetos Hub
# Persona: Base (Arquiteto de Software)

import json
import subprocess
import os

print("="*60)
print("SINCRONIZACAO PROJETOS HUB")
print("Persona: Base (Arquiteto de Software)")
print("="*60)

# Carregar diagnóstico
with open("diagnostico-aws-completo.json", "r", encoding="utf-8") as f:
    diag = json.load(f)

# Mapeamento correto baseado no diagnóstico
PROJETOS = {
    "Portfolio": {
        "local": r"C:\Projetos Git\dev-cloud",
        "bucket": "portfolio-sergio-sena",
        "cf_id": "E23SOSSVGQ2NOD",
        "dominio": "dev-cloud.sstechnologies-cloud.com",
        "obs": "Contem STGBR e Base Imoveis"
    },
    "AWS Services": {
        "local": r"C:\Projetos Git\AWS-Services\frontend-next",
        "bucket": "aws-services-dashboard-prod",
        "cf_id": "E1U10Q11WGDP01",
        "dominio": "aws-services.sstechnologies-cloud.com"
    },
    "Financas": {
        "local": r"C:\Projetos Git\controle de gastos sergiosena",
        "bucket": "financaspessoais.sstechnologies-cloud.com",
        "cf_id": "E233IHQWZDF2M2",
        "dominio": "financaspessoais.sstechnologies-cloud.com"
    },
    "Midiaflow": {
        "local": r"C:\Projetos Git\drive-online-clean-NextJs",
        "bucket": "N/A - API Gateway",
        "cf_id": "E2HZKZ9ZJK18IU",
        "dominio": "midiaflow.sstechnologies-cloud.com",
        "obs": "JA ONLINE - Next.js com API Gateway",
        "skip_sync": True
    },
    "Ritech": {
        "local": r"C:\Projetos Git\Loja-Ritech",
        "bucket": "ritech-fechaduras-site",
        "cf_id": "E2PT7P40RJBK38",
        "dominio": "ritech-fechaduras-digitais.sstechnologies-cloud.com"
    },
    "Gestao Trafego": {
        "local": r"C:\Projetos Git\SS-Gestao-de-Trafego",
        "bucket": "ssgestaodetrafego",
        "cf_id": "E32SZD5BCOGZDM",
        "dominio": "sstrafegopago.sstechnologies-cloud.com"
    },
    "Automacao Sistemas": {
        "local": r"C:\Projetos Git\Automação de sistemas",
        "bucket": "N/A - EM DESENVOLVIMENTO",
        "cf_id": "N/A",
        "dominio": "automacao.sstechnologies-cloud.com",
        "obs": "85% concluido - Aguardando finalizacao",
        "skip_sync": True
    },
    "AWS Certification": {
        "local": r"C:\Projetos Git\AWS-Certification-Platform",
        "bucket": "aws-cert-platform-2025",
        "cf_id": "EW17MMXFBIMW6",
        "dominio": "aws-certification-platform.sstechnologies-cloud.com",
        "obs": "GitHub Pages + CloudFront"
    }
}

def verificar_diretorio(path):
    """Verifica se diretório existe"""
    return os.path.exists(path)

def sync_projeto(nome, config):
    """Sincroniza projeto com S3"""
    print(f"\n{'='*60}")
    print(f"Sincronizando: {nome}")
    print(f"{'='*60}")
    
    # Verificar se deve pular
    if config.get('skip_sync'):
        print(f"[SKIP] {config.get('obs', 'Projeto nao requer sincronizacao')}")
        return True
    
    # Verificar diretório local
    if not verificar_diretorio(config['local']):
        print(f"[ERRO] Diretorio nao encontrado: {config['local']}")
        return False
    
    print(f"[OK] Diretorio local: {config['local']}")
    print(f"[OK] Bucket S3: {config['bucket']}")
    print(f"[OK] CloudFront: {config['cf_id']}")
    if 'obs' in config:
        print(f"[INFO] {config['obs']}")
    
    # Comando de sync
    cmd = f'aws s3 sync "{config["local"]}" s3://{config["bucket"]}/ --delete'
    
    print(f"\n[SYNC] Executando sincronizacao...")
    print(f"Comando: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("[OK] Sincronizacao concluida")
            
            # Invalidar cache CloudFront
            print(f"\n[CACHE] Invalidando CloudFront...")
            inv_cmd = f'aws cloudfront create-invalidation --distribution-id {config["cf_id"]} --paths "/*"'
            inv_result = subprocess.run(inv_cmd, shell=True, capture_output=True, text=True)
            
            if inv_result.returncode == 0:
                print("[OK] Cache invalidado")
                print(f"\n[TESTE] Acesse: https://{config['dominio']}")
                return True
            else:
                print(f"[ERRO] Falha ao invalidar cache: {inv_result.stderr}")
                return False
        else:
            print(f"[ERRO] Falha na sincronizacao: {result.stderr}")
            return False
    except Exception as e:
        print(f"[ERRO] Excecao: {str(e)}")
        return False

# Menu interativo
print("\n" + "="*60)
print("PROJETOS DISPONIVEIS PARA SINCRONIZACAO")
print("="*60)

for i, (nome, config) in enumerate(PROJETOS.items(), 1):
    existe = "[OK]" if verificar_diretorio(config['local']) else "[XX]"
    skip = "[SKIP]" if config.get('skip_sync') else ""
    obs = f" - {config.get('obs', '')}" if 'obs' in config else ""
    print(f"{i}. {existe} {skip} {nome}{obs}")

print("\n0. Sincronizar TODOS")
print("="*60)

escolha = input("\nEscolha o projeto (0-5): ").strip()

if escolha == "0":
    print("\n[INFO] Sincronizando todos os projetos...")
    for nome, config in PROJETOS.items():
        sync_projeto(nome, config)
elif escolha.isdigit() and 1 <= int(escolha) <= len(PROJETOS):
    nome = list(PROJETOS.keys())[int(escolha) - 1]
    sync_projeto(nome, PROJETOS[nome])
else:
    print("[ERRO] Opcao invalida")

print("\n" + "="*60)
print("SINCRONIZACAO FINALIZADA")
print("="*60)
