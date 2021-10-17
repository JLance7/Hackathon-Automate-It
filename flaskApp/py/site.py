#flask website app for displaying reliable news from newsGrabber file
from flask import Flask, redirect, url_for, render_template
from scrape import *
import time
from newsChecker import *

#main lists
links = []
titles = []
texts = []

#reliable
validLink = []
validTitle = []
validTexts = []

#failed test (unreliable)
invalidLink = []
invalidTitle = []
invalidTexts = []

app = Flask(__name__)
app = Flask(__name__, static_folder='../static', template_folder='../html')


#if no subdirectory url is given show reliable news (index.html)
@app.route("/")
def home():
    try:
        return redirect(url_for("first_page"))
    except:
        print('\nerror in other func\n')

#reliable-news subdirectory url
@app.route("/reliable-news/")
def first_page():
    try:
        return render_template("index.html", page="Reliable News", list1=validLink, 
            list2=validTitle, list3=validTexts, num=len(links), valid=len(validLink))
    except:
        print('\nerror in first_page func\n')

#unreliable-news subdirectory url
@app.route("/unreliable-news/")
def second_page():
    try:
        return render_template("second.html", page="Unreliable News", list1=invalidLink, list2=invalidTitle, 
            list3=invalidTexts, num=len(links), valid=(len(invalidLink)))
    except:
        print('\nerror in second_page func\n')

#third page runs java swing GUI application for drug abuse issue
@app.route("/drug-abuse/")
def third_page():
    try:
        return render_template("third.html")
    except:
        print('\nerror in third_page func\n')


urls = ["https://www.nbcnews.com/"]

if __name__ == "__main__":
    #scrape info info from websites into
    setNumOfArticles(10)
    for i in range(0, len(urls)): 
        getNews(urls[i])
        links = getLinks()
        #print('Links is ' + str(links))
        titles = getTitles()
        texts = getArticleText()
    #print('Titles are: ' + str(titles))
    #print('Links are: ' + str(links))
    #print('Bodies are: ' + str(texts))
    trainSetup()
    
    #uncomment this block and comment bottom block for full functionality
    for i in range(len(titles)):
        try:
            articleResponse = checkFake(titles[i])
            #if valid add values to valid lists
            if articleResponse == 1:
                validLink.append(links[i])
                validTitle.append(titles[i])
                validTexts.append(texts[i])
            else:
                invalidLink.append(links[i])
                invalidTitle.append(titles[i])
                invalidTexts.append(texts[i])
        except:
            print('error in site main')

    #for testing webscraping
    # list1 = links
    # list2 = titles
    # list3 = texts

    app.run(debug=True)