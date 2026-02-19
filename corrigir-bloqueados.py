import boto3
import json

cf = boto3.client('cloudfront')
s3 = boto3.client('s3')

BLOQUEADOS = [
    {"nome": "AWS Services", "bucket": "aws-services-dashboard-prod", "cf_id": "E1U10Q11WGDP01"},
    {"nome": "Ritech", "bucket": "ritech-fechaduras-site", "cf_id": "E2PT7P40RJBK38"},
    {"nome": "AWS Cert", "bucket": "aws-cert-platform-2025", "cf_id": "EW17MMXFBIMW6"}
]

print("="*60)
print("DIAGNOSTICANDO E CORRIGINDO PROJETOS BLOQUEADOS")
print("="*60)

for projeto in BLOQUEADOS:
    print(f"\n[{projeto['nome']}]")
    
    # Verificar se bucket existe
    try:
        s3.head_bucket(Bucket=projeto['bucket'])
        print(f"  [OK] Bucket existe: {projeto['bucket']}")
    except:
        print(f"  [ERRO] Bucket nao existe!")
        continue
    
    # Verificar OAC no CloudFront
    try:
        dist = cf.get_distribution_config(Id=projeto['cf_id'])
        origin = dist['DistributionConfig']['Origins']['Items'][0]
        
        if 'OriginAccessControlId' in origin and origin['OriginAccessControlId']:
            oac_id = origin['OriginAccessControlId']
            print(f"  [OK] OAC no CloudFront: {oac_id}")
            
            # Aplicar bucket policy
            policy = {
                "Version": "2012-10-17",
                "Statement": [{
                    "Sid": "AllowCloudFrontOAC",
                    "Effect": "Allow",
                    "Principal": {"Service": "cloudfront.amazonaws.com"},
                    "Action": "s3:GetObject",
                    "Resource": f"arn:aws:s3:::{projeto['bucket']}/*",
                    "Condition": {
                        "StringEquals": {
                            "AWS:SourceArn": f"arn:aws:cloudfront::969430605054:distribution/{projeto['cf_id']}"
                        }
                    }
                }]
            }
            
            s3.put_bucket_policy(Bucket=projeto['bucket'], Policy=json.dumps(policy))
            print(f"  [OK] Bucket policy aplicada")
            
            # Invalidar cache
            cf.create_invalidation(
                DistributionId=projeto['cf_id'],
                InvalidationBatch={
                    'Paths': {'Quantity': 1, 'Items': ['/*']},
                    'CallerReference': str(hash(projeto['nome']))
                }
            )
            print(f"  [OK] Cache invalidado")
        else:
            print(f"  [ERRO] OAC nao configurado no CloudFront")
            
    except Exception as e:
        print(f"  [ERRO] {str(e)[:60]}")

print("\n" + "="*60)
print("CORRECAO CONCLUIDA!")
print("Aguarde 2-3 minutos e teste novamente")
print("="*60)
