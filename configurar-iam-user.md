# Configurar IAM User - Acesso Permanente AWS

## 🎯 OBJETIVO
Criar usuário IAM com credenciais permanentes para desenvolvimento.

## 📋 PASSO A PASSO

### 1. Criar IAM User no Console AWS
1. Acesse: https://console.aws.amazon.com/iam/
2. **Users** → **Create user**
3. **User name**: `sergio-dev`
4. **Next**

### 2. Configurar Permissões
1. **Attach policies directly**
2. Buscar e selecionar: `AdministratorAccess`
3. **Next** → **Create user**

### 3. Criar Access Key
1. Clique no usuário `sergio-dev` criado
2. **Security credentials** tab
3. **Create access key**
4. Selecione: **Command Line Interface (CLI)**
5. Marque: "I understand the above recommendation"
6. **Next** → **Create access key**

### 4. Salvar Credenciais
```
Access Key ID: AKIA...
Secret Access Key: wJalrXUt...
```
⚠️ **IMPORTANTE**: Copie e salve em local seguro!

### 5. Configurar AWS CLI Local
```bash
aws configure
```
Inserir:
- **AWS Access Key ID**: [sua access key]
- **AWS Secret Access Key**: [sua secret key]  
- **Default region name**: us-east-1
- **Default output format**: json

### 6. Testar Configuração
```bash
aws sts get-caller-identity
aws s3 ls
```

## ✅ RESULTADO ESPERADO
```json
{
    "UserId": "AIDA...",
    "Account": "123456789012", 
    "Arn": "arn:aws:iam::123456789012:user/sergio-dev"
}
```

## 🔧 COMANDOS DE VERIFICAÇÃO
```bash
# Verificar configuração
aws configure list

# Testar acesso S3
aws s3 ls

# Testar criação de bucket
aws s3 mb s3://teste-sergio-dev --region us-east-1
aws s3 rb s3://teste-sergio-dev
```

## 🚀 PRÓXIMOS PASSOS
Após configurar IAM User, execute:
```bash
cd "c:\Projetos Git\sstech-hub"
aws s3 mb s3://hub-home-sstechnologies-cloud --region us-east-1
aws s3 mb s3://automacao-sstechnologies-cloud --region us-east-1
```