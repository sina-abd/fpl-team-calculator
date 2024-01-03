from bs4 import BeautifulSoup
import requests
from lxml import etree

portvale_id = ['14502', '17950', '1401154', '1267063', '4252172', '21057']
away_id = []
sum = 0
for id in portvale_id:
    livefpl_url = f'https://livefpl.net/{id}'
    user_page = requests.get(livefpl_url).text
    soup = BeautifulSoup(user_page, "lxml")
    player_name_element = soup.select_one('body > section:nth-of-type(2) > div > div:nth-of-type(1) > p:nth-of-type(1)')
    player_point_element = soup.select_one('body > section:nth-of-type(4) > div:nth-of-type(2) > table > tbody > tr:nth-of-type(1) > td:nth-of-type(2)').text
    print(player_name_element.text, player_point_element.split()[3])
    sum += int(player_point_element.split()[3])
    
print(f"total point is: {sum}")