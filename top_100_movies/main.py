from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage,"html.parser")
titles = soup.find_all(name="h3",class_="title")
title_texts = []
for title_text in titles:
    text = title_text.getText()
    title_texts.append(text)

movies = title_texts[::-1]
with open("movies.txt",mode="w",encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")





