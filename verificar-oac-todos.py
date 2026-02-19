import boto3
import json

cf = boto3.client('cloudfront')
s3 = boto3.client('s3')

PROJETOS = {
    "Portfolio": {"bucket": "portfolio-sergio-sena", "cf_id": "E23SOSSVGQ2NOD"},
    "AWS Services": {"bucket": "aws-services-dashboard-prod", "cf_id": "E1U10Q11WGDP01"},
    "Financas": {"bucket": "financaspessoais.sstechnologies-cloud.com", "cf_id": "E233IHQWZDF2M2"},
    "Ritech": {"bucket": "ritech-fechaduras-site", "cf_id": "E2PT7P40RJBK38"},
    "Gestao Trafego": {"bucket": "ssgestaodetrafego", "cf_id": "E32SZD5BCOGZDM"},
    "AWS Cert": {"bucket": "aws-cert-platform-2025", "cf_id": "EW17MMXFBIMW6"}
}

print("="*60)
print("VERIFICANDO OAC - TODOS OS PROJETOS HUB")
print("="*60)

for nome, config in PROJETOS.items():
    print(f"\n[{nome}]")
    print(f"Bucket: {config['bucket']}")
    print(f"CloudFront: {config['cf_id']}")
    
    # Verificar CloudFront Origin
    try:
        dist = cf.get_distribution_config(Id=config['cf_id'])
        origin = dist['DistributionConfig']['Origins']['Items'][0]
        
        if 'OriginAccessControlId' in origin and origin['OriginAccessControlId']:
            print(f"  [OK] OAC configurado: {origin['OriginAccessControlId']}")
        else:
            print(f"  [AVISO] OAC nao configurado (usando OAI ou publico)")
            
    except Exception as e:
        print(f"  [ERRO] {str(e)[:50]}")
    
    # Aplicar bucket policy com OAC
    try:
        policy = {
            "Version": "2012-10-17",
            "Statement": [{
                "Sid": "AllowCloudFrontOAC",
                "Effect": "Allow",
                "Principal": {"Service": "cloudfront.amazonaws.com"},
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{config['bucket']}/*",
                "Condition": {
                    "StringEquals": {
                        "AWS:SourceArn": f"arn:aws:cloudfront::969430605054:distribution/{config['cf_id']}"
                    }
                }
            }]
        }
        
        s3.put_bucket_policy(Bucket=config['bucket'], Policy=json.dumps(policy))
        print(f"  [OK] Bucket policy OAC aplicada")
        
    except Exception as e:
        print(f"  [ERRO] Policy: {str(e)[:50]}")

print("\n" + "="*60)
print("VERIFICACAO CONCLUIDA")
print("="*60)
