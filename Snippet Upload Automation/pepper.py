import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.pepcoding.com/resources/online-java-foundation"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

module_list = soup.find_all("li", class_="classResourceList")

question_id = []
question_name = []
topic_name = []
module_name = []

for module in module_list:
    module_div = module.find("div", class_="collapsible-header")
    mname = module_div.text.lstrip().rstrip()
    
    topic_list = module.find_all("li", class_="list-item")
    for topic in topic_list:
        topic_href = "https://www.pepcoding.com" + topic.find('a', href=True)['href']
        tname = topic.text.lstrip().rstrip()
        
        topic_page = requests.get(topic_href)
        topic_soup = BeautifulSoup(topic_page.content, "html.parser")
        question_list = topic_soup.find_all("li", attrs={"resource-type":"ojquestion"})

        count = 0
        for question in question_list:
            qname = question.find('a', href=True).text.lstrip().rstrip()
            qid = question['resource-type-id']
            
            question_id.append(qid)
            question_name.append(qname)
            topic_name.append(tname)
            module_name.append(mname)
            count += 1
        print(count, "->", tname)


dict = {"ID": question_id, "Question": question_name, "Topic": topic_name, "Module": module_name}
df = pd.DataFrame(dict)

df.to_csv('question_list.csv', index=False)