# Divisão Prática - Hub SStech

## DENTRO DO HUB (CloudFront Behaviors)
**hub.sstechnologies-cloud.com**

### ✅ Projetos Integrados (4 projetos)
1. **Portfolio Sérgio Sena** - `/portfolio/*`
   - Origin: dev-cloud.sstechnologies-cloud.com (mantém bucket)
   - Acesso: hub.sstechnologies-cloud.com/portfolio/

2. **AWS Services Dashboard** - `/aws-services/*`
   - Origin: aws-services.sstechnologies-cloud.com (mantém bucket)
   - Acesso: hub.sstechnologies-cloud.com/aws-services/

3. **Finanças Pessoais** - `/financas/*`
   - Origin: financaspessoais.sstechnologies-cloud.com (mantém bucket)
   - Acesso: hub.sstechnologies-cloud.com/financas/

4. **Automação de Sistemas** - `/automacao/*`
   - Origin: automacao-sstechnologies-cloud.com (novo bucket)
   - Acesso: hub.sstechnologies-cloud.com/automacao/

## FORA DO HUB (CDNs Independentes)
**Mantêm CDNs próprios**

### ❌ Projetos Independentes (5 projetos)
1. **Ritech Fechaduras** 
   - ritech-fechaduras-digitais.sstechnologies-cloud.com
   - *Razão: Produto comercial independente*

2. **Gestão de Tráfego**
   - sstrafegopago.sstechnologies-cloud.com  
   - *Razão: Sistema específico de cliente*

3. **Mídiaflow**
   - midiaflow.sstechnologies-cloud.com
   - *Razão: Produto SaaS independente*

4. **Site Corporativo STGBR**
   - Atual: dentro do portfolio
   - *Razão: Projeto cliente específico*

5. **Base Imóveis**
   - Atual: dentro do portfolio
   - *Razão: Projeto cliente específico*

## ESTRATÉGIA DE MIGRAÇÃO

### 🚀 FASE 1 - Validação (4 projetos no hub)
- Implementar os 4 projetos iniciais
- Testar performance e funcionalidade
- Validar economia de custos

### 📈 FASE 2 - Expansão (após validação)
Se a Fase 1 funcionar bem, migrar para o hub:

6. **Site Corporativo STGBR** - `/stgbr/`
   - Atual: dentro do portfolio
   - Novo: hub.sstechnologies-cloud.com/stgbr/

7. **Base Imóveis** - `/base-imoveis/`
   - Atual: dentro do portfolio  
   - Novo: hub.sstechnologies-cloud.com/base-imoveis/

### ⚖️ PROJETOS QUE FICAM INDEPENDENTES
- **Ritech Fechaduras** (produto comercial)
- **Gestão de Tráfego** (sistema de cliente)
- **Mídiaflow** (SaaS independente)

## RESULTADO FINAL
- **CDNs Atuais**: 8 distribuições
- **CDNs Fase 1**: 6 distribuições (Hub + 5 independentes)
- **CDNs Fase 2**: 4 distribuições (Hub + 3 independentes)
- **Economia Final**: 50% dos custos CDN
- **Estrutura**: Hub com projetos relacionados + produtos independentes