import boto3
import time

cf = boto3.client('cloudfront')

PROJETOS_BLOQUEADOS = [
    {"nome": "AWS Services", "cf_id": "E1U10Q11WGDP01", "oac_id": "E2U1S1O8OK84Y7"},
    {"nome": "Financas", "cf_id": "E233IHQWZDF2M2", "oac_id": None},  # Precisa criar
    {"nome": "Ritech", "cf_id": "E2PT7P40RJBK38", "oac_id": "E9ZMQJHAHZBIC"},
    {"nome": "AWS Cert", "cf_id": "EW17MMXFBIMW6", "oac_id": "E1IJIO903N4MB8"}
]

print("="*60)
print("CONFIGURANDO OAC NOS CLOUDFRONT")
print("="*60)

for projeto in PROJETOS_BLOQUEADOS:
    print(f"\n[{projeto['nome']}]")
    print(f"CloudFront: {projeto['cf_id']}")
    
    try:
        # Obter config atual
        response = cf.get_distribution_config(Id=projeto['cf_id'])
        config = response['DistributionConfig']
        etag = response['ETag']
        
        # Atualizar origin com OAC
        origin = config['Origins']['Items'][0]
        
        # Remover OAI se existir
        if 'S3OriginConfig' in origin:
            origin['S3OriginConfig']['OriginAccessIdentity'] = ''
        
        # Adicionar OAC
        if projeto['oac_id']:
            origin['OriginAccessControlId'] = projeto['oac_id']
            print(f"  [OK] OAC configurado: {projeto['oac_id']}")
        else:
            # Criar OAC para Finanças
            oac_response = cf.create_origin_access_control(
                OriginAccessControlConfig={
                    'Name': f"OAC-{projeto['nome']}-{int(time.time())}",
                    'Description': f"OAC para {projeto['nome']}",
                    'SigningProtocol': 'sigv4',
                    'SigningBehavior': 'always',
                    'OriginAccessControlOriginType': 's3'
                }
            )
            oac_id = oac_response['OriginAccessControl']['Id']
            origin['OriginAccessControlId'] = oac_id
            print(f"  [OK] OAC criado: {oac_id}")
        
        # Atualizar distribution
        cf.update_distribution(
            Id=projeto['cf_id'],
            DistributionConfig=config,
            IfMatch=etag
        )
        print(f"  [OK] CloudFront atualizado")
        
        # Invalidar cache
        cf.create_invalidation(
            DistributionId=projeto['cf_id'],
            InvalidationBatch={
                'Paths': {'Quantity': 1, 'Items': ['/*']},
                'CallerReference': str(time.time())
            }
        )
        print(f"  [OK] Cache invalidado")
        
    except Exception as e:
        print(f"  [ERRO] {str(e)[:80]}")

print("\n" + "="*60)
print("CONFIGURACAO CONCLUIDA!")
print("Aguarde 5-10 minutos para CloudFront propagar as mudancas")
print("="*60)
