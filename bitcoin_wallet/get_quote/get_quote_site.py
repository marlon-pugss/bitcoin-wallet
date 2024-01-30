import requests
from bs4 import BeautifulSoup

class Site:
    def __init__(self):
        pass

    def get_quote(self):
        url = 'https://br.investing.com/crypto/bitcoin/btc-brl'
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
        }
        page = requests.get(url, headers=headers)

        if page.status_code == 200:
            soup = BeautifulSoup(page.text, 'html.parser')
            print(soup.prettify())

        else:
            print(f"Erro ao obter a página. Código de status: {page.status_code}")

site = Site()
site.get_quote()
