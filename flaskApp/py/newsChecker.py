#import machine learning/data analysis libraries
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score

#global variables

def trainSetup():
    global tfidf_vectorizer, passive
    df = p.read_csv('../data/train.csv')
    df = df.dropna()
    messages = df.copy()
    #0 is unreliable, 1 is reliable

    #df.label.value_counts() shows how many are reliable or unreliable

    #place text in trainset (relationship between article text and if it is real or fake)
    trainSet1, testSet1, trainSet2, testSet2  = train_test_split(df['text'], df['label'], test_size= 0.1, random_state=5, shuffle=True)
    #vectorize text (convert to numerical representation)
    tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.5)

    #encode as type U
    numericTrain = tfidf_vectorizer.fit_transform(trainSet1.values.astype('U'))
    numericTest = tfidf_vectorizer.transform(testSet1.values.astype('U'))

    #passive aggressive strategy for determining true or false
    passive = PassiveAggressiveClassifier(max_iter=50)
    passive.fit(numericTrain, trainSet2) 


def checkFake(text):
    newTest = tfidf_vectorizer.transform([text])
    result = passive.predict(newTest)
    return result[0]

