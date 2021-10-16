import requests
from bs4 import BeautifulSoup

titles = []
text = []
urls = []

url = "https://www.nbcnews.com/"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
titles = soup1.find_all('span', class_='tease-card__headline')
for title in titles:
    title = title.get_text()
    print(title)
    print()
