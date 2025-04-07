# 🕷️ Web Crawler para Produtos no eBay

Este projeto é um simples web crawler desenvolvido em Python que coleta títulos de produtos de uma página do eBay e os salva em um arquivo `.csv`.

## 📌 Objetivo

Extrair dados relevantes de produtos (como títulos) de páginas do eBay para análises, comparações de preços ou estudos de mercado.

## 🧰 Tecnologias Utilizadas

- Python 3
- [requests](https://docs.python-requests.org/)
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)
- [pandas](https://pandas.pydata.org/)

## 🚀 Como Executar

1. **Clone o repositório (ou copie o script)**

2. **Instale as dependências:**
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

3. **Execute o script:**
   ```bash
   python web_crawler.py
   ```

4. O script irá gerar um arquivo `scraped_data.csv` com os títulos extraídos.

## 📁 Estrutura do Projeto

```
├── web_crawler.py          # Script principal para scraping
├── scraped_data.csv        # Arquivo de saída com os dados coletados
└── README.md               # Este arquivo
```

## ⚠️ Observações

- A tag HTML buscada atualmente é `<h2>`, o que pode variar conforme a estrutura da página. Adapte o seletor para obter os dados desejados.
- O script utiliza um cabeçalho de User-Agent para evitar bloqueios simples de scraping.
- URLs diferentes do eBay podem exigir ajustes nos seletores HTML.

## 📌 Exemplo de Uso

Página alvo:  
`https://br.ebay.com/b/Jordan-12-Retro-Brilliant-Orange-W/95672/bn_7119137189`

O crawler extrai os títulos de produtos disponíveis nesta página.

## 📬 Contato

https://digitalquanta.com.br

