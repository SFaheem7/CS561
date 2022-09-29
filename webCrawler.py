import requests
from bs4 import BeautifulSoup

href = []
homepagecount = 0
count = 0
mypu = 0

def crw(url):
    line = requests.get(url)
    lines = line.text
    global count
    global homepagecount
    u = BeautifulSoup(lines, 'html.parser')
    for urls in u.find_all('a'):
        ref = urls.get('href')
        count = count + 1
        if (url in ref) and (url != ref) and (ref is not None) and (ref not in href):
            print(ref)
            href.append(ref)
            crw(ref)
        elif (url == ref) and homepagecount == 0 and ref is not None:
            print(ref)
            homepagecount = homepagecount + 1
            crw(url)
    print(count)


crw("https://www.stencia.com/blog/2017/6/15/security-cracking-passwords")
