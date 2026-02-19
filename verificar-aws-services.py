import requests

url = "https://aws-services.sstechnologies-cloud.com"
response = requests.get(url)

print(f"URL: {url}")
print(f"Status: {response.status_code}\n")

if response.status_code == 200:
    # Extrair título
    if "<title>" in response.text:
        start = response.text.find("<title>") + 7
        end = response.text.find("</title>")
        title = response.text[start:end]
        print(f"Titulo: {title}")
    
    # Extrair h1
    if "<h1>" in response.text:
        start = response.text.find("<h1>") + 4
        end = response.text.find("</h1>")
        h1 = response.text[start:end]
        print(f"H1: {h1}")
    
    print(f"\nConteudo: {response.text[:500]}")
