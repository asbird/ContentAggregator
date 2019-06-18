import requests
from bs4 import BeautifulSoup
import pdb
import webbrowser

class Post:
    def __init__(self, title, link):
        self.title = title
        self.link = title


odpowiedz = requests.get("https://tim.blog/")
soup = BeautifulSoup(odpowiedz.text, 'html.parser')

mydivs = soup.findAll("h1", {"class": "entry-title"})

newestPosts = []
for x in mydivs:
    postTitle = x.string
    postLink = x.a.get('href')
    newestPosts.append(Post(postTitle, postLink))

pdb.set_trace()