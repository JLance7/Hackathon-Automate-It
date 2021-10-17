import requests
import traceback
from bs4 import BeautifulSoup

num_of_articles = 2


titles = []
links = []
article_text = []

#globa variables
title = None


def getNews(url):
    r1 = requests.get(url)
    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, 'html5lib')
    
    if url == "https://www.nbcnews.com/":
        print('\nGoing into 1\n')
        title_content = soup1.find_all('span', class_='tease-card__headline')
        link_content = soup1.find_all('h2', class_='tease-card__headline tease-card__title relative')
    elif url == "https://www.cnn.com/":
        print('\nGoing into 2\n')
        title_content = soup1.find_all('h3', class_='cd__headline')
        link_content = soup1.find_all('h3', class_='cd__headline')
    else:
        print('\nGoing into 3\n')
        title_content = soup1.find_all('h2', class_='title title-color-default')
        # print()
        # print(title_content)
        # print()
        link_content = soup1.find_all('h2', class_='title title-color-default')
    
        
    for i in range(0, num_of_articles):
        try:
            #get titles
            if url == 'https://www.foxnews.com/':
                title = title_content[i].get_text()
            else:
                title = title_content[i].get_text()
            titles.append(title)
            print('GOT HERE')
            print('wooo')
            print(titles)
            print('woo')
            #get links
            link = link_content[i].find('a')['href']
            links.append(link)
            #get articles
            article = requests.get(link)
            article_con = article.content
            soup_article = BeautifulSoup(article_con, 'html5lib')
            if url == 'https://www.nbcnews.com/':
                body = soup_article.find_all('div', class_='article-body__content')
            elif url == 'https://www.cnn.com':
                body = soup_article.find_all('div', class_='l-container')
            else:
                body = soup_article.find_all('div', class_='article-content-wrap sticky-columns')
            x = body[0].find_all('p')

            # Unifying the paragraphs
            list_paragraphs = []
            for p in range(0, 5):
                paragraph = x[p].get_text()
                list_paragraphs.append(paragraph)
                final_article = " ".join(list_paragraphs)

            
            article_text.append(final_article)
        except:
            traceback.print_exc()
            continue

def getLinks():
    return links

def getTitles():
    return titles

def getArticleText():
    return article_text

def setNumOfArticles(num):
    num_of_articles = num


