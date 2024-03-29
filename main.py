from bs4 import BeautifulSoup
import requests
from collections import Counter

home_id = input('input home team player IDs separated by an space')
away_id = input('input away team player IDs separated by an space')

home_sum = 0
home_players = []
away_sum = 0
away_players= []

for id in home_id:

    livefpl_url = f'https://livefpl.net/{id}'
    fplteam_url = f'https://fpl.team/live/{id}'

    livefpl_page = requests.get(livefpl_url).text
    fplteam_page = requests.get(fplteam_url).text

    livefpl_soup = BeautifulSoup(livefpl_page, "lxml")
    fplteam_soup = BeautifulSoup(fplteam_page, "lxml")

    user_name_element = livefpl_soup.select_one('body > section:nth-of-type(2) > div > div:nth-of-type(1) > p:nth-of-type(1)')

    user_point_element = livefpl_soup.select_one('body > section:nth-of-type(4) > div:nth-of-type(2) > table > tbody > tr:nth-of-type(1) > td:nth-of-type(2)')
    
    print(user_name_element.text, user_point_element.text.split()[3])
    
    home_sum += int(user_point_element.text.split()[3])

    gk_name = fplteam_soup.select_one('body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1) > div > div > div:nth-of-type(2)')
    home_players.append(gk_name.text)

    for i in range(1, 6):
        def_name = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type({i}) > div > div:nth-of-type(2)')
        if def_name is not None:
            home_players.append(def_name.text)
            cap_wid = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type({i}) > div > div:nth-of-type(1)')
            cap_wid = cap_wid.find(name="svg").get('style')
            if cap_wid is not None:
                home_players.append(def_name.text)
    for i in range(1, 6):
        mid_name = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type({i}) > div > div:nth-of-type(2)')
        if mid_name is not None:
            home_players.append(mid_name.text)
            cap_wid = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type({i}) > div > div:nth-of-type(1)')
            cap_wid = cap_wid.find(name="svg").get('style')
            if cap_wid is not None:
                home_players.append(mid_name.text)
    for i in range(1, 4):
        fwd_name = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > div:nth-of-type({i}) > div > div:nth-of-type(2)')
        if fwd_name is not None:
            home_players.append(fwd_name.text)
            cap_wid = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > div:nth-of-type({i}) > div > div:nth-of-type(1)')
            cap_wid = cap_wid.find(name="svg").get('style')
            if cap_wid is not None:
                home_players.append(fwd_name.text)
            
for id in away_id:

    livefpl_url = f'https://livefpl.net/{id}'
    fplteam_url = f'https://fpl.team/live/{id}'

    livefpl_page = requests.get(livefpl_url).text
    fplteam_page = requests.get(fplteam_url).text

    livefpl_soup = BeautifulSoup(livefpl_page, "lxml")
    fplteam_soup = BeautifulSoup(fplteam_page, "lxml")

    user_name_element = livefpl_soup.select_one('body > section:nth-of-type(2) > div > div:nth-of-type(1) > p:nth-of-type(1)')

    user_point_element = livefpl_soup.select_one('body > section:nth-of-type(4) > div:nth-of-type(2) > table > tbody > tr:nth-of-type(1) > td:nth-of-type(2)')
    
    print(user_name_element.text, user_point_element.text.split()[3])
    
    away_sum += int(user_point_element.text.split()[3])

    gk_name = fplteam_soup.select_one('body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1) > div > div > div:nth-of-type(2)')
    away_players.append(gk_name.text)

    for i in range(1, 6):
        def_name = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type({i}) > div > div:nth-of-type(2)')
        if def_name is not None:
            away_players.append(def_name.text)
            cap_wid = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type({i}) > div > div:nth-of-type(1)')
            cap_wid = cap_wid.find(name="svg").get('style')
            if cap_wid is not None:
                away_players.append(def_name.text)
    for i in range(1, 6):
        mid_name = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type({i}) > div > div:nth-of-type(2)')
        if mid_name is not None:
            away_players.append(mid_name.text)
            cap_wid = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type({i}) > div > div:nth-of-type(1)')
            cap_wid = cap_wid.find(name="svg").get('style')
            if cap_wid is not None:
                away_players.append(mid_name.text)
    for i in range(1, 4):
        fwd_name = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > div:nth-of-type({i}) > div > div:nth-of-type(2)')
        if fwd_name is not None:
            away_players.append(fwd_name.text)
            cap_wid = fplteam_soup.select_one(f'body > main > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > div:nth-of-type({i}) > div > div:nth-of-type(1)')
            cap_wid = cap_wid.find(name="svg").get('style')
            if cap_wid is not None:
                away_players.append(fwd_name.text)
c_home_players = Counter(home_players)
c_away_players = Counter(away_players)
print(f"home team players: {c_home_players}")
print(f"total point is: {home_sum}")
print(f"away team players: {c_away_players}")
print(f"total point is: {away_sum}")
print(f"effective players of home team: {c_home_players-c_away_players}")
print(f"effective players of away team: {c_away_players-c_home_players}")