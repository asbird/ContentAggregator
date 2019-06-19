import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pdb
import webbrowser
import re
import time

class Post:
    def __init__(self, title,
                 link, dateTime):
        self.title = title
        self.link = link
        self.dateTime = dateTime

class TimBlog:
    newestPosts = []

    def getWebContent(self):
        odpowiedz = requests.get("https://tim.blog/")
        soup = BeautifulSoup(odpowiedz.text, 'html.parser')
        webContent = soup.findAll("header", {"class": "entry-header"})
        return webContent

    def uploadPosts(self, webContent):
        for x in webContent:
            postTitle = x.find("h1", {"class" : "entry-title"}).a.string
            postLink = x.a.get('href')
            dateTime = TimBlog.formatDateTime(
                        x.find("time", {"class" : "entry-date published"})
                        .get('datetime'))
            self.newestPosts.append(Post(postTitle, postLink, dateTime))

    def formatDateTime(Date):
        day = re.findall('(.+)[T]',Date)
        time = re.findall('[T](.+)[-]',Date)
        date_time = (''.join(day))+' '+str(''.join(time));
        date_time_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        return date_time_obj

TB = TimBlog()
TB.uploadPosts(TB.getWebContent())

for post in TB.newestPosts:
    print('Title: '+post.title
        +'\nLink: '+post.link
        +'\nDate and Time: '+str(post.dateTime)+'\n')
    time.sleep(1)

# pdb.set_trace()


# webbrowser.open_new_tab(newestPosts[0].link)
