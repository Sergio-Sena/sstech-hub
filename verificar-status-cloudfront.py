import boto3

cf = boto3.client('cloudfront')

PROJETOS = [
    {"nome": "AWS Services", "cf_id": "E1U10Q11WGDP01"},
    {"nome": "Ritech", "cf_id": "E2PT7P40RJBK38"},
    {"nome": "AWS Cert", "cf_id": "EW17MMXFBIMW6"}
]

print("="*60)
print("VERIFICANDO STATUS CLOUDFRONT")
print("="*60)

for projeto in PROJETOS:
    print(f"\n[{projeto['nome']}]")
    
    try:
        dist = cf.get_distribution(Id=projeto['cf_id'])
        status = dist['Distribution']['Status']
        
        print(f"  Status: {status}")
        
        if status == "InProgress":
            print(f"  [AVISO] CloudFront ainda propagando mudancas")
        elif status == "Deployed":
            print(f"  [OK] CloudFront deployed")
            
            # Verificar origin
            config = dist['Distribution']['DistributionConfig']
            origin = config['Origins']['Items'][0]
            
            print(f"  Origin: {origin['DomainName']}")
            
            if 'OriginAccessControlId' in origin:
                print(f"  OAC: {origin['OriginAccessControlId']}")
            else:
                print(f"  [ERRO] SEM OAC!")
                
    except Exception as e:
        print(f"  [ERRO] {str(e)[:60]}")

print("\n" + "="*60)
