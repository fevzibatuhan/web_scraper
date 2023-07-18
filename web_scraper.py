import requests

from bs4 import BeautifulSoup


url = 'https://example.com' # Veri toplanacak web sayfasının URL'si

response = requests.get(url) # Web sayfasını almak için GET isteği yapılır

soup = BeautifulSoup(response.text, 'html.parser') # Web sayfasının içeriği BeautifulSoup ile parse edilir

basliklar = soup.find_all('h1') # Tüm başlıkları bul

for baslik in basliklar: # Her başlığı ekrana yazdır
    print(baslik.text)
