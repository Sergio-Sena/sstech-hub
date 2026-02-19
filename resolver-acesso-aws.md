# 🔧 Resolver Acesso AWS - Guia Completo

## 🚨 Problema Atual
- AWS SSO configurado mas sem permissões
- ForbiddenException ao executar comandos
- Precisa de acesso para verificar infraestrutura

## 🎯 Soluções (em ordem de prioridade)

### SOLUÇÃO 1: Verificar Permissões SSO (Mais Provável)

#### Passo 1: Acessar Console AWS
1. **Abra o navegador** e acesse:
   ```
   https://d-906636b78b.awsapps.com/start
   ```

2. **Faça login** com suas credenciais SSO

3. **Verifique se consegue acessar** os serviços:
   - Route 53
   - S3
   - CloudFront
   - ACM

#### Passo 2: Verificar Role/Permissões
No console AWS:
1. **Acesse IAM** → Roles
2. **Procure por:** `AdministratorAccess`
3. **Verifique** se o role tem as permissões necessárias

#### Passo 3: Reconfigurar SSO (se necessário)
```bash
# Limpar cache SSO
aws sso logout
rm -rf ~/.aws/sso/cache/*

# Reconfigurar
aws configure sso
```

### SOLUÇÃO 2: Criar Access Keys (Alternativa)

#### Passo 1: Criar Access Keys no Console
1. **Acesse IAM** → Users
2. **Crie um novo usuário** ou use existente
3. **Anexe política:** `AdministratorAccess`
4. **Crie Access Keys**

#### Passo 2: Configurar Credenciais Locais
```bash
aws configure
```
Insira:
- Access Key ID: [SUA_ACCESS_KEY]
- Secret Access Key: [SUA_SECRET_KEY]
- Region: us-east-1
- Output: json

### SOLUÇÃO 3: Usar Profile Específico

#### Criar novo profile
```bash
aws configure --profile admin
```

#### Testar profile
```bash
aws sts get-caller-identity --profile admin
```

### SOLUÇÃO 4: Verificar Configuração Atual

#### Verificar arquivos de configuração
```bash
# Ver configuração atual
cat ~/.aws/config
cat ~/.aws/credentials

# Ver profiles disponíveis
aws configure list-profiles
```

## 🔍 Diagnóstico Detalhado

### Comandos de Diagnóstico
Execute estes comandos e me informe os resultados:

```bash
# 1. Verificar profiles
aws configure list-profiles

# 2. Verificar configuração atual
aws configure list

# 3. Verificar cache SSO
ls ~/.aws/sso/cache/

# 4. Tentar diferentes profiles
aws sts get-caller-identity --profile default
aws sts get-caller-identity --profile amazonq-pro

# 5. Verificar região
aws configure get region
```

## 🚀 Scripts de Correção

### Script 1: Limpeza Completa
```bash
# Logout de todos os SSO
aws sso logout

# Limpar cache
rm -rf ~/.aws/sso/cache/*

# Relogin
aws sso login
```

### Script 2: Reconfiguração SSO
```bash
# Backup configuração atual
cp ~/.aws/config ~/.aws/config.backup

# Reconfigurar SSO
aws configure sso --profile default
```

### Script 3: Teste de Permissões
```bash
# Testar serviços específicos
aws s3 ls
aws route53 list-hosted-zones
aws cloudfront list-distributions
aws acm list-certificates --region us-east-1
```

## 📋 Checklist de Resolução

### Pré-Diagnóstico
- [ ] Consegue acessar console AWS via browser?
- [ ] Vê os recursos AWS no console?
- [ ] Tem permissões de administrador?

### Testes de Acesso
- [ ] `aws sts get-caller-identity` funciona?
- [ ] `aws s3 ls` funciona?
- [ ] `aws configure list` mostra configuração?

### Soluções Aplicadas
- [ ] Tentou logout/login SSO
- [ ] Limpou cache SSO
- [ ] Testou profiles diferentes
- [ ] Criou access keys (se necessário)

## 🎯 Próximos Passos Baseados no Resultado

### Se Resolver o Acesso
1. **Executar** comandos de verificação
2. **Mapear** infraestrutura existente
3. **Proceder** com implementação multi-domínio

### Se Não Resolver
1. **Usar console manual** para verificação
2. **Documentar** recursos existentes
3. **Implementar** via console web

## 📞 Suporte Adicional

### Informações Necessárias
Para ajudar melhor, preciso saber:

1. **Consegue acessar console AWS?** (Sim/Não)
2. **Vê recursos no console?** (S3, Route53, etc.)
3. **Resultado dos comandos de diagnóstico**
4. **Mensagens de erro específicas**

### Contato AWS Support
Se nada funcionar:
- **AWS Support Center**
- **Documentação SSO:** https://docs.aws.amazon.com/singlesignon/
- **Troubleshooting:** https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html

---

**Próximo Passo:** Execute os comandos de diagnóstico e me informe os resultados para identificarmos a causa exata do problema.