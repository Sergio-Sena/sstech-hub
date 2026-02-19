# Resolver Acesso SSO AWS de Forma Permanente

## 🎯 PROBLEMA
Token SSO expira constantemente, causando erro "ForbiddenException: No access"

## ✅ SOLUÇÕES PERMANENTES

### 1. **Usar IAM User ao invés de SSO** (RECOMENDADO)
```bash
# Criar usuário IAM com permissões administrativas
aws iam create-user --user-name sergio-dev
aws iam attach-user-policy --user-name sergio-dev --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
aws iam create-access-key --user-name sergio-dev
```

**Configurar credenciais permanentes:**
```bash
aws configure
# AWS Access Key ID: [sua-access-key]
# AWS Secret Access Key: [sua-secret-key] 
# Default region: us-east-1
# Default output format: json
```

### 2. **Automatizar Renovação SSO**
Criar script que renova automaticamente:

```batch
@echo off
echo Renovando token SSO...
aws sso login --profile default
if %errorlevel% equ 0 (
    echo Token renovado com sucesso!
) else (
    echo Erro ao renovar token
)
```

### 3. **Configurar Profile Permanente**
```bash
# Editar ~/.aws/config
[profile dev]
sso_start_url = https://d-906636b78b.awsapps.com/start
sso_region = us-east-1
sso_account_id = SEU_ACCOUNT_ID
sso_role_name = AdministratorAccess
region = us-east-1
```

## 🚀 IMPLEMENTAÇÃO RECOMENDADA

### Passo 1: Criar IAM User
1. Acesse AWS Console → IAM
2. Users → Create User
3. Nome: `sergio-dev`
4. Attach policy: `AdministratorAccess`
5. Create access key → CLI

### Passo 2: Configurar Localmente
```bash
aws configure
# Inserir as credenciais do IAM User
```

### Passo 3: Testar
```bash
aws sts get-caller-identity
aws s3 ls
```

## ⚠️ SEGURANÇA
- **IAM User**: Credenciais não expiram, mais conveniente
- **SSO**: Mais seguro, mas expira periodicamente
- **Recomendação**: IAM User para desenvolvimento, SSO para produção

## 🔧 COMANDOS DE DIAGNÓSTICO
```bash
# Verificar configuração atual
aws configure list

# Verificar profiles
aws configure list-profiles

# Testar acesso
aws sts get-caller-identity

# Limpar configuração
aws configure set aws_access_key_id ""
aws configure set aws_secret_access_key ""
```

## 📋 CHECKLIST
- [ ] Decidir entre IAM User ou SSO
- [ ] Criar credenciais no AWS Console
- [ ] Configurar AWS CLI localmente
- [ ] Testar acesso com `aws s3 ls`
- [ ] Documentar credenciais em local seguro