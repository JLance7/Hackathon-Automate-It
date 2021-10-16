#flask website app for displaying reliable news from newsGrabber file
from flask import Flask, redirect, url_for, render_template
from scrape import *
import time
#from newsGrabber import *
links = []
titles = []
texts = []

app = Flask(__name__)
app = Flask(__name__, static_folder='../static', template_folder='../html')

#if no subdirectory url is given show reliable news (index.html)
@app.route("/")
def home():
    try:
        return render_template("index.html", page="Reliable News", list1=titles)
    except:
        print('\nerror in home\n')

#any other subdirectory url given
#if no subdirectory url is given show reliable news (index.html)
@app.route("/")
def other():
    try:
        return redirect(url_for("first_page"))
    except:
        print('\nerror in other func\n')

#reliable-news subdirectory url
@app.route("/reliable-news/")
def first_page():
    try:
        return render_template("index.html", page="Reliable News", list1=links, list2=titles, list3=texts, num=len(links))
    except:
        print('\nerror in first_page func\n')

#unreliable-news subdirectory url
@app.route("/unreliable-news/")
def second_page():
    try:
        return render_template("second.html", page="Unreliable News", list1=links, list2=titles, list3=texts, num=len(links))
    except:
        print('\nerror in second_page func\n')

#third page runs java swing GUI application for drug abuse issue
@app.route("/drug-abuse/")
def third_page():
    try:
        return render_template("third.html")
    except:
        print('\nerror in third_page func\n')


urls = ["https://www.nbcnews.com/", "https://www.cnn.com/"]

if __name__ == "__main__":
    #scrape info info from websites into
    setNumOfArticles(10)
    for i in range(0, len(urls)): 
        getNews(urls[i])
        linksAdd = getLinks()
        links.extend(linksAdd)
        print('Links is ' + str(links))
        time.sleep(4)
        titlesAdd = getTitles()
        titles.extend(titlesAdd)
        textsAdd = getArticleText()
        texts.extend(textsAdd)
    #print('Titles are: ' + str(titles))
    #print('Links are: ' + str(links))
    #print('Bodies are: ' + str(texts))
    app.run(debug=True)