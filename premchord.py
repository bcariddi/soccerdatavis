#!/usr/bin/env python3

import requests
import re
import ssl
import itertools
from itertools import chain
import pandas as pd
from bs4 import BeautifulSoup
from chord import Chord

headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

ssl.match_hostname = lambda cert, hostname: True

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

names = ['AFC Bournemouth', 'Arsenal FC', 'Aston Villa', 'Brighton & Hove Albion', 'Burnley FC', 'Chelsea FC', 'Crystal Palace', 'Everton FC', 'Leicester City', 'Liverpool FC', 
        'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City', 'Sheffield United', 'Southampton FC', 'Tottenham Hotspur', 'Watford FC', 'West Ham United', 'Wolverhampton Wanderers']

colors = ['#B50E12', '#EF0107', '#670E36', '#0057B8', '#99D6EA', '#034694', '#A7A5A6', '#003399', '#FDBE11', '#C8102E',
          '#6CABDD', '#DA291C', '#241F20', '#00A650', '#0D171A', '#D71920', '#132257', '#FBEE23', '#7A263A', '#FDB913']

def get_player_hrefs():
    ogurl = 'https://www.worldfootball.net/players_list/eng-premier-league-2019-2020/nach-name/'
    numpages = 12
    playerhrefs = []

    for p in range(1, numpages + 1):
        url = ogurl + str(p) + '/'
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        players = soup.find_all('td', {'class': ['hell', 'dunkel'], 'nowrap' : True})
        for player in players:
            player = player.find('a')
            playerhref = player.get('href')
            playerhrefs.append(playerhref)

    return playerhrefs


def processplayer(href):
    ogurl = 'https://worldfootball.net'
    url = ogurl + href
    page = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')

    teams = []

    currentteam = soup.find_all('b')
    curr = currentteam[0].text.strip()
    if curr in names:
        teams.append(curr)

    formerteams = soup.find_all('td', {'class': ['hell', 'dunkel'], 'width' : '40%'})
    for team in formerteams:
        team = team.text.strip()
        if team not in teams and team in names:
            teams.append(team)

    return teams


playerhrefs = get_player_hrefs()

listteams = []

for n, href in enumerate(playerhrefs):
    print(n)
    teams = processplayer(href)
    listteams.append(teams)

c = [list(itertools.combinations(i, 2)) for i in listteams]
a = list(chain.from_iterable((i, i[::-1]) for c_ in c for i in c_))

df = pd.DataFrame(a)
matrix = pd.pivot_table(df, index=0, columns=1, aggfunc='size', fill_value=0)

counts = list(x for x in range(20))
mat = matrix
mat.columns = counts
mat.index   = counts 

m = mat.values.tolist()

names = ['Bournemouth', 'Arsenal', 'Aston Villa', 'Brighton', 'Burnley', 'Chelsea', 'Palace', 'Everton', 'Leicester', 'Liverpool',
        'Man City', 'Man United', 'Newcastle', 'Norwich', 'Sheffield', 'Southampton', 'Spurs', 'Watford', 'West Ham', 'Wolves']

Chord(m, names, colors=colors, wrap_labels=False, margin=50, font_size="14px", font_size_large="14px", padding=.01).to_html()
