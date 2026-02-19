import boto3
import json
from datetime import datetime

print("="*60)
print("DIAGNOSTICO AWS - PROJETOS HUB")
print("Persona: meumanus (FinOps & AWS Specialist)")
print("="*60)

# Clientes AWS
s3 = boto3.client('s3')
cf = boto3.client('cloudfront')
r53 = boto3.client('route53')

diagnostico = {
    "timestamp": datetime.now().isoformat(),
    "s3_buckets": [],
    "cloudfront_distributions": [],
    "route53_zones": [],
    "problemas": []
}

# 1. Verificar S3 Buckets
print("\n[1/3] Analisando S3 Buckets...")
try:
    buckets = s3.list_buckets()['Buckets']
    for bucket in buckets:
        nome = bucket['Name']
        if 'sstechnologies-cloud' in nome or 'dev-cloud' in nome:
            try:
                # Verificar policy
                policy = s3.get_bucket_policy(Bucket=nome)
                tem_policy = True
            except:
                tem_policy = False
            
            # Verificar website
            try:
                website = s3.get_bucket_website(Bucket=nome)
                tem_website = True
            except:
                tem_website = False
            
            diagnostico['s3_buckets'].append({
                "nome": nome,
                "tem_policy": tem_policy,
                "tem_website": tem_website
            })
            print(f"  [OK] {nome} | Policy: {tem_policy} | Website: {tem_website}")
except Exception as e:
    print(f"  [ERRO] {str(e)}")
    diagnostico['problemas'].append(f"S3: {str(e)}")

# 2. Verificar CloudFront
print("\n[2/3] Analisando CloudFront Distributions...")
try:
    dists = cf.list_distributions()
    if 'DistributionList' in dists and 'Items' in dists['DistributionList']:
        for dist in dists['DistributionList']['Items']:
            aliases = dist.get('Aliases', {}).get('Items', [])
            for alias in aliases:
                if 'sstechnologies-cloud' in alias:
                    origin = dist['Origins']['Items'][0]['DomainName']
                    diagnostico['cloudfront_distributions'].append({
                        "id": dist['Id'],
                        "alias": alias,
                        "status": dist['Status'],
                        "origin": origin
                    })
                    print(f"  [OK] {alias}")
                    print(f"       ID: {dist['Id']}")
                    print(f"       Origin: {origin}")
                    print(f"       Status: {dist['Status']}")
except Exception as e:
    print(f"  [ERRO] {str(e)}")
    diagnostico['problemas'].append(f"CloudFront: {str(e)}")

# 3. Verificar Route53
print("\n[3/3] Analisando Route53...")
try:
    zones = r53.list_hosted_zones()['HostedZones']
    for zone in zones:
        if 'sstechnologies-cloud' in zone['Name']:
            diagnostico['route53_zones'].append({
                "nome": zone['Name'],
                "id": zone['Id']
            })
            print(f"  [OK] {zone['Name']}")
except Exception as e:
    print(f"  [ERRO] {str(e)}")
    diagnostico['problemas'].append(f"Route53: {str(e)}")

# Análise de Problemas
print("\n" + "="*60)
print("ANALISE DE PROBLEMAS")
print("="*60)

# Verificar erro 403
projetos_403 = ["dev-cloud", "aws-services", "financaspessoais"]
for projeto in projetos_403:
    bucket_existe = any(projeto in b['nome'] for b in diagnostico['s3_buckets'])
    cf_existe = any(projeto in d['alias'] for d in diagnostico['cloudfront_distributions'])
    
    if bucket_existe and cf_existe:
        print(f"\n[403] {projeto}")
        print("  Causa provavel: OAC/Bucket Policy incorreta")
        print("  Solucao: Atualizar bucket policy para permitir CloudFront")
    elif bucket_existe and not cf_existe:
        print(f"\n[SEM CF] {projeto}")
        print("  Causa: CloudFront nao configurado")
    elif not bucket_existe:
        print(f"\n[SEM BUCKET] {projeto}")
        print("  Causa: Bucket S3 nao existe")

# Salvar diagnóstico
with open("diagnostico-aws-completo.json", "w", encoding="utf-8") as f:
    json.dump(diagnostico, f, indent=2, ensure_ascii=False)

print(f"\n\nDiagnostico salvo em: diagnostico-aws-completo.json")
print("\n" + "="*60)
print("RECOMENDACOES meumanus:")
print("="*60)
print("1. Corrigir bucket policies dos projetos com erro 403")
print("2. Criar CloudFront distributions para projetos sem conexao")
print("3. Configurar OAC (Origin Access Control) para seguranca")
print("="*60)
