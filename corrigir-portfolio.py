import boto3
import json

s3 = boto3.client('s3')
cf = boto3.client('cloudfront')

bucket = "portfolio-sergio-sena"
cf_id = "E23SOSSVGQ2NOD"

print("="*60)
print("CORRIGINDO PORTFOLIO")
print("="*60)

# 1. Verificar bucket policy atual
print(f"\n[1] Verificando bucket: {bucket}")
try:
    policy = s3.get_bucket_policy(Bucket=bucket)
    print("[OK] Bucket policy existe")
except:
    print("[AVISO] Sem bucket policy")

# 2. Aplicar policy correta para CloudFront OAC
print(f"\n[2] Aplicando bucket policy correta...")

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCloudFrontServicePrincipal",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket}/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": f"arn:aws:cloudfront::969430605054:distribution/{cf_id}"
                }
            }
        }
    ]
}

try:
    s3.put_bucket_policy(Bucket=bucket, Policy=json.dumps(policy))
    print("[OK] Bucket policy atualizada")
except Exception as e:
    print(f"[ERRO] {str(e)}")

# 3. Sincronizar conteúdo
print(f"\n[3] Sincronizando conteudo...")
import subprocess

cmd = f'aws s3 sync "C:\\Projetos Git\\dev-cloud" s3://{bucket}/ --delete'
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

if result.returncode == 0:
    print("[OK] Sincronizacao concluida")
else:
    print(f"[ERRO] {result.stderr}")

# 4. Invalidar cache
print(f"\n[4] Invalidando cache CloudFront...")
try:
    cf.create_invalidation(
        DistributionId=cf_id,
        InvalidationBatch={
            'Paths': {'Quantity': 1, 'Items': ['/*']},
            'CallerReference': str(hash(bucket))
        }
    )
    print("[OK] Cache invalidado")
except Exception as e:
    print(f"[ERRO] {str(e)}")

print("\n" + "="*60)
print("CONCLUIDO!")
print("Aguarde 2-3 minutos e teste:")
print("https://dev-cloud.sstechnologies-cloud.com/")
print("="*60)
