from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_soup(url):
    response = requests.get(url)
    html = response.text
    return BeautifulSoup(html, 'lxml')

def get_content_by_tag(tag):
    elements = soup.find_all(tag)
    return [element.text.strip() for element in elements]

soup = get_soup('https://www.scrapethissite.com/pages/')

titles = get_content_by_tag('h3')
descriptions = get_content_by_tag('p')

data = { 'Title': titles, 'Description': descriptions }
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)
