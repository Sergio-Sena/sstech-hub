# 🧪 Testes CloudFront Centralizado

## 📊 **Distribuição de Teste:**
- **ID**: E9ZQJ3RPSA04N
- **Domain**: d10mjoe1zes9j1.cloudfront.net
- **Status**: Aguardando deploy (5-15 min)

## 🎯 **Testes a Realizar:**

### **1. Teste Default (Hub):**
```bash
curl -I https://d10mjoe1zes9j1.cloudfront.net
# Deve carregar: Hub (hub-origin)
```

### **2. Teste com Host Header (Simulação):**
```bash
# Simular dev-cloud.sstechnologies-cloud.com
curl -I https://d10mjoe1zes9j1.cloudfront.net -H "Host: dev-cloud.sstechnologies-cloud.com"
# Deve carregar: Portfolio (portfolio-origin)

# Simular ritech-fechaduras-digitais.sstechnologies-cloud.com  
curl -I https://d10mjoe1zes9j1.cloudfront.net -H "Host: ritech-fechaduras-digitais.sstechnologies-cloud.com"
# Deve carregar: Ritech (ritech-origin)
```

### **3. Verificar Origins:**
- ✅ hub-origin → hub.sstechnologies-cloud.com.s3
- ✅ portfolio-origin → portfolio-sergio-sena.s3
- ✅ aws-services-origin → aws-services-dashboard-prod.s3
- ✅ ritech-origin → ritech-fechaduras-site.s3
- ✅ trafego-origin → ssgestaodetrafego.s3
- ✅ midiaflow-origin → mediaflow-frontend-969430605054.s3-website

## ⏱️ **Aguardar Deploy:**
```bash
# Verificar status
aws cloudfront get-distribution --id E9ZQJ3RPSA04N --profile deploy --query "Distribution.Status"
```

## 🎯 **Após Validação:**
1. ✅ **Adicionar CNAMEs** à distribuição
2. ✅ **Migrar DNS** um domínio por vez
3. ✅ **Remover distribuições antigas**
4. ✅ **Confirmar economia**

---
**Próximo Passo**: Aguardar deploy e executar testes