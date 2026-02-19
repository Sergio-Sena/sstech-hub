import boto3
import subprocess
import time

s3 = boto3.client('s3')
cf = boto3.client('cloudfront')

PROJETOS = [
    {"nome": "Portfolio", "local": r"C:\Projetos Git\dev-cloud", "bucket": "portfolio-sergio-sena", "cf_id": "E23SOSSVGQ2NOD"},
    {"nome": "AWS Services", "local": r"C:\Projetos Git\AWS-Services\frontend-next", "bucket": "aws-services-dashboard-prod", "cf_id": "E1U10Q11WGDP01"},
    {"nome": "Financas", "local": r"C:\Projetos Git\controle de gastos sergiosena", "bucket": "financaspessoais.sstechnologies-cloud.com", "cf_id": "E233IHQWZDF2M2"},
    {"nome": "Ritech", "local": r"C:\Projetos Git\Loja-Ritech", "bucket": "ritech-fechaduras-site", "cf_id": "E2PT7P40RJBK38"},
    {"nome": "Gestao Trafego", "local": r"C:\Projetos Git\SS-Gestao-de-Trafego", "bucket": "ssgestaodetrafego", "cf_id": "E32SZD5BCOGZDM"},
    {"nome": "AWS Cert", "local": r"C:\Projetos Git\AWS-Certification-Platform", "bucket": "aws-cert-platform-2025", "cf_id": "EW17MMXFBIMW6"}
]

print("="*60)
print("SINCRONIZACAO FINAL - PROJETOS HUB")
print("="*60)

for projeto in PROJETOS:
    print(f"\n[{projeto['nome']}]")
    
    # Sync S3
    cmd = f'aws s3 sync "{projeto["local"]}" s3://{projeto["bucket"]}/ --delete'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"  [OK] Sincronizado")
    else:
        print(f"  [ERRO] {result.stderr[:50]}")
        continue
    
    # Invalidar cache
    try:
        cf.create_invalidation(
            DistributionId=projeto['cf_id'],
            InvalidationBatch={
                'Paths': {'Quantity': 1, 'Items': ['/*']},
                'CallerReference': str(time.time())
            }
        )
        print(f"  [OK] Cache invalidado")
    except Exception as e:
        print(f"  [ERRO] {str(e)[:50]}")

print("\n" + "="*60)
print("SINCRONIZACAO CONCLUIDA!")
print("\nAguarde 2-3 minutos e teste os projetos:")
print("- https://dev-cloud.sstechnologies-cloud.com/")
print("- https://aws-services.sstechnologies-cloud.com")
print("- https://financaspessoais.sstechnologies-cloud.com")
print("- https://ritech-fechaduras-digitais.sstechnologies-cloud.com")
print("- https://sstrafegopago.sstechnologies-cloud.com")
print("- https://aws-certification-platform.sstechnologies-cloud.com")
print("="*60)
