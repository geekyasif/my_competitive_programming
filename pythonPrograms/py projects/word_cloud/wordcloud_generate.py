import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import wikipedia

def wiki(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content


def create_word_cloud(text):
    stopwords = STOPWORDS

    wc = WordCloud(
        background_color='black',
        stopwords=stopwords,
        height=500,
        width=400,
        max_words=40
    )

    wc.generate(text)
    wc.to_file('word.png')


# text = open('sampleWords.txt','r').read()

text = wiki('python programming')
create_word_cloud(text)