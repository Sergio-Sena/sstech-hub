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