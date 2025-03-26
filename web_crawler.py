import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://br.ebay.com/b/Jordan-12-Retro-Brilliant-Orange-W/95672/bn_7119137189'  # Substitua pela URL real

# Adicionando um cabeçalho com um User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Fazer a requisição HTTP com cabeçalhos
response = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    for item in soup.find_all('h2'):  # Substitua pela tag que deseja extrair
        data.append(item.get_text())

    df = pd.DataFrame(data, columns=['Title'])
    print(df)
    df.to_csv('scraped_data.csv', index=False)
else:
    print(f'Erro ao acessar o site. Status code: {response.status_code}')
