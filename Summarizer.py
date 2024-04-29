import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article 

#nltk.download('punkt')

def summarize():
    url = utext.get('1.0', "end").strip()
    article_obj = Article(url)  
    article_obj.download()
    article_obj.parse()
    article_obj.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', "end")
    title.insert('1.0', article_obj.title) 

    author.delete('1.0', "end")
    author.insert('1.0', ', '.join(article_obj.authors))  # Convert authors list to a comma-separated string

    publication.delete('1.0', "end")
    publication.insert('1.0', str(article_obj.publish_date))  # Convert publish_date to string


    summary.delete('1.0', "end")
    summary.insert('1.0', article_obj.summary)

    analysis = TextBlob(article_obj.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')  # Fixed typo in "negative"

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlable = tk.Label(root, text="Title")
tlable.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

alabel = tk.Label(root, text="Author")  
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

plabel = tk.Label(root, text="Publication Date")  
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()

slabel = tk.Label(root, text="Summary") 
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

selabel = tk.Label(root, text="Sentiment")  
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

ulabel = tk.Label(root, text="Enter URL") 
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="SUMMARIZER", command=summarize)
btn.pack()

root.mainloop()
