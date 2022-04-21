from turtle import clear
import requests

from bs4 import BeautifulSoup

url_request = requests.get("https://news.ycombinator.com/news")
# url_request.text

all_news = BeautifulSoup(url_request.text, "html.parser")
# print(soup.prettify())

news_headlines = [news.getText() for news in all_news.find_all("a", class_="titlelink", limit=10)]
# print(news_headlines)

with open("news.txt", mode="w") as file:
    for news_headline in news_headlines:
        file.write(f"{news_headline} \n")

print("Done! News headlines write in to a file.")