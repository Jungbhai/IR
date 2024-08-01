import requests
from bs4 import BeautifulSoup

URL = 'https://www.bbc.com/news/topics/cj3ergr8209t'

response = requests.get(URL)

print("The response code is:",response)

# parse the HTML document
soup = BeautifulSoup(response.content,'html.parser')
# print(soup)

# Extract the news headline from HTML
headlines = soup.find_all('p')

for headline in headlines:
    print(headline.get_text())
