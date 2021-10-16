#flask website app for displaying reliable news from newsGrabber file
from flask import Flask, redirect, url_for, render_template
#from newsGrabber import *

app = Flask(__name__)
app = Flask(__name__, static_folder='../static', template_folder='../html')

#if no subdirectory url is given show reliable news (index.html)
@app.route("/")
def home():
    try:
        return render_template("index.html", page="Reliable News", list=["blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah"])
    except:
        print('\nerror in home\n')

#any other subdirectory url given
@app.route("/<name>/")
def other(name):
    try:
        return redirect(url_for("home"))
    except:
        print('\nerror in other func\n')

#reliable-news subdirectory url
@app.route("/reliable-news/")
def first_page():
    try:
        return render_template("index.html", page="Reliable News", list=["blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah"])
    except:
        print('\nerror in first_page func\n')

#unreliable-news subdirectory url
@app.route("/unreliable-news/")
def second_page():
    try:
        return render_template("second.html", page="Unreliable News", list=["woo", "woo", "woo", "woo", "woo", "woo", "woo", "woo", "woo", "woo"])
    except:
        print('\nerror in second_page func\n')

#third page runs java swing GUI application for drug abuse issue
@app.route("/drug-abuse/")
def third_page():
    try:
        return render_template("third.html")
    except:
        print('\nerror in third_page func\n')


#scrape info info from websites into 


if __name__ == "__main__":
    app.run(debug=True)