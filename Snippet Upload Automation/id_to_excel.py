import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://www.pepcoding.com/resources/online-java-foundation/linked-lists"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

question_list = soup.find_all("li", attrs={"resource-type":"ojquestion"})

name = [question.find('a', href=True).text.lstrip().rstrip() for question in question_list]
id = [question['resource-type-id'] for question in question_list]

dict = {"Question Name": name, "Question ID": id}
df = pd.DataFrame(dict)

df.to_csv('question_list.csv', index=False)