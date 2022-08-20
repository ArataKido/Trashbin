import requests
from constant import API_KEY_IMDB

respone = requests.get(f"https://imdb-api.com/en/API/Top250Movies/{API_KEY_IMDB}").json()['items']
list_of_films = []
for i in range(0,10):
	list_of_films.append(respone[i]['title'])
print(f"{list_of_films}\n\n")
print("".join(list_of_films))
