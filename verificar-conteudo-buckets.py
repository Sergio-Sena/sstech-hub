import boto3

s3 = boto3.client('s3')

BUCKETS = [
    "aws-services-dashboard-prod",
    "ritech-fechaduras-site", 
    "aws-cert-platform-2025"
]

print("="*60)
print("VERIFICANDO CONTEUDO DOS BUCKETS")
print("="*60)

for bucket in BUCKETS:
    print(f"\n[{bucket}]")
    try:
        # Listar primeiros 10 objetos
        response = s3.list_objects_v2(Bucket=bucket, MaxKeys=10)
        
        if 'Contents' in response:
            print(f"  Total objetos: {response.get('KeyCount', 0)}")
            
            # Verificar index.html
            has_index = False
            for obj in response['Contents']:
                if obj['Key'] == 'index.html':
                    has_index = True
                    print(f"  [OK] index.html encontrado")
                    break
            
            if not has_index:
                print(f"  [ERRO] index.html NAO encontrado!")
                print(f"  Arquivos: {[obj['Key'] for obj in response['Contents'][:5]]}")
        else:
            print(f"  [ERRO] Bucket vazio!")
            
    except Exception as e:
        print(f"  [ERRO] {str(e)[:60]}")

print("\n" + "="*60)
