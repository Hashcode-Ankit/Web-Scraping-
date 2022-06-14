import pandas as pd
from pandas.core.reshape import tile
from pytube import Playlist

play_list = Playlist("https://www.youtube.com/playlist?list=PL-Jc9J83PIiHxc8vuYMq3C1KUvqc_jB6L")
print("Found", len(play_list), "Videos in \"", play_list.title, "\"")

videos = {}

for video in play_list.videos:
    title = video.title.split("|")[0].rstrip()
    url = video.watch_url
    videos[title] = url


df = pd.read_csv("Level_1.csv")
for que in df["Question"]:
    if que in videos:
        print(que, "->", videos[que])
