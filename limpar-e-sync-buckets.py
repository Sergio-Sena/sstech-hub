import subprocess

PROJETOS = [
    {
        "nome": "AWS Services",
        "local": r"C:\Projetos Git\AWS-Services\frontend-next",
        "bucket": "aws-services-dashboard-prod"
    },
    {
        "nome": "Ritech",
        "local": r"C:\Projetos Git\Loja-Ritech",
        "bucket": "ritech-fechaduras-site"
    },
    {
        "nome": "AWS Cert",
        "local": r"C:\Projetos Git\AWS-Certification-Platform",
        "bucket": "aws-cert-platform-2025"
    }
]

print("="*60)
print("LIMPANDO E SINCRONIZANDO BUCKETS")
print("="*60)

for projeto in PROJETOS:
    print(f"\n[{projeto['nome']}]")
    
    # Limpar bucket
    print(f"  Limpando bucket...")
    cmd_clean = f'aws s3 rm s3://{projeto["bucket"]}/ --recursive'
    subprocess.run(cmd_clean, shell=True, capture_output=True)
    print(f"  [OK] Bucket limpo")
    
    # Sincronizar apenas arquivos necessários
    print(f"  Sincronizando arquivos...")
    cmd_sync = f'aws s3 sync "{projeto["local"]}" s3://{projeto["bucket"]}/ --exclude ".git/*" --exclude ".next/*" --exclude "node_modules/*" --exclude "*.md" --exclude ".env*"'
    
    result = subprocess.run(cmd_sync, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"  [OK] Sincronizado")
    else:
        print(f"  [ERRO] {result.stderr[:60]}")

print("\n" + "="*60)
print("CONCLUIDO! Aguarde 2-3 minutos")
print("="*60)
