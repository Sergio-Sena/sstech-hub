#!/usr/bin/env python3
import hashlib

# Hash encontrado no DynamoDB para sergio_sena
hash_sergio = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"

# Senhas comuns para testar
senhas_teste = [
    "sergio123",
    "sena123", 
    "sergio",
    "sena",
    "admin123",
    "123456",
    "password",
    "sergio_sena",
    "midiaflow123",
    "sstech123"
]

print("Testando senhas comuns para sergio_sena:")
print("=" * 50)

for senha in senhas_teste:
    hash_teste = hashlib.sha256(senha.encode()).hexdigest()
    if hash_teste == hash_sergio:
        print(f"✓ SENHA ENCONTRADA: {senha}")
        print(f"  Hash: {hash_teste}")
        break
    else:
        print(f"✗ {senha} -> {hash_teste[:20]}...")

print("\nHash original:", hash_sergio)