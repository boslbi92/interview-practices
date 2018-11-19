import requests, re, json
from bs4 import BeautifulSoup
from tqdm import tqdm
import random

def get_hotels(url):
    r  = requests.get(url)
    text = r.text
    text = re.sub(r'[^\x00-\x7F]+',' ', text)
    soup = BeautifulSoup(text, "lxml")
    text = soup.prettify()
    text = re.sub(r'[^\x00-\x7F]+',' ', text)
    trip = 'https://www.tripadvisor.com'
    found, names = set(), set()
    for a in soup.find_all('a', href=True):
        found_url = a['href']
        if 'Hotel_Review' in found_url and '#REVIEWS' not in found_url:
            name = found_url.split('-Reviews-')[1].split('.html')[0]
            found.add((trip + found_url))
            names.add(name)
    return (names, found)

def extract_reviews(url):
    r  = requests.get(url)
    text = r.text
    text = re.sub(r'[^\x00-\x7F]+',' ', text)
    soup = BeautifulSoup(text, "lxml")
    text = soup.prettify()
    text = re.sub(r'[^\x00-\x7F]+',' ', text)
    reviews = list()
    for link in soup.find_all("p", {"class": "partial_entry"}):
        reviews.append(link.text)
    return reviews

url = "https://www.tripadvisor.com/Hotels-g45963-Las_Vegas_Nevada-Hotels.html"
name, hotels = get_hotels(url)

data = dict()
count = 0
for x, y in zip(name, hotels):
    data[x] = extract_reviews(y)
    break

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)


