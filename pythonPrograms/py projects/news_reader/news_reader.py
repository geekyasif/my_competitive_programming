import requests
import json
from win32com.client import Dispatch

def speak_news(articles):
    speak = Dispatch('SAPI.SpVoice')

    # iterating the articles by one by one and pass to speak module to speak
    for i in range(len(articles)):
        article = (i+1,articles[i])
        speak.Speak(article)


if __name__ == '__main__':
    #geting the data using news api news api
    news = requests.get("https://newsapi.org/v2/top-headlines?source=bbc_news&country=us&apiKey=")
    # parsing the data into json format
    json_news = news.json()

    #getting articles from the json file
    articles = json_news["articles"]

    #creating a empty list to store the titles from articles
    articles_list = []

    for article in articles:
        articles_list.append(article["title"])


    #calling the speak function and passing the list of title
    speak_news(articles_list)


