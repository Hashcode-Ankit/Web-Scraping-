import requests
from bs4 import BeautifulSoup

URL = "https://gist.github.com/....."
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

title = soup.find("div", itemprop="about")
name = title.text.split('/')[-1]
print(name)

divs = soup.find_all("div", class_="file-actions")

for div in divs:
    href = div.find('a', href=True)['href']
    url = "https://gist.github.com" + href
    filename = "snippet_code/" + url.split('/')[-1]
    print(filename)

    file = requests.get(url)
    open(filename, 'wb').write(file.content)