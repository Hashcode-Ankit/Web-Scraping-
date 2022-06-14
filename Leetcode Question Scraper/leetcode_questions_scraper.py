import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://leetcode.com/problemset/all/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


divs = soup.find_all("div", class_="group flex items-center m-[10px]")

topic = []
que_count = []
total = 0

for div in divs:
    span = div.find_all("span")
    name = span[0].text
    count = span[1].text

    total += int(count)
    topic.append(name)
    que_count.append(count)

topic.append("TOTAL")
que_count.append(total)
dict = {"Topic Name": topic, "Questions Count": que_count}
df = pd.DataFrame(dict)

df.to_csv('leet_questions.csv', index=False)