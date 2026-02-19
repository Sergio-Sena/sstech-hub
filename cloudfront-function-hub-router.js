function handler(event) {
    var request = event.request;
    var uri = request.uri;
    
    // Roteamento para projetos específicos
    if (uri.startsWith('/portfolio')) {
        // Portfolio Sérgio Sena
        if (uri === '/portfolio' || uri === '/portfolio/') {
            request.uri = '/portfolio/index.html';
        }
    } else if (uri.startsWith('/aws-services')) {
        // AWS Services Dashboard
        if (uri === '/aws-services' || uri === '/aws-services/') {
            request.uri = '/aws-services/index.html';
        }
    } else if (uri.startsWith('/financas')) {
        // Finanças Pessoais
        if (uri === '/financas' || uri === '/financas/') {
            request.uri = '/financas/index.html';
        }
    } else if (uri.startsWith('/automacao')) {
        // Automação de Sistemas
        if (uri === '/automacao' || uri === '/automacao/') {
            request.uri = '/automacao/index.html';
        }
    } else if (uri === '/' || uri === '') {
        // Página inicial do hub
        request.uri = '/index.html';
    }
    
    // Adicionar .html para arquivos sem extensão
    if (!uri.includes('.') && !uri.endsWith('/')) {
        request.uri = uri + '.html';
    }
    
    return request;
}