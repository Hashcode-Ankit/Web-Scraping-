from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://www.appliedaicourse.com/course/11/Applied-Machine-learning-course")
soup = BeautifulSoup(page.content, "html.parser")

module_name = []
topic_name = []
sno = []
que_name = []
duration = []

modules = soup.find_all("div", class_="col-12 col-md-12 p-2")
for module in modules:
    module_name.append(module.font.text)
    topic_name.append("")
    # sno.append("")
    # que_name.append("")
    # duration.append("")

    topics = module.find_all("div", class_="card p-0")
    count = 1
    for topic in topics:
        module_name.append("")
        topic_name.append("\t" + str(count) +". " + topic.a.text.strip())
        count += 1
        # topic_name.append(topic.a.text.strip())
        # sno.append("")
        # que_name.append("")
        # duration.append("")

        # ques = topic.find_all("div", class_="card-body px-4 p-2 card-body-n")
        # for que in ques:
        #     module_name.append("")
        #     topic_name.append("")
            # sno.append(que.div.div.text.strip())
            # que_name.append(que.a.text.strip())
            # duration.append(que.span.text.strip())

# dist = {"Modules":module_name, "Topics": topic_name, "SNO":sno, "Sub Topics":que_name, "Duration":duration}
# df = pd.DataFrame(dist)

# df.to_csv("Applied ML Course Outline.csv", index=False)


dist = {"Modules":module_name, "Topics":topic_name}
df = pd.DataFrame(dist)

df.to_csv("Applied ML Topics.csv", index=False)