# 🔍 Verificação da Infraestrutura AWS Existente

## 📋 Scripts de Verificação

### 1. Verificar Domínios no Route 53
```bash
# Listar todas as hosted zones
aws route53 list-hosted-zones --query 'HostedZones[*].[Name,Id]' --output table

# Verificar domínios específicos
aws route53 list-hosted-zones --query 'HostedZones[?contains(Name, `sshub`) || contains(Name, `dev-cloud`) || contains(Name, `sstechnologies-cloud`)]'
```

### 2. Verificar Buckets S3
```bash
# Listar todos os buckets
aws s3 ls

# Verificar buckets relacionados aos projetos
aws s3 ls | grep -E "(sshub|dev-cloud|sstechnologies)"

# Verificar configuração de website hosting
aws s3api get-bucket-website --bucket BUCKET_NAME
```

### 3. Verificar Certificados SSL (ACM)
```bash
# Listar certificados na região us-east-1 (CloudFront)
aws acm list-certificates --region us-east-1 --query 'CertificateSummaryList[*].[DomainName,CertificateArn,Status]' --output table

# Verificar certificados em outras regiões
aws acm list-certificates --region us-east-2 --query 'CertificateSummaryList[*].[DomainName,CertificateArn,Status]' --output table
```

### 4. Verificar Distribuições CloudFront
```bash
# Listar todas as distribuições
aws cloudfront list-distributions --query 'DistributionList.Items[*].[Id,DomainName,Status,Comment]' --output table

# Verificar CNAMEs configurados
aws cloudfront list-distributions --query 'DistributionList.Items[*].[Id,Aliases.Items[*]]' --output table
```

### 5. Verificar Registros DNS Específicos
```bash
# Verificar registros para domínios específicos (substitua HOSTED_ZONE_ID)
aws route53 list-resource-record-sets --hosted-zone-id HOSTED_ZONE_ID --query 'ResourceRecordSets[?Type==`A` || Type==`CNAME`]'
```

## 📊 Checklist de Verificação

### Domínios Route 53
- [ ] `sshub.com` - Hosted Zone ID: ___________
- [ ] `dev-cloud.com` - Hosted Zone ID: ___________
- [ ] `sstechnologies-cloud.com` - Hosted Zone ID: ___________

### Buckets S3
- [ ] Bucket para SStech Hub: ___________
- [ ] Bucket para Portfolio: ___________
- [ ] Website hosting habilitado: Sim/Não
- [ ] Public access bloqueado: Sim/Não

### Certificados SSL
- [ ] Certificado multi-domínio existente: ___________
- [ ] Região: us-east-1 (obrigatório para CloudFront)
- [ ] Status: Issued/Pending/Failed
- [ ] Domínios incluídos: ___________

### CloudFront
- [ ] Distribuição existente: ___________
- [ ] CNAMEs configurados: ___________
- [ ] Origins configuradas: ___________
- [ ] Status: Deployed/InProgress

### DNS Records
- [ ] `sshub.com` aponta para: ___________
- [ ] `dev-cloud.com` aponta para: ___________
- [ ] Tipo de registro: A (Alias) / CNAME

## 🎯 Próximos Passos Baseados no Resultado

### Cenário 1: Tudo Existe (Apenas Ajustar)
Se já existe:
- ✅ Domínios registrados
- ✅ Buckets S3 configurados
- ✅ Certificado SSL válido
- ✅ CloudFront funcionando

**Ação:** Apenas ajustar configurações existentes

### Cenário 2: Parcialmente Configurado
Se existe parcialmente:
- ✅ Alguns recursos criados
- ❌ Alguns recursos faltando

**Ação:** Completar configuração faltante

### Cenário 3: Começar do Zero
Se não existe:
- ❌ Recursos não criados

**Ação:** Seguir plano de implementação completo

## 📝 Template de Resultado

Preencha após executar os comandos:

```
=== INFRAESTRUTURA AWS ATUAL ===

DOMÍNIOS ROUTE 53:
- sshub.com: [EXISTE/NÃO EXISTE] - Zone ID: _______
- dev-cloud.com: [EXISTE/NÃO EXISTE] - Zone ID: _______

BUCKETS S3:
- SStech Hub: [NOME DO BUCKET] - Website: [SIM/NÃO]
- Portfolio: [NOME DO BUCKET] - Website: [SIM/NÃO]

CERTIFICADOS SSL:
- Multi-domínio: [ARN DO CERTIFICADO] - Status: [STATUS]
- Região: [us-east-1/OUTRA]

CLOUDFRONT:
- Distribuição: [ID DA DISTRIBUIÇÃO] - Status: [STATUS]
- CNAMEs: [LISTA DE CNAMES]

DNS RECORDS:
- sshub.com → [DESTINO ATUAL]
- dev-cloud.com → [DESTINO ATUAL]

CONCLUSÃO:
[CENÁRIO 1/2/3] - [AÇÕES NECESSÁRIAS]
```

## 🚀 Comandos Rápidos de Verificação

Execute estes comandos e cole os resultados:

```bash
# Verificação rápida completa
echo "=== HOSTED ZONES ==="
aws route53 list-hosted-zones --query 'HostedZones[*].[Name,Id]' --output table

echo "=== BUCKETS S3 ==="
aws s3 ls

echo "=== CERTIFICADOS SSL ==="
aws acm list-certificates --region us-east-1 --query 'CertificateSummaryList[*].[DomainName,Status]' --output table

echo "=== CLOUDFRONT ==="
aws cloudfront list-distributions --query 'DistributionList.Items[*].[Id,Status,Comment]' --output table

echo "=== VERIFICAÇÃO COMPLETA ==="
```

---

**Próximo Passo:** Execute os comandos de verificação e compartilhe os resultados para definirmos a estratégia de implementação.