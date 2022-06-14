import requests
from bs4 import BeautifulSoup

URL = "https://www.pepcoding.com/resources/online-java-foundation/linked-lists"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

question_list = soup.find_all("li", attrs={"resource-type":"ojquestion"})

for question in question_list:
    a = question.find('a', href=True)
    href = a['href']
    name = a.text.lstrip().rstrip()
    id = question['resource-type-id']
    print(name, "\t->", href)