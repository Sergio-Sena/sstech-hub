# 🗑️ Recursos AWS Não Utilizados - Análise para Remoção

## 📊 **CloudFront Distributions:**

### ❌ **Para Remover (Não Utilizadas):**

1. **E3ODIUY4LXU8TH** - Mediaflow v4.1 (DISABLED)
   - Status: Desabilitada
   - Motivo: Versão antiga do Mídiaflow
   - **REMOVER**: ✅

2. **E12GJ6BBJXZML5** - Mediaflow v4.1 (DISABLED)  
   - Status: Desabilitada
   - Motivo: Versão antiga do Mídiaflow
   - **REMOVER**: ✅

3. **EW17MMXFBIMW6** - AWS Certification Platform
   - Domínio: `aws-certification-platform.sstechnologies-cloud.com`
   - Motivo: Removido do hub, não mais utilizado
   - **REMOVER**: ✅

4. **E26AJFZZPE428D** - DVA-C02 Course Distribution
   - Sem domínio customizado
   - Motivo: Não está no hub, parece ser teste
   - **AVALIAR**: ⚠️

### ✅ **Manter (Em Uso):**
- E20VPG27E02V7M - Hub ✅
- E23SOSSVGQ2NOD - Portfolio ✅  
- E1U10Q11WGDP01 - AWS Services ✅
- E2PT7P40RJBK38 - Ritech ✅
- E32SZD5BCOGZDM - Gestão Tráfego ✅
- E2HZKZ9ZJK18IU - Mídiaflow ✅
- E233IHQWZDF2M2 - Finanças ✅
- E1R9CQH6OLDP6F - Kate Kuray (independente) ✅

## 📦 **S3 Buckets:**

### ❌ **Para Remover (Não Utilizados):**

1. **automacao-video** - Projeto antigo
2. **aws-cert-platform-2025** - Certificação removida do hub
3. **docs.sena** - Documentação antiga (2023)
4. **midia-devaria** - Projeto Devaria antigo
5. **pics-notebackup** - Backup de fotos (2023)
6. **smarthophone** - Projeto antigo (2023)
7. **xioami-mi6** - Projeto antigo (2024)

### ⚠️ **Avaliar (Podem ser Backup/Importantes):**

1. **aws-services-api-prod-serverlessdeploymentbucket-6etypbqdiskf** - Serverless Framework
2. **serverless-framework-deployments-us-east-1-63d30e2f-ee28** - Serverless Framework
3. **midiaflow-backups-969430605054** - Backups do Mídiaflow

### ✅ **Manter (Em Uso):**
- hub.sstechnologies-cloud.com ✅
- portfolio-sergio-sena ✅
- aws-services-dashboard-prod ✅
- ritech-fechaduras-site ✅
- ssgestaodetrafego ✅
- financaspessoais.sstechnologies-cloud.com ✅
- kate-kuray-portfolio-20250915 ✅
- dva-c02-course-prod ✅
- mediaflow-frontend-969430605054 ✅
- mediaflow-processed-969430605054 ✅
- mediaflow-uploads-969430605054 ✅

## 💰 **Economia Estimada:**

### **CloudFront (3-4 distribuições):**
- **Economia**: $3-4/mês
- **Requests**: Redução significativa

### **S3 Buckets (7 buckets):**
- **Storage**: ~$2-5/mês (dependendo do conteúdo)
- **Requests**: Redução de custos

### **Total Estimado**: $5-10/mês de economia

## 🎯 **Plano de Remoção:**

### **FASE 1 - CloudFront (Seguro):**
1. E3ODIUY4LXU8TH (Mediaflow v4.1 - DISABLED)
2. E12GJ6BBJXZML5 (Mediaflow v4.1 - DISABLED)
3. EW17MMXFBIMW6 (AWS Certification Platform)

### **FASE 2 - S3 Buckets Antigos:**
1. automacao-video
2. docs.sena  
3. pics-notebackup
4. smarthophone
5. xioami-mi6

### **FASE 3 - Avaliar:**
1. E26AJFZZPE428D (DVA-C02 Course)
2. aws-cert-platform-2025
3. midia-devaria

## ⚠️ **IMPORTANTE - Backup Antes da Remoção:**

### **Verificar Conteúdo Importante:**
```bash
# Verificar tamanho e conteúdo dos buckets antes de remover
aws s3 ls s3://bucket-name --recursive --human-readable --summarize
```

### **Fazer Backup se Necessário:**
```bash
# Download de backup antes da remoção
aws s3 sync s3://bucket-name ./backup/bucket-name/
```

## 🚀 **Próximos Passos:**

1. **Confirmar remoção** dos recursos identificados
2. **Executar FASE 1** (CloudFront - sem risco)
3. **Verificar conteúdo** dos buckets S3
4. **Executar FASE 2** (S3 buckets antigos)
5. **Monitorar economia** de custos

---

**Economia Total Estimada**: $5-10/mês
**Risco**: Baixo (recursos já identificados como não utilizados)
**Tempo**: 30-60 minutos para execução completa