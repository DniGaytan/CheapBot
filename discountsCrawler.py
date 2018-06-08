#Automated file that will crawl discounts for the stored games in games.txt

import requests

with open('games.txt') as file:
    games = file

games.split('\n')

print(games)