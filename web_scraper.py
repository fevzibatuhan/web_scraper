import requests
from bs4 import BeautifulSoup

url = input("Web sayfasını giriniz ('https://example.com'):") # Veri toplanacak web sayfasının URL'si

response = requests.get(url) # Web sayfasını almak için GET isteği yapılır

soup = BeautifulSoup(response.text, 'html.parser') # Web sayfasının içeriği BeautifulSoup ile parse edilir

while True:
    print("\n--- Başlıklar ---")
    for baslik in basliklar: # Her başlığı ekrana yazdır
        print(baslik.text)

    paragraflar = soup.find_all('p') # Tüm paragraf içeriklerini bul

    print("\n--- Paragraflar ---")
    for paragraf in paragraflar: # Her paragraf içeriğini ekrana yazdır
        print(paragraf.text)

    linkler = soup.find_all('a') # Tüm bağlantıları (linkleri) bul

    print("\n--- Bağlantılar ---")
    for link in linkler: # Her bağlantıyı ekrana yazdır
        print(link.get('href'))

    cikis = input("Çıkış yapmak için 'x' tuşuna bas: ")
    
    if cikis == ord('q') or key == ord('x'):
        break

