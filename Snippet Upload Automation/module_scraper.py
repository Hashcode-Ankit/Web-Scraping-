import requests
from bs4 import BeautifulSoup

URL = "https://www.pepcoding.com/resources/online-java-foundation"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

module_list = soup.find_all("li", class_="classResourceList")

for module in module_list:
    topic_list = module.find_all("li", class_="list-item")
    for topic in topic_list:
        href = topic.find('a', href=True)['href']
        name = topic.text.lstrip().rstrip()
        print(name, "\t->", href)