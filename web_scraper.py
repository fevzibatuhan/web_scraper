import requests
from bs4 import BeautifulSoup

url = input("Web sayfasını giriniz ('https://example.com'):") # Veri toplanacak web sayfasının URL'si

response = requests.get(url) # Web sayfasını almak için GET isteği yapılır

soup = BeautifulSoup(response.text, 'html.parser') # Web sayfasının içeriği BeautifulSoup ile parse edilir

basliklar = soup.find_all('h1') # Tüm başlıkları bul

print("\n--- BAŞLIKLAR ---")
for baslik in basliklar: # Her başlığı ekrana yazdır
    print(baslik.text)

paragraflar = soup.find_all('p') # Tüm paragraf içeriklerini bul

print("\n--- PARAGRAFLAR ---")
for paragraf in paragraflar: # Her paragraf içeriğini ekrana yazdır
    print(paragraf.text)

linkler = soup.find_all('a') # Tüm bağlantıları (linkleri) bul

print("\n--- BAĞLANTILAR ---")
for link in linkler: # Her bağlantıyı ekrana yazdır
    print(link.get('href'))
