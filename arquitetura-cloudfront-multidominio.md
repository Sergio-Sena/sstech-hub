# Arquitetura CloudFront Multi-Domínio

## Arquitetura Resumida

**Distribuição Principal:** 1 (Amazon CloudFront)  
**Domínios:** N domínios/subdomínios diferentes (ex: seuhub.com, projetoA.com)  
**Origens (Origins):** N origens diferentes (ex: S3 Bucket do Hub, S3 Bucket do Projeto A)  
**Segurança:** HTTPS (ACM) + Acesso Restrito ao S3 (OAC)

## Fases de Execução

### FASE 1: Configuração de Pré-requisitos e Domínios

| Passo | Serviço | Ação | Detalhe Crucial |
|-------|---------|------|-----------------|
| 1.1 | Route 53 | Verificação/Registro de Domínios | Garanta que todos os domínios (seuhub.com, projetoA.com, etc.) estejam registrados e com a Zona Hospedada configurada no Route 53. |
| 1.2 | S3 | Criação dos Buckets | Crie um bucket para cada projeto (ex: seuhub-content, projeto-a-content). Desative o Public Access nestes buckets. |
| 1.3 | S3 | Configuração de Hospedagem Estática | Para cada bucket, em Propriedades, ative Static website hosting e defina o Index document (index.html). |
| 1.4 | ACM | Criação do Certificado SSL | Acesse a região N. Virginia (us-east-1). Solicite um certificado para TODOS os seus domínios (incluindo www. se desejar). Use o método Validação de DNS e crie os registros necessários no Route 53. |
| 1.5 | S3 | Upload de Conteúdo | Faça o upload dos arquivos index.html e demais ativos para os respectivos S3 Buckets. |

### FASE 2: Criação e Conexão do CDN Central

| Passo | Serviço | Ação | Detalhe Crucial |
|-------|---------|------|-----------------|
| 2.1 | CloudFront | Criação da Distribuição | Crie UMA ÚNICA distribuição web. |
| 2.2 | CloudFront | Adicionar Origens (Origins) | Adicione cada S3 Bucket criado (Hub e Projetos) como uma Origin na distribuição. |
| 2.3 | CloudFront & S3 | Configurar OAC (Origin Access Control) | Ao adicionar o Origin S3, o CloudFront solicitará um OAC. Crie um OAC para cada Origin. O CloudFront fornecerá uma Bucket Policy (Política de Acesso). COPIE e cole essa política na aba Permissions de cada S3 Bucket correspondente. |
| 2.4 | CloudFront | Configurar Domínios Alternativos (CNAMEs) | Em Settings, no campo Alternate Domain Names (CNAMEs), liste TODOS os seus domínios (seuhub.com, projetoA.com, etc.). |
| 2.5 | CloudFront | Associar SSL/TLS | Em Custom SSL Certificate, selecione o certificado multi-domínio criado no ACM (Passo 1.4). |
| 2.6 | CloudFront | Configurar o Default Behavior | Defina o Origin do Hub (seuhub-content) como o Origin Padrão (Default Cache Behavior). |
| 2.7 | CloudFront | Aguardar Deploy | Aguarde a distribuição mudar o status para Deployed. |

### FASE 3: Roteamento e Ativação do Acesso Direto (CNAMEs)

Esta fase garante que a mesma distribuição CloudFront possa servir domínios diferentes.

| Passo | Serviço | Ação | Detalhe Crucial |
|-------|---------|------|-----------------|
| 3.1 | CloudFront | Obter Domain Name | Copie o Domain Name da sua distribuição (ex: d123456abcdef.cloudfront.net). |
| 3.2 | Route 53 | Criação de Registros ALIAS (CNAME) | Para CADA DOMÍNIO (Hub e Projetos): |
| 3.3 | Route 53 | Registro do Hub | Crie um registro A (Alias) para seuhub.com apontando para o Domain Name do CloudFront. |
| 3.4 | Route 53 | Registro do Projeto A | Crie um registro A (Alias) para projetoA.com apontando para o MESMO Domain Name do CloudFront. |
| ... | Route 53 | Outros Projetos | Repita o Passo 3.4 para todos os outros domínios de projetos. |

### FASE 4: Verificação Final e Conclusão

| Passo | Ação | Cenário Testado | Resultado Esperado |
|-------|------|-----------------|-------------------|
| 4.1 | Acessar https://seuhub.com | Roteamento do Hub | Carrega o index.html do Hub. |
| 4.2 | Acessar https://projetoA.com | Acesso Direto do Projeto | Carrega o index.html do Projeto A. |
| 4.3 | Acessar o S3 diretamente | Segurança (OAC) | Deve retornar 403 Forbidden ou Access Denied. |
| 4.4 | Navegar via Hub | Experiência Centralizada | Clicar em um link no Hub deve levar o usuário para o domínio respectivo do projeto. |

## 🛑 Regra de Ouro da Arquitetura

**Para o Agente de IA:** A chave para esta arquitetura é a repetição da ligação DNS. Todos os domínios (seuhub.com, projetoA.com, etc.) devem ser configurados no Route 53 como ALIAS Records que apontam para o MESMO Domain Name do CloudFront. O CloudFront usará o nome do host na requisição (ex: projetoA.com) para buscar o conteúdo na Origin correta.