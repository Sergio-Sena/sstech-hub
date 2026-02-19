import boto3

cf = boto3.client('cloudfront')

cf_id = "E233IHQWZDF2M2"
bucket = "financaspessoais.sstechnologies-cloud.com"

print("="*60)
print("CORRIGINDO FINANCAS - MUDANDO PARA BUCKET ENDPOINT")
print("="*60)

try:
    # Obter config
    response = cf.get_distribution_config(Id=cf_id)
    config = response['DistributionConfig']
    etag = response['ETag']
    
    # Mudar origin de website para bucket
    origin = config['Origins']['Items'][0]
    origin['DomainName'] = f"{bucket}.s3.us-east-1.amazonaws.com"
    origin['S3OriginConfig'] = {'OriginAccessIdentity': ''}
    origin['OriginAccessControlId'] = "E2VFVTDE7BY9N8"
    
    # Remover CustomOriginConfig se existir
    if 'CustomOriginConfig' in origin:
        del origin['CustomOriginConfig']
    
    print(f"[OK] Origin alterado para: {origin['DomainName']}")
    
    # Atualizar
    cf.update_distribution(
        Id=cf_id,
        DistributionConfig=config,
        IfMatch=etag
    )
    print("[OK] CloudFront atualizado")
    
    # Invalidar
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
print("CONCLUIDO! Aguarde 5-10 minutos")
print("="*60)
