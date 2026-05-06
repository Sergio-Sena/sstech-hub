# Deploy Hub → CDN Unificado
$bucket = "sstech-cdn-unified"
$prefix = "hub"
$distributionId = "E9ZQJ3RPSA04N"

Write-Host "=== Deploy Hub para CDN Unificado ===" -ForegroundColor Cyan

Write-Host "Sincronizando arquivos..." -ForegroundColor Yellow
aws s3 sync . s3://$bucket/$prefix/ `
  --exclude ".git/*" `
  --exclude "*.md" `
  --exclude "*.py" `
  --exclude "*.json" `
  --exclude "_archive/*" `
  --exclude "scripts/*" `
  --exclude "docs/*" `
  --include "index.html" `
  --include "script.js" `
  --include "styles.css" `
  --include "src/*" `
  --cache-control "public, max-age=3600"

Write-Host "Invalidando cache..." -ForegroundColor Yellow
aws cloudfront create-invalidation --distribution-id $distributionId --paths "/$prefix/*"

Write-Host "Deploy concluido!" -ForegroundColor Green
Write-Host "URL: https://hub.sstechnologies-cloud.com" -ForegroundColor Cyan
