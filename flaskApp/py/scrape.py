import requests
from bs4 import BeautifulSoup

num_of_articles = 2
url = "https://www.nbcnews.com/"

titles = []
links = []
article_text = []

r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
title_content = soup1.find_all('span', class_='tease-card__headline')
article_content = soup1.find_all('div', class_='article-body__content')
link_content = soup1.find_all('h2', class_='tease-card__headline tease-card__title relative')

def getNews():
    for i in range(0, num_of_articles):
        #get titles
        title = title_content[i].get_text()
        titles.append(title)
        #get links
        link = link_content[i].find('a')['href']
        links.append(link)
        #get articles
        article = requests.get(link)
        article_con = article.content
        soup_article = BeautifulSoup(article_con, 'html5lib')
        body = soup_article.find_all('div', class_='article-body__content')
        x = body[0].find_all('p')

        # Unifying the paragraphs
        list_paragraphs = []
        for p in range(0, len(x)):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
            final_article = " ".join(list_paragraphs)
            
        article_text.append(final_article)

def getLinks():
    return links

def getTitles():
    return titles

def getText():
    return article_content




