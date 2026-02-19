function handler(event) {
    var request = event.request;
    var host = request.headers.host.value;
    
    // Mapeamento de hosts para origins
    var originMapping = {
        'v2-hub.sstechnologies-cloud.com': 'hub-origin',
        'v2-portfolio.sstechnologies-cloud.com': 'portfolio-origin', 
        'v2-aws-services.sstechnologies-cloud.com': 'aws-services-origin',
        'v2-ritech.sstechnologies-cloud.com': 'ritech-origin',
        'v2-gestao-trafego.sstechnologies-cloud.com': 'gestao-trafego-origin',
        'v2-automacao.sstechnologies-cloud.com': 'automacao-origin'
    };
    
    // Define o origin baseado no host
    var targetOrigin = originMapping[host];
    if (targetOrigin) {
        request.origin = {
            s3: {
                domainName: getS3Domain(targetOrigin),
                region: 'us-east-1',
                authMethod: 'origin-access-control',
                path: ''
            }
        };
    }
    
    return request;
}

function getS3Domain(origin) {
    var s3Mapping = {
        'hub-origin': 'hub.sstechnologies-cloud.com.s3.us-east-1.amazonaws.com',
        'portfolio-origin': 'dev-cloud.sstechnologies-cloud.com.s3.us-east-1.amazonaws.com',
        'aws-services-origin': 'aws-services.sstechnologies-cloud.com.s3.us-east-1.amazonaws.com',
        'ritech-origin': 'ritech-fechaduras-digitais.sstechnologies-cloud.com.s3.us-east-1.amazonaws.com',
        'gestao-trafego-origin': 'ss-gestao-de-trafego.sstechnologies-cloud.com.s3.us-east-1.amazonaws.com',
        'automacao-origin': 'automacao-sistemas.sstechnologies-cloud.com.s3.us-east-1.amazonaws.com'
    };
    return s3Mapping[origin];
}