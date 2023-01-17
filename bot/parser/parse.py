from pathlib import Path

import requests
from bs4 import BeautifulSoup
import json

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
url = 'https://habr.com/'
req = requests.get(url=url, headers=headers)

soup = BeautifulSoup(req.text, 'lxml')
articles_cards = soup.find_all("div", class_="tm-article-snippet")

def get_id(article):
        href = article.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2").find("a",
                                                                                                        class_='tm-article-snippet__title-link').get(
            'href')
        article_id = href.split("/")[::-1]
        article_id = int(article_id[1])
        return article_id

def get_title(article):
        article_title = article.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2").text.strip()
        return article_title

def get_desc(article):
        article_desc = article.find("p")
        if article_desc == None:
            article_desc = article.find("div",
                                        class_='article-formatted-body article-formatted-body article-formatted-body_version-1').get_text()
        else:
            article_desc = article.find("p").get_text()
        return article_desc

def get_time(article):
        article_date_time = article.find("time").get("title")
        return article_date_time

def get_url(article):
    href = article.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2").find("a",
                                                                                                        class_='tm-article-snippet__title-link').get(
            'href')
    url = f'https://habr.com{href}'
    return url

def search():
    news_dict = {}
    for article in articles_cards:
        news_dict[get_id(article)] = {
            "article_date_time": get_time(article),
            "articles_title": get_title(article),
            "article_url": get_url(article),
            "article_desc": get_desc(article)
        }
    return news_dict

def get_first_news():
    with open("news_dict.json", "w", encoding="utf-8") as file:
        json.dump(search(), file, indent=4, ensure_ascii=False)

def check_news_update():
    with open(Path.home() / ("PycharmProjects\\TwitchTgBot\\bot\\parser\\news_dict.json"),
              encoding='utf-8') as file:
        news_dict = json.load(file)
        fresh_news = {}
    for article in articles_cards:
        article_id = str(get_id(article))
        if article_id in news_dict:
            continue
        else:
            fresh_news[article_id] = {
                "article_date_time": get_time(article),
                "articles_title": get_title(article),
                "article_url": get_url(article),
                "article_desc": get_desc(article)
            }
            with open((Path.home() / ("PycharmProjects\\TwitchTgBot\\bot\\parser\\news_dict.json")), "w", encoding='utf-8') as file:
                json.dump(search(), file, indent=4, ensure_ascii=False)

    return fresh_news

def main():
    get_first_news()


if __name__ == '__main__':
    main()
