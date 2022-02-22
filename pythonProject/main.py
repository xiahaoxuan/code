import requests


while True:
    r = requests.get("https://www.carde.shop/#/home")
    print(r)