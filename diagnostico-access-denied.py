import boto3
import json

s3 = boto3.client('s3')
cf = boto3.client('cloudfront')

PROJETOS = [
    {"nome": "AWS Services", "bucket": "aws-services-dashboard-prod", "cf_id": "E1U10Q11WGDP01"},
    {"nome": "Ritech", "bucket": "ritech-fechaduras-site", "cf_id": "E2PT7P40RJBK38"},
    {"nome": "AWS Cert", "bucket": "aws-cert-platform-2025", "cf_id": "EW17MMXFBIMW6"}
]

print("="*60)
print("DIAGNOSTICO COMPLETO - ACCESS DENIED")
print("="*60)

for projeto in PROJETOS:
    print(f"\n[{projeto['nome']}]")
    
    # 1. Verificar se bucket tem Block Public Access
    try:
        block = s3.get_public_access_block(Bucket=projeto['bucket'])
        print(f"  Block Public Access: {block['PublicAccessBlockConfiguration']}")
    except:
        print(f"  Block Public Access: Nao configurado")
    
    # 2. Verificar bucket policy
    try:
        policy = s3.get_bucket_policy(Bucket=projeto['bucket'])
        policy_json = json.loads(policy['Policy'])
        print(f"  Bucket Policy: Existe")
        
        # Verificar se tem Statement correto
        for stmt in policy_json.get('Statement', []):
            if stmt.get('Principal', {}).get('Service') == 'cloudfront.amazonaws.com':
                print(f"  CloudFront Principal: OK")
                if 'Condition' in stmt:
                    print(f"  Condition SourceArn: OK")
                else:
                    print(f"  [ERRO] Falta Condition SourceArn!")
            else:
                print(f"  [AVISO] Principal incorreto: {stmt.get('Principal')}")
    except Exception as e:
        print(f"  [ERRO] Bucket Policy: {str(e)[:50]}")
    
    # 3. Verificar CloudFront Origin
    try:
        dist = cf.get_distribution_config(Id=projeto['cf_id'])
        origin = dist['DistributionConfig']['Origins']['Items'][0]
        
        print(f"  Origin Domain: {origin['DomainName']}")
        
        if 'OriginAccessControlId' in origin and origin['OriginAccessControlId']:
            print(f"  OAC ID: {origin['OriginAccessControlId']}")
        else:
            print(f"  [ERRO] OAC nao configurado!")
        
        # Verificar se tem OAI (antigo)
        if 'S3OriginConfig' in origin:
            oai = origin['S3OriginConfig'].get('OriginAccessIdentity', '')
            if oai:
                print(f"  [ERRO] Ainda usa OAI (antigo): {oai}")
                print(f"  [SOLUCAO] Remover OAI e usar apenas OAC")
                
    except Exception as e:
        print(f"  [ERRO] CloudFront: {str(e)[:50]}")

print("\n" + "="*60)
print("CAUSA PROVAVEL:")
print("CloudFront tem OAC mas bucket policy nao permite")
print("OU CloudFront ainda tem OAI configurado junto com OAC")
print("="*60)
