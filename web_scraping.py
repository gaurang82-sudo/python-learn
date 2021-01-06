import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(response.text, "html.parser")


questions = soup.select(".question-summary")
for que in questions:
    print(que.select_one(".question-hyperlink").getText())
    print(que.select_one(".vote-count-post").getText())
