# Teste CloudFront Functions - SStech Hub

## Status do Teste
- **Data**: 15/12/2024 19:18
- **Distribuição**: E9ZQJ3RPSA04N (Status: InProgress)
- **Função**: sstech-host-router (Status: LIVE)

## Configuração Implementada

### CloudFront Function
```javascript
function handler(event) {
    var request = event.request;
    var host = request.headers.host.value;
    
    // Roteamento simples baseado no host
    if (host === 'v2-portfolio.sstechnologies-cloud.com') {
        request.uri = '/portfolio' + request.uri;
    } else if (host === 'v2-aws-services.sstechnologies-cloud.com') {
        request.uri = '/aws-services' + request.uri;
    } else if (host === 'v2-ritech.sstechnologies-cloud.com') {
        request.uri = '/ritech' + request.uri;
    }
    
    return request;
}
```

### Domínios de Teste
- v2-hub.sstechnologies-cloud.com (padrão - hub-origin)
- v2-portfolio.sstechnologies-cloud.com (modifica URI para /portfolio)
- v2-aws-services.sstechnologies-cloud.com (modifica URI para /aws-services)

## Limitações Identificadas
1. **CloudFront Functions** só funciona com `viewer-request` e `viewer-response`
2. Não pode modificar o origin dinamicamente
3. Solução atual modifica apenas o URI path

## Próximos Passos
1. Aguardar deploy da distribuição (~5-10 min)
2. Testar URLs de teste
3. Se funcionar, considerar estrutura de pastas nos buckets S3
4. Avaliar se vale a pena vs arquitetura distribuída atual

## Arquitetura Atual (Funcional)
- 8 distribuições separadas
- Custo: ~$8-15/mês
- Simplicidade de manutenção

## Arquitetura Centralizada (Teste)
- 1 distribuição com múltiplos origins
- Economia potencial: ~$5-8/mês
- Complexidade adicional de roteamento