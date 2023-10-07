
from bs4 import BeautifulSoup
import requests
import numpy as np 

headers = {'user-agent': 'my-agent/1.0.1'}

page_link = 'https://rttf.ru/players/'

data = []

def get_players_data(players_list):
    for player in players_list:
        page = requests.get(page_link+player, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        name = soup.find(class_='player-info').findAll('h1')[0].contents[0]
        rate = soup.find(class_='player-info').findAll('h3')[0].find('dfn').contents[0]
        last_tournament = soup.find(class_='player-results').findAll('a', href=True)
        last_tournament= [x for x in last_tournament if 'tournaments' in x['href']]
        last_tournament = [x.text.split('<var>')[0] for x in last_tournament][0][:10]
        data.append([name, rate, last_tournament])
    df = np.array(data)
    df = np.concatenate([np.arange(1, len(df)+1).reshape(-1,1), df[df[:,-2].argsort()[::-1]]], axis=1)
    data = df.tolist()
    return data