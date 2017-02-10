"""
By Bradley Robinson"""import pandas as pd
import requests
from bs4 import BeautifulSoup


games = pd.read_csv("games.csv")
small_dataset = games.iloc[0:10]

def get_reviews(divs):
    reviews = {'recommended': [], 'text': []}
    for d in divs:
        print('...', end='')
        attribs = d.attrs
        if 'class' in attribs:
            if attribs['class'] == ['title']:
                reviews['recommended'].append(d.text)
            elif attribs['class'] == ['apphub_CardTextContent']:
                reviews['text'].append(d.text)
    return reviews

def get_page(page, steam_id):
    print('hi')
    response = requests.get("http://steamcommunity.com/app/" + str(steam_id) + "/reviews/?p=1&browsefilter=mostrecent")
    content  = response.content
    parser = BeautifulSoup(content, 'html.parser')
    divs = parser.find_all('div')
    reviews = get_reviews(divs)
    return reviews
	
g_dict = {}
for i in range(10):
	g_dict[games['game'].iloc[i]] = get_page(1, games['game_id'].iloc[i])

pd.DataFrame(g_dict).to_csv("reviews")